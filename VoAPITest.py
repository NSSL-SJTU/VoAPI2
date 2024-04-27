import os, time, copy, json, argparse
from VoAPIGlobalData import *
from RESTlerCompileParser import *
from VoAPITemplate import *
from VoAPIUtils import *
from urllib3 import encode_multipart_formdata

def candidate_apis_test(baseurl, header_dict, param_dict, output_dir, api_template_list, candidate_api_list, api_validity_json, no_get_producer, open_isrequired, need_trigger, log_file):
    for candidate_api in candidate_api_list:
        #try:
        if candidate_api[0].api_url in JellyfinBugUrls:
            continue
        candidate_api_template = candidate_api[0]
        candidate_api_test_types = candidate_api[1]
        candidate_api_index = api_template_list.index(candidate_api_template)
        candidate_api_producer_pool = api_template_list[:candidate_api_index] + api_template_list[candidate_api_index+1:]
        candidate_api_seq, candidate_api_seq_relations = reverse_sequence_construction(candidate_api_template, candidate_api_producer_pool, no_get_producer)
        write_every_candidate_api_test_log(log_file, candidate_api_seq, candidate_api_seq_relations, candidate_api_test_types)
        finished_flag = True
        unfinished_seq_dir = output_dir + "unfinished_seq/"
        for api_index in range(len(candidate_api_seq)-1):
            current_api = candidate_api_seq[api_index]
            parameter_values_generation(current_api, candidate_api_seq_relations)
            temp_request_value = copy.deepcopy(current_api.api_request_value)
            if param_dict:
                update_api_request_param_value_by_custom_param_dict(temp_request_value, param_dict)
            request_dict_list = format_request(temp_request_value, current_api.api_request, open_isrequired)
            response = request_sender(baseurl, current_api.api_url, current_api.api_method, header_dict, request_dict_list, log_file)
            valid_flag = True
            if response != None:
                if api_validity_json:
                    if (api_validity_json["success_str"] in response.text) and (api_validity_json["fail_str"] not in response.text):
                        if "Content-Type" in response.headers:
                            if "json" in response.headers["Content-Type"]:
                                response_json = json.loads(response.text)
                                update_api_response_value_by_response_json(current_api.api_response_value, response_json)
                            else:
                                #ToDo: Support Other Content-Type
                                pass
                    else:
                        valid_flag = False
                else:
                    if (str(response.status_code)[0] == "2"):
                        if "Content-Type" in response.headers:
                            if "json" in response.headers["Content-Type"]:
                                response_json = json.loads(response.text)
                                update_api_response_value_by_response_json(current_api.api_response_value, response_json)
                            else:
                                #ToDo: Support Other Content-Type
                                pass
                    else:
                        valid_flag = False
            else:
                valid_flag = False
            if not valid_flag:
                # Record
                record_unfinished_seq(candidate_api_template, candidate_api_seq, current_api, unfinished_seq_dir)
                finished_flag = False
                break
        if finished_flag:
            vul_dir = output_dir + "vul/"
            undetected_suspicious_dir = output_dir + "undetected_suspicious/"
            parameter_values_generation(candidate_api_template, candidate_api_seq_relations)
            for candidate_api_test_type in candidate_api_test_types:
                if candidate_api_test_type in ["proxy_api", "command_api", "display_api"]:
                    test_payloads = ApiVulnerabilityPayloads[candidate_api_test_type]
                    test_params = candidate_api_test_types[candidate_api_test_type]
                    vul_output_dir = vul_dir + APIFuncAndVulMapping[candidate_api_test_type] + "/"
                    if not os.path.exists(vul_output_dir):
                        os.makedirs(vul_output_dir)
                    for test_param in test_params:
                        for test_payload in test_payloads:
                            vul_location_str = (candidate_api_template.api_url + "VoAPI" + test_param).replace("{","!").replace("}","!")
                            vul_output_file = vul_location_str.replace("/","!")
                            test_payload = test_payload.format(vul_location_str)
                            request_value_struct = copy.deepcopy(candidate_api_template.api_request_value)
                            if param_dict:
                                update_api_request_param_value_by_custom_param_dict(request_value_struct, param_dict)
                            update_api_request_param_value(request_value_struct, test_param, [test_payload, "VoAPI_TEST"])
                            test_request_dict_list = format_request(request_value_struct, candidate_api_template.api_request, open_isrequired)
                            response = request_sender(baseurl, candidate_api_template.api_url, candidate_api_template.api_method, header_dict, test_request_dict_list, log_file)
                            # sleep time for vul request
                            time.sleep(0.4)
                            if candidate_api_test_type == "display_api":
                                if (candidate_api_template.api_method.lower() == "post") and (response != None) and (str(response.status_code)[0] == "2"):
                                    record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload, request_validation_api=False)
                            if os.path.exists(vul_output_dir + vul_output_file):
                                #record_vul_api
                                record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload, request_validation_api=True)
                            else:
                                # vul not exist
                                if need_trigger:
                                    if (candidate_api_template.api_method.lower() == "post") and (response != None) and (str(response.status_code)[0] == "2"):
                                        #need_trigger
                                        api_triggers = find_triggers(candidate_api_template, api_template_list)
                                        vul_flag = False
                                        for api_trigger in api_triggers:
                                            ## appwrite bug
                                            if api_trigger.api_url == "/health/time":
                                                continue
                                            ## trick: microcks trigger
                                            if api_trigger.api_method.lower() != "get":
                                                microcks_response_json = json.loads(response.text)
                                                request_value_struct = copy.deepcopy(api_trigger.api_request_value)
                                                request_value_struct["path"]["id"] = [microcks_response_json["id"], "VoAPI_PRODUCER"]
                                                request_dict_list = format_request(request_value_struct, api_trigger.api_request, open_isrequired)
                                                request_sender(baseurl, api_trigger.api_url, api_trigger.api_method, header_dict, request_dict_list, log_file)
                                            else:    
                                                request_sender(baseurl, api_trigger.api_url, api_trigger.api_method, header_dict, [{}, {}, {}, {}], log_file)
                                            # sleep time for vul request
                                            time.sleep(0.4)
                                            if os.path.exists(vul_output_dir + vul_output_file):
                                                record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload, request_validation_api=True)
                                                vul_flag = True
                                                break
                                #         if not vul_flag:
                                #             # record not detect vul
                                #             record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                                #     else:
                                #         # record not detect vul
                                #         record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                                # else:
                                #     # record not detect vul
                                #     record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                elif candidate_api_test_type == "path_api":
                    test_payloads = ApiVulnerabilityPayloads[candidate_api_test_type]
                    test_params = candidate_api_test_types[candidate_api_test_type]
                    vul_output_dir = vul_dir + APIFuncAndVulMapping[candidate_api_test_type] + "/"
                    if not os.path.exists(vul_output_dir):
                        os.makedirs(vul_output_dir)
                    for test_param in test_params:
                        for test_payload in test_payloads:
                            request_value_struct = copy.deepcopy(candidate_api_template.api_request_value)
                            if param_dict:
                                update_api_request_param_value_by_custom_param_dict(request_value_struct, param_dict)
                            update_api_request_param_value(request_value_struct, test_param, [test_payload, "VoAPI_TEST"])
                            test_request_dict_list = format_request(request_value_struct, candidate_api_template.api_request, open_isrequired)
                            response = request_sender(baseurl, candidate_api_template.api_url, candidate_api_template.api_method, header_dict, test_request_dict_list, log_file)
                            if response != None:
                                if api_validity_json:
                                    if (api_validity_json["success_str"] in response.text) and (api_validity_json["fail_str"] not in response.text) and (("; for 16-bit" in response.text) or ("root:" in response.text)):
                                        record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload[0], request_validation_api=False)
                                    # else:
                                    #     record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                                else:
                                    if str(response.status_code)[0] == "2" and (("; for 16-bit" in response.text) or ("root:" in response.text)):
                                        # record vul
                                        record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload[0], request_validation_api=False)
                                    # else:
                            #             record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                            # else:
                            #     # record not detect vul
                            #     record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                elif candidate_api_test_type == "database_api":
                    test_params = candidate_api_test_types[candidate_api_test_type]
                    vul_output_dir = vul_dir + APIFuncAndVulMapping[candidate_api_test_type] + "/"
                    if not os.path.exists(vul_output_dir):
                        os.makedirs(vul_output_dir)
                    request_value_struct = copy.deepcopy(candidate_api_template.api_request_value)
                    if param_dict:
                        update_api_request_param_value_by_custom_param_dict(request_value_struct, param_dict)
                    test_request_dict_list = format_request(request_value_struct, candidate_api_template.api_request, open_isrequired)
                    try:
                        inject_param_list = sqlmap_test(baseurl, candidate_api_template.api_url, candidate_api_template.api_method, header_dict, test_request_dict_list, test_params, log_file)
                    except:
                        continue
                    if inject_param_list:
                        for inject_param in inject_param_list:
                            record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, inject_param, "SQLMap heuristic (basic) test", request_validation_api=False)
                    # else:
                    #     record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, str(test_params), undetected_suspicious_dir)
                elif candidate_api_test_type == "upload_api":
                    test_payloads = ApiVulnerabilityPayloads[candidate_api_test_type]
                    test_params = candidate_api_test_types[candidate_api_test_type]
                    vul_output_dir = vul_dir + APIFuncAndVulMapping[candidate_api_test_type] + "/"
                    if not os.path.exists(vul_output_dir):
                        os.makedirs(vul_output_dir)
                    for test_param in test_params:
                        for test_payload in test_payloads:
                            request_value_struct = copy.deepcopy(candidate_api_template.api_request_value)
                            if param_dict:
                                update_api_request_param_value_by_custom_param_dict(request_value_struct, param_dict)
                            file_data = {test_param: (test_payload[0], open(test_payload[1], 'rb').read())}
                            multipart_formdata = encode_multipart_formdata(file_data)
                            test_request_dict_list = format_request(request_value_struct, candidate_api_template.api_request, open_isrequired)
                            test_request_dict_list = list(test_request_dict_list)
                            test_request_dict_list[3] = multipart_formdata[0]
                            header_dict['Content-Type'] = multipart_formdata[1]
                            response = request_sender(baseurl, candidate_api_template.api_url, candidate_api_template.api_method, header_dict, test_request_dict_list, log_file, upload_flag=True)
                            if response != None:
                                if api_validity_json:
                                    if (api_validity_json["success_str"] in response.text) and (api_validity_json["fail_str"] not in response.text):
                                        record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload[0], request_validation_api=False)
                                    #     upload_paths = try_extract_upload_path(response.text)
                                    #     for upload_path in upload_paths:
                                    #         # try execute webshell
                                    #         webshell_response = request_sender(baseurl, upload_path, "Get", header_dict, [{}, {}, {}, {}], log_file)
                                    #         if (webshell_response) and ("VoAPI WebShell" in webshell_response.text):
                                    #             record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload[0], request_validation_api=False)
                                    #         else:
                                    #             record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                                    # else:
                                    #     record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                                else:
                                    if str(response.status_code)[0] == "2":
                                        record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload[0], request_validation_api=False)
                                        # upload_paths = try_extract_upload_path(response.text)
                                        # for upload_path in upload_paths:
                                        #     # try execute webshell
                                        #     webshell_response = request_sender(baseurl, upload_path, "Get", header_dict, [{}, {}, {}, {}], log_file)
                                        #     if (webshell_response) and ("VoAPI WebShell" in webshell_response.text):
                                        #         record_vul_api(vul_output_dir, candidate_api_test_type, candidate_api_template, test_param, test_payload[0], request_validation_api=False)
                                        #     else:
                                        #         record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                            #         else:
                            #             record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                            # else:
                            #     # record not detect vul
                            #     record_undetected_suspicious_api(candidate_api_template, candidate_api_test_type, test_param, undetected_suspicious_dir)
                else:
                    print("Not Supported API Func: ", candidate_api_test_type)
        # except Exception as e:
        #     continue

# def api_template_list_example():
#     api_url = "/Repositories"
#     api_method = "Post"
#     api_request = {'path': {}, 'header': {}, 'query': {}, 'body': {'body': ['Array', {'Enabled': ['Bool', [], ['RESTlerBool'], False], 'Name': ['String', [], ['RESTlerString'], False], 'Url': ['String', [], ['RESTlerString'], False]}, True]}}
#     api_response = {'bodyResponse': {}, 'headerResponse': {}}
#     return [ApiTemplate(api_url, api_method, api_request, api_response)]

def api_func_statistics(candidate_api_list):
    APIClassificationDict = {}
    for api_func in ApiFuncList:
        APIClassificationDict[api_func] = []
    for candidate_api in candidate_api_list:
        candidate_api_template = candidate_api[0]
        candidate_api_test_types = candidate_api[1]
        for api_func in candidate_api_test_types.keys():
            APIClassificationDict[api_func].append([candidate_api_template.api_url, candidate_api_template.api_method])
    result = json.dumps(APIClassificationDict, indent=2)
    f = open("APIClassificationDict.txt", "w")
    f.write(result)
    f.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--openapi', help='OpenAPI File Path For Resolve "multipart/form-data" to Support Upload API', type=str, default=None, required=False)
    parser.add_argument('--restler_compile', help='RESTler Compile File Path', type=str, default="APIInfo.txt", required=False)
    parser.add_argument('--verification_server_ip', help='Verification Server IP', type=str, default="127.0.0.1", required=False)
    parser.add_argument('--verification_server_port', help='Verification Server Port', type=int, default=4444, required=False)
    parser.add_argument('--verification_server_port_for_https', help='Verification Server Port For Https', type=int, default=4445, required=False)
    parser.add_argument('--baseurl', help='Target API Service Base Url', type=str, default="http://127.0.0.1", required=False)
    parser.add_argument('--output', help='Output Dir Absolute Path', type=str, default="./", required=False)
    parser.add_argument('--upload_payloads_dir', help='Upload Payloads Dir Absolute Path', type=str, default=None, required=False)
    parser.add_argument('--api_header_file', help='API Header File for Using API', type=str, default=None, required=False)
    parser.add_argument('--api_content_type', help='API Request Content-Type Header for Using API', type=str, default="application/json", required=False)
    parser.add_argument('--api_param_file', help='API Param File for Using API', type=str, default=None, required=False)
    parser.add_argument('--api_validity_file', help='API Validity Str File for Judging API Request Success or Not', type=str, default=None, required=False)
    parser.add_argument('--api_template_file', help='API Template File for Adding API', type=str, default=None, required=False)
    parser.add_argument('--no_get_producer', action="store_true", help='Get Method Can not be Producer, Default: False')
    parser.add_argument('--open_isrequired', action="store_true", help='Whether Open Param isRequired Option or not, Default: False')
    parser.add_argument('--need_trigger', action="store_true", help='Whether Need Trigger API to Trigger Vul, Default: False')
    #parser.add_argument('--no_vul_oriented', action="store_true", help='No Need for a Vulnerability-oriented Mechanism., Default: False')
    args = parser.parse_args()
    #start_log_str = "----------------VoAPI Start: " + time.asctime() + "-----------------------\n"
    start_log_str = "----------------VoAPI Start" + "-----------------------\n"
    adapt_api_vul_payloads(args.verification_server_ip, args.verification_server_port, args.verification_server_port_for_https, args.upload_payloads_dir)
    if args.output == "./":
        output_dir = os.path.abspath('.')
    else:
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        output_dir = args.output
    if not output_dir.endswith("/"):
        output_dir = output_dir + "/"
    #subdirs = ["unfinished_seq", "vul", "undetected_suspicious"]
    subdirs = ["unfinished_seq", "vul"]
    for subdir in subdirs:
        temp_dir = output_dir + subdir + "/"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
    log_file = output_dir + "test_log.txt"
    if os.path.exists(log_file):
        os.remove(log_file)
    write_log(log_file, start_log_str)
    if args.openapi:
        upload_apis = solve_multipart(args.openapi)
        # if upload_apis:
        #     record_hand_test_apis(output_dir, upload_apis)             
    baseurl = args.baseurl
    header_dict = {"Content-Type" : args.api_content_type}
    if args.api_header_file:
        fd = open(args.api_header_file, "r", encoding="utf-8")
        header_dict.update(json.loads(fd.read().strip()))
        fd.close()
    if args.api_param_file:
        fd = open(args.api_param_file, "r", encoding="utf-8")
        param_dict = json.loads(fd.read().strip())
        fd.close()
    else:
        param_dict = None
    if args.api_validity_file:
        fd = open(args.api_validity_file, "r", encoding="utf-8")
        api_validity_json = json.loads(fd.read().strip())
        fd.close()
    else:
        api_validity_json = None
    if args.api_template_file:
        fd = open(args.api_template_file, "r", encoding="utf-8")
        add_api_templates_json = json.loads(fd.read().strip())
        fd.close()
        add_api_templates_list, add_candidate_api_list = solve_add_api_templates_json(add_api_templates_json)
    else:
        add_api_templates_list = None
        add_candidate_api_list = None
    api_template_list = parse_restler_compile(args.restler_compile)
    # for api_template in api_template_list:
    #     if api_template.api_url == "/v3/projects" and api_template.api_method.lower() == "post":
    #         json_str = json.dumps(api_template.api_response, indent=4)
    #         f = open("a.txt","w")
    #         f.write(json_str)
    #         f.close()
    #         exit(0)
    if add_api_templates_list:
        for add_api_template in add_api_templates_list:
            for api_template in api_template_list:
                if (api_template.api_url == add_api_template.api_url) and (api_template.api_method.lower() == add_api_template.api_method.lower()):
                    api_template_list.remove(api_template)
        api_template_list += add_api_templates_list
    # if args.no_vul_oriented:
    #     candidate_api_list = no_vul_oriented_api_format(api_template_list)
    # else:
    candidate_api_list = candidate_api_extraction(api_template_list)
    upload_candidate_api_list = []
    if upload_apis:
        for upload_api in upload_apis:
            for api_template in api_template_list:
                if (api_template.api_url == upload_api["api_url"]) and (api_template.api_method.lower() == upload_api["api_method"].lower()):
                    api_template.api_request["body"] = {upload_api["multipart_param"]: ["String", [], ["MultiPartValue"], True]}
                    api_template.api_request_value["body"] = {upload_api["multipart_param"]: ["MultiPartValue", "VoAPI_SPECIFICATION"]}
                    upload_candidate_api_list.append([api_template, {"upload_api": [upload_api["multipart_param"]]}])
                    break
    if upload_candidate_api_list:
        candidate_api_list += upload_candidate_api_list
    if add_candidate_api_list:
        for add_candidate_api in add_candidate_api_list:
            for candidate_api in candidate_api_list:
                if (candidate_api[0].api_url == add_candidate_api[0].api_url) and (candidate_api[0].api_method.lower() == add_candidate_api[0].api_method.lower()):
                    candidate_api_list.remove(candidate_api)
        candidate_api_list = add_candidate_api_list + candidate_api_list
    candidate_apis_test(baseurl, header_dict, param_dict, output_dir, api_template_list, candidate_api_list, api_validity_json, args.no_get_producer, args.open_isrequired, args.need_trigger, log_file)
    #end_log_str = "----------------VoAPI End: " + time.asctime() + "-----------------------\n"
    end_log_str = "----------------VoAPI End" + "-----------------------\n"
    write_log(log_file, end_log_str)

if __name__ == "__main__":
    main()