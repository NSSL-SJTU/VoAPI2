import os, re, sys, copy, time, json, random, requests, functools
import VoAPITemplate
from VoAPIGlobalData import *
from json_ref_dict import materialize, RefDict

def resolve_multipart_api(multipart_json):
    multipart_param = ""
    # only support signal file upload and other param string type
    for param_name in multipart_json.keys():
        if "format" in multipart_json[param_name].keys():
            if multipart_json[param_name]["format"].lower() == "binary":
                # file param
                multipart_param = param_name
                break
        elif "description" in multipart_json[param_name].keys():
            if " file" in multipart_json[param_name]["description"].lower():
                # file param
                multipart_param = param_name
                break
        else:
            pass
    return multipart_param

def resolve_signal_api_info(api_method, signal_api_info):
    if api_method.lower() not in ["post", "put", "patch"]:
        return False
    if "requestBody" in signal_api_info.keys():
        api_request_body = materialize(signal_api_info["requestBody"])
        if "content" in api_request_body.keys():
            api_request_body_content = api_request_body["content"]
            if "multipart/form-data" in api_request_body_content.keys():
                return resolve_multipart_api(api_request_body_content["multipart/form-data"]["schema"]["properties"])    
    return False 

def solve_multipart(openapi):
    f = open(openapi, "r", encoding="utf-8")
    content = f.read()
    f.close()
    upload_apis = []
    if "multipart/form-data" in content.lower():
        try:
            api_json = RefDict(openapi)
        except:
            print(openapi + " validating...")
            f = open(openapi, "r", encoding="utf-8")
            openapi_content = f.read()
            f.close()
            res = ""
            for x in openapi_content:
                if ord(x) not in range(0,128):
                    continue
                res += x
            f = open(openapi, "w")
            f.write(res)
            f.close()
            api_json = RefDict(openapi)
        if "paths" in api_json.keys():
            for api_url in api_json["paths"].keys():
                api_info = api_json["paths"][api_url]
                if not isinstance(api_info, RefDict):
                    continue
                api_methods = list(api_info.keys()) 
                for api_method in api_methods:
                    multipart_param = resolve_signal_api_info(api_method, api_info[api_method])
                    if multipart_param:
                        path_flag = False
                        param_flag = False
                        for api_path_keyword in ApiPathKeywords["upload_api"]:
                            if api_path_keyword in api_url.lower():
                                path_flag = True
                                break
                        for api_param_keyword in ApiParamKeywords["upload_api"]:
                            if api_param_keyword in multipart_param.lower():
                                param_flag = True
                                break
                        if (path_flag and (not param_flag)) or (param_flag):
                            upload_apis.append({"api_url": api_url, "api_method": api_method, "multipart_param": multipart_param})
        elif "webhooks" in api_json.keys():
            for api_url in api_json["webhooks"].keys():
                api_info = api_json["webhooks"][api_url]
                if not isinstance(api_info, RefDict):
                    continue
                api_methods = list(api_info.keys()) 
                for api_method in api_methods:
                    multipart_param = resolve_signal_api_info(api_method, api_info[api_method])
                    if multipart_param:
                        path_flag = False
                        param_flag = False
                        for api_path_keyword in ApiPathKeywords["upload_api"]:
                            if api_path_keyword in api_url.lower():
                                path_flag = True
                                break
                        for api_param_keyword in ApiParamKeywords["upload_api"]:
                            if api_param_keyword in multipart_param.lower():
                                param_flag = True
                                break
                        if (path_flag and (not param_flag)) or (param_flag):
                            upload_apis.append({"api_url": api_url, "api_method": api_method, "multipart_param": multipart_param})
        else:
            print("Not Support OpenAPI Spec:", api_json.keys())
    return upload_apis    
    
def adapt_api_vul_payloads(verification_server_ip, verification_server_port, verification_server_port_for_https, upload_dir):
    global ApiVulnerabilityPayloads
    for api_func in ApiVulnerabilityPayloads:
        if api_func in ["proxy_api", "command_api", "display_api"]:
            for i in range(len(ApiVulnerabilityPayloads[api_func])):
                if "http://" in ApiVulnerabilityPayloads[api_func][i]:
                    ApiVulnerabilityPayloads[api_func][i] = ApiVulnerabilityPayloads[api_func][i].replace("IP:PORT", verification_server_ip + ":" + str(verification_server_port))
                elif "https://" in ApiVulnerabilityPayloads[api_func][i]:
                    ApiVulnerabilityPayloads[api_func][i] = ApiVulnerabilityPayloads[api_func][i].replace("IP:PORT", verification_server_ip + ":" + str(verification_server_port_for_https))
                else:
                    pass    
    if upload_dir:
        for upload_file in os.listdir(upload_dir):
            if os.path.isfile(os.path.join(upload_dir, upload_file)):
                ApiVulnerabilityPayloads["upload_api"].append([upload_file, os.path.join(upload_dir, upload_file)])
    return

def naming_convention_split(param):
    output_list = []
    campel_case_pattern = r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)'
    output_list.append(re.findall(campel_case_pattern, param)[-1].lower())
    output_list.append(param.split("-")[-1].lower())
    output_list.append(param.split("_")[-1].lower())
    return list(set(output_list))

def symspell_corrector(param):
    output_list = []
    # look up suggestions for multi-word input strings 
    suggestions = sym_spell.lookup_compound( 
        phrase=param,  
        max_edit_distance=2,  
        transfer_casing=True,  
        ignore_term_with_digits=True, 
        ignore_non_words=True, 
        split_by_space=True 
    ) 
    # display the correction
    for suggestion in suggestions: 
        output_list.append(suggestion.term.split(" ")[-1].lower())
    return list(set(output_list))

def extend_consumers(consumers):
    for consumer in consumers:
        consumer_split_list = []
        # NamingConvention Split
        consumer_split_list += naming_convention_split(consumer)
        # SpellCorrect Split
        consumer_split_list += symspell_corrector(consumer)
        consumer_split_list = list(set(consumer_split_list))
        if consumer in consumer_split_list:
            consumer_split_list.remove(consumer)
        consumers[consumer] = [consumers[consumer], consumer_split_list]
    return consumers

def find_consumer_the_only_producer(consumer_name, consumer_type, candidate_api_producer_pool):
    consumer_producer_apis = []
    the_only_producer = None
    if consumer_type not in RandomValueDict.keys():
        return False
    accurate_pattern_str = "^[^A-Za-z0-9]*" + consumer_name + "(?!.)"
    accurate_producer_pattern = re.compile(accurate_pattern_str, re.IGNORECASE)
    for candidate_api_producer in candidate_api_producer_pool:
        producer_flag = False
        producer_dict = get_consumers_or_producers(candidate_api_producer.api_response)
        for producer_name in producer_dict:
            producer_type = producer_dict[producer_name]
            if (re.match(accurate_producer_pattern, producer_name)) and (producer_type == consumer_type):
                producer_flag = True
                temp_producer_apis = consumer_producer_apis[:]
                for temp_producer_api in temp_producer_apis:
                    if candidate_api_producer.api_url == temp_producer_api[0].api_url:
                        if ProducerMethodPriority[candidate_api_producer.api_method.upper()] < ProducerMethodPriority[temp_producer_api[0].api_method.upper()]:
                            producer_flag = False
                        else:
                            consumer_producer_apis.remove(temp_producer_api)
                if producer_flag:
                    if (candidate_api_producer,  producer_name) not in consumer_producer_apis:
                        consumer_producer_apis.append((candidate_api_producer,  producer_name))
    if consumer_producer_apis:
        if len(consumer_producer_apis) >= 2:
            the_only_producer = consumer_producer_apis[0]
            # find api_url max length, no same length, because same length only keep the highest ProducerMethodPriority
            for consumer_producer_api in consumer_producer_apis[1:]:
                if len(consumer_producer_api[0].api_url) > len(the_only_producer[0].api_url):
                    the_only_producer = consumer_producer_api
        else:
            the_only_producer = consumer_producer_apis[0]
    return the_only_producer


def find_producers(candidate_api, candidate_api_producer_pool):
    producer_apis = []
    producer_consumer_relations = []
    if not candidate_api_producer_pool:
        return producer_apis, producer_consumer_relations
    extend_consumer_dict = extend_consumers(get_consumers_or_producers(candidate_api.api_request))
    for consumer in extend_consumer_dict:
        consumer_type = extend_consumer_dict[consumer][0]
        the_only_producer = find_consumer_the_only_producer(consumer, consumer_type, candidate_api_producer_pool)
        if the_only_producer:
            producer_apis.append(the_only_producer[0])
            producer_consumer_relations.append({'consumer_api': candidate_api, 'consumer_param': consumer, 'producer_api': the_only_producer[0], 'producer_param': the_only_producer[1]})
            continue
        # accurate match > extend match
        signal_producer_apis = []
        extend_consumer_list = extend_consumer_dict[consumer][1]
        for extend_consumer in extend_consumer_list:
            # only matches strings which start with extend_consumer and may be preceded by any number of special characters, and must end at the string boundary
            the_only_producer = find_consumer_the_only_producer(extend_consumer, consumer_type, candidate_api_producer_pool)
            if the_only_producer:
                signal_producer_apis.append(the_only_producer)
        if signal_producer_apis:
            if len(signal_producer_apis) >= 2:
                the_signal_producer = signal_producer_apis[0]
                # find api_url max length, no same length, because same length only keep the highest ProducerMethodPriority
                for signal_producer_api in signal_producer_apis[1:]:
                    if len(signal_producer_api[0].api_url) > len(the_signal_producer[0].api_url):
                        the_signal_producer = signal_producer_api
            else:
                the_signal_producer = signal_producer_apis[0]
            producer_apis.append(the_signal_producer[0])
            producer_consumer_relations.append({'consumer_api': candidate_api, 'consumer_param': consumer, 'producer_api': the_signal_producer[0], 'producer_param': the_signal_producer[1]})    
    return list(set(producer_apis)), producer_consumer_relations

def is_valid_producer(candidate_api, candidate_api_producer, no_get_producer):
    # CRUD semantics
    if no_get_producer:
        producer_methods = ProducerMethodsNoGet
    else:
        producer_methods = ProducerMethods
    if candidate_api_producer.api_method.upper() not in producer_methods:
        return False
    # resource hierarchy
    candidate_api_resource = [i.lower() for i in filter(None, candidate_api.api_url.split("/"))]
    candidate_api_producer_resource = [i.lower() for i in filter(None, candidate_api_producer.api_url.split("/"))]
    for resource in candidate_api_producer_resource:
        if resource not in candidate_api_resource:
            return False
    # same api_url, low priority method should not be producer
    if (candidate_api.api_url == candidate_api_producer.api_url) and (ProducerMethodPriority[candidate_api.api_method.upper()] > ProducerMethodPriority[candidate_api_producer.api_method.upper()]):
        return False
    return True
    
def vaild_producer(candidate_api_seq, current_api_index, candidate_api_producer_pool, no_get_producer):
    current_api = candidate_api_seq[current_api_index]
    vaild_producer_pool = []
    # only strip current_api and candidate_api, because current_api may have same producer in candidate_api_seq
    current_api_producer_pool = list(set(candidate_api_producer_pool)-set([candidate_api_seq[-1], current_api]))
    for candidate_api_producer in current_api_producer_pool:
        if is_valid_producer(current_api, candidate_api_producer, no_get_producer):
            vaild_producer_pool.append(candidate_api_producer)
    return vaild_producer_pool

def api_compare(api1, api2):
    if (api1.api_url == api2.api_url) and (api1.api_method == api2.api_method):
        return 0
    else:
        if (api1.api_url == api2.api_url):
            if (ProducerMethodPriority[api1.api_method.upper()] > ProducerMethodPriority[api2.api_method.upper()]):
                return 1
            else:
                return -1
        else:
            if len(api1.api_url) == len(api2.api_url):
                return 0
            elif len(api1.api_url) > len(api2.api_url):
                return 1
            else:
                return -1

def reverse_sequence_construction(candidate_api, candidate_api_producer_pool, no_get_producer):
    candidate_api_seq = [candidate_api]
    candidate_api_seq_relations = []
    i = -1
    while True:
        valid_producer_pool = vaild_producer(candidate_api_seq, i, candidate_api_producer_pool, no_get_producer)
        producer_apis, producer_consumer_relations = find_producers(candidate_api_seq[i], valid_producer_pool)
        candidate_api_seq_relations += producer_consumer_relations
        # for producer_api in producer_apis:
        #     candidate_api_seq.insert(0, producer_api)
        no_sorted_api_seq = candidate_api_seq[:-1]
        for producer_api in producer_apis:
            if producer_api not in no_sorted_api_seq:
                no_sorted_api_seq.append(producer_api)
        sorted_api_seq = sorted(no_sorted_api_seq, key=functools.cmp_to_key(api_compare))
        candidate_api_seq = sorted_api_seq + [candidate_api]
        if candidate_api_seq[i] == candidate_api_seq[0]:
            break
        else:
            i = i - 1
    return candidate_api_seq, candidate_api_seq_relations

def format_request(request_value_struct, api_request_struct, open_isrequired=False):
    def remove_voapi_not_required(api_request_part_dict):
        if isinstance(api_request_part_dict, dict):
            for key, value in list(api_request_part_dict.items()):
                if value == 'VoAPI_NotRequired':
                    del api_request_part_dict[key]
                else:
                    remove_voapi_not_required(value)
        elif isinstance(api_request_part_dict, list):
            for item in api_request_part_dict:
                remove_voapi_not_required(item)

    def traverse_and_format(param_dict, request_dict, param_name, api_request_part_dict, open_isrequired):
        param_struct = param_dict[param_name]
        request_struct = request_dict[param_name]
        if param_struct[0] == "Array":
            api_request_part_dict[param_name] = []
            for array_param_index in range(1, len(param_struct)):
                if type(param_struct[array_param_index]) == dict:
                    api_request_part_dict[param_name].append(param_struct[array_param_index])
                    for array_param_name in param_struct[array_param_index]:
                        traverse_and_format(param_struct[array_param_index], request_struct[array_param_index], array_param_name, api_request_part_dict[param_name][-1], open_isrequired)
                elif type(param_struct[array_param_index]) == list:
                    if param_struct[array_param_index][1] == "VoAPI_RANDOM":
                        param_type = request_struct[array_param_index][0]
                        api_request_part_dict[param_name].append(RandomValueDict[param_type][random.randint(0,43)])
                    else:
                        api_request_part_dict[param_name].append(param_struct[array_param_index][0])
                elif type(param_struct[array_param_index]) == bool:
                    # ignore is_required
                    continue
                else:
                    print("Not Supported Struct in format_request: ", param_struct[array_param_index])
        elif param_struct[0] == "Property":
            api_request_part_dict[param_name] = param_struct[1]
            for property_param_name in param_struct[1]:
                traverse_and_format(param_struct[1], request_struct[1], property_param_name, api_request_part_dict[param_name], open_isrequired)
        else:
            param_is_required_priority = ["VoAPI_TEST", "VoAPI_CONSUMER", "VoAPI_PRODUCER", "VoAPI_CUSTOM"]
            if param_struct[1] in param_is_required_priority:
                api_request_part_dict[param_name] = param_struct[0]
                return 
            if open_isrequired:
                is_required = request_struct[3]
                if not is_required:
                    api_request_part_dict[param_name] = "VoAPI_NotRequired"
                    return
            if param_struct[1] == "VoAPI_FORMAT":
                for format_str in ApiParamFormat:
                    if format_str in param_name:
                        api_request_part_dict[param_name] = ApiParamFormat[format_str][random.randint(0,43)]
            elif param_struct[1] == "VoAPI_RANDOM":
                param_type = request_struct[0]
                api_request_part_dict[param_name] = RandomValueDict[param_type][random.randint(0,43)]
            else:
                api_request_part_dict[param_name] = param_struct[0]

    api_path_dict = {}
    api_header_dict = {}
    api_query_dict = {}
    api_body_dict = {}
    if request_value_struct["path"]:
        api_path_dict = copy.deepcopy(request_value_struct["path"])
        for param_name in request_value_struct["path"]:
            traverse_and_format(request_value_struct["path"], api_request_struct["path"], param_name, api_path_dict, open_isrequired)
    #print("api_path_dict: ", api_path_dict)
    if request_value_struct["header"]:
        api_header_dict = copy.deepcopy(request_value_struct["header"])
        for param_name in request_value_struct["header"]:
            traverse_and_format(request_value_struct["header"], api_request_struct["header"], param_name, api_header_dict, open_isrequired)
    #print("api_header_dict: ", api_header_dict)
    if request_value_struct["query"]:
        api_query_dict = copy.deepcopy(request_value_struct["query"])
        for param_name in request_value_struct["query"]:
            traverse_and_format(request_value_struct["query"], api_request_struct["query"], param_name, api_query_dict, open_isrequired)
    #print("api_query_dict: ", api_query_dict)
    if request_value_struct["body"]:
        api_body_dict = copy.deepcopy(request_value_struct["body"])
        for param_name in request_value_struct["body"]:
            #Ignore meaningless first parameter name -> body in OpenAPI body parameters
            if (param_name == "body") and (len(list(request_value_struct["body"].keys()))) == 1 and (type(request_value_struct["body"][param_name]) == list):
                api_body_dict = []
                param_struct = request_value_struct["body"][param_name]
                request_struct = api_request_struct["body"][param_name]
                for array_param_index in range(1, len(param_struct)):
                    if type(param_struct[array_param_index]) == dict:
                        api_body_dict.append(param_struct[array_param_index])
                        for array_param_name in param_struct[array_param_index]:
                            traverse_and_format(param_struct[array_param_index], request_struct[array_param_index], array_param_name, api_body_dict[-1], open_isrequired)
                    elif type(param_struct[array_param_index]) == list:
                        if param_struct[array_param_index][1] == "VoAPI_RANDOM":
                            param_type = request_struct[array_param_index][0]
                            api_body_dict.append(RandomValueDict[param_type][random.randint(0,43)])
                        else:
                            api_body_dict.append(param_struct[array_param_index][0])
                    elif type(param_struct[array_param_index]) == bool:
                        # ignore is_required
                        continue
                    else:
                        print("Not Supported Struct in format_request: ", param_struct[array_param_index])
            else:
                traverse_and_format(request_value_struct["body"], api_request_struct["body"], param_name, api_body_dict, open_isrequired)
    if open_isrequired:
        remove_voapi_not_required(api_path_dict)
        remove_voapi_not_required(api_header_dict)
        remove_voapi_not_required(api_query_dict)
        remove_voapi_not_required(api_body_dict)
    return api_path_dict, api_header_dict, api_query_dict, api_body_dict

def update_api_request_param_value_by_custom_param_dict(request_value_struct, custom_param_dict):
    for request_part in request_value_struct:
        if request_value_struct[request_part]:
            for param_name in request_value_struct[request_part]:
                custom_flag = False
                for custom_param in custom_param_dict:
                    if param_name == custom_param:
                        if (request_value_struct[request_part][param_name][0] == "Array") or (request_value_struct[request_part][param_name][0] == "Property"):
                            request_value_struct[request_part][param_name] = [custom_param_dict[custom_param], "VoAPI_CUSTOM"]
                        else:
                            if ParamValuePriority[request_value_struct[request_part][param_name][1]] <= ParamValuePriority["VoAPI_CUSTOM"]:
                                request_value_struct[request_part][param_name] = [custom_param_dict[custom_param], "VoAPI_CUSTOM"]
                        custom_flag = True
                if custom_flag:
                    continue       
    return

def update_api_request_param_value(request_value_struct, request_param_name, request_param_value_list):
    def traverse_and_update(param_dict, param_name, request_param_name, request_param_value_list):
        request_param_value_strategy = request_param_value_list[1]
        param_struct = param_dict[param_name]
        if param_struct[0] == "Array":
            for array_param_index in range(1, len(param_struct)):
                if type(param_struct[array_param_index]) == dict:
                    for array_param_name in param_struct[array_param_index]:
                        if param_struct[array_param_index][array_param_name]:
                            if (param_struct[array_param_index][array_param_name][0] != "Array") and (param_struct[array_param_index][array_param_name][0] != "Property"):
                                if (array_param_name == request_param_name):
                                    if ParamValuePriority[param_struct[array_param_index][array_param_name][1]] <= ParamValuePriority[request_param_value_strategy]: 
                                        param_struct[array_param_index][array_param_name] = request_param_value_list
                            else:
                                traverse_and_update(param_struct[array_param_index], array_param_name, request_param_name, request_param_value_list)
                        else:
                            if (array_param_name == request_param_name):
                                param_struct[array_param_index][array_param_name] = request_param_value_list
                elif type(param_struct[array_param_index]) == list:
                    if (param_name == request_param_name):
                        if ParamValuePriority[param_struct[array_param_index][1]] <= ParamValuePriority[request_param_value_strategy]: 
                            param_struct[array_param_index] = request_param_value_list
                elif type(param_struct[array_param_index]) == bool:
                        # ignore is_required
                        continue
                else:
                    print("Not Supported Struct in update_api_request_param_value: ", param_struct[array_param_index])
        elif param_struct[0] == "Property":
            for property_param_name in param_struct[1]:
                if param_struct[1][property_param_name]:
                    if (param_struct[1][property_param_name][0] != "Array") and (param_struct[1][property_param_name][0] != "Property"):
                        if (property_param_name == request_param_name):
                            if ParamValuePriority[param_struct[1][property_param_name][1]] <= ParamValuePriority[request_param_value_strategy]: 
                                param_struct[1][property_param_name] = request_param_value_list
                    else:
                        traverse_and_update(param_struct[1], property_param_name, request_param_name, request_param_value_list)
                else:
                    if (property_param_name == request_param_name):
                        param_struct[1][property_param_name] = request_param_value_list
        else:
            print(param_struct)
            print("Error in traverse_and_update!!!")
        return
        
    #request_param_value = request_param_value_list[0]
    request_param_value_strategy = request_param_value_list[1]
    for request_part in request_value_struct:
        if request_value_struct[request_part]:
            for param_name in request_value_struct[request_part]:
                if request_value_struct[request_part][param_name]:
                    if (request_value_struct[request_part][param_name][0] != "Array") and (request_value_struct[request_part][param_name][0] != "Property"):
                        if param_name == request_param_name:
                            if ParamValuePriority[request_value_struct[request_part][param_name][1]] <= ParamValuePriority[request_param_value_strategy]: 
                                request_value_struct[request_part][param_name] = request_param_value_list
                    else:
                        traverse_and_update(request_value_struct[request_part], param_name, request_param_name, request_param_value_list)
                else:
                    if param_name == request_param_name:
                        request_value_struct[request_part][param_name] = request_param_value_list        
    return 

def request_sender(baseurl, api_url, api_method, header_dict, request_dict_list, log_file, upload_flag=False):
    if baseurl.endswith("/"):
        baseurl = baseurl[:-1]
    api_path_dict, api_header_dict, api_query_dict, api_body_dict = request_dict_list
    if header_dict:
        api_header_dict.update(header_dict)
    # format api_url
    path_params = re.findall(r'({.*?})', api_url)
    if path_params and api_path_dict:
        for path_param in path_params:
            api_url = api_url.replace(path_param, str(api_path_dict[path_param[1:-1]]))
    url = baseurl + api_url
    if upload_flag:
        request_data = api_body_dict
    else:
        if api_body_dict:
            request_data = json.dumps(api_body_dict)
        else:
            request_data = ''
    try:
        #log_str = "----------------Send: " + time.asctime() + "-----------------------\n"
        log_str = "----------------Send: " + "-----------------------\n"
        log_str += "send request: {0} {1}\n".format(api_method.lower(), url)
        log_str += "api_header_dict: " + str(api_header_dict) + "\n"
        log_str += "api_query_dict: " + str(api_query_dict) + "\n"
        log_str += "request_data: " + str(api_body_dict) + "\n"
        write_log(log_file, log_str)
        r = requests.request(method=api_method.lower(), url=url, headers=api_header_dict, params=api_query_dict, data=request_data, timeout=4)
        log_str = "response: " + r.text + "\n" + "status_code: " + str(r.status_code) + "\n"
        write_log(log_file, log_str)
    except Exception as e:
        print(e)
        r = None
    return r

def update_api_response_value_by_response_json(api_response_value, response_json, prev_param_name=None):
    if type(response_json) == list:
        for i in response_json:
            if type(i) == dict:
                update_api_response_value_by_response_json(api_response_value, i)
            else:
                update_api_response_param_value(api_response_value, prev_param_name, [response_json, "VoAPI_PRODUCER"])
                return 
    elif type(response_json) == dict:
        for param_name in response_json:
            if type(response_json[param_name]) == list:
                update_api_response_value_by_response_json(api_response_value, response_json[param_name], param_name)
            elif type(response_json[param_name]) == dict:
                update_api_response_value_by_response_json(api_response_value, response_json[param_name])
            else:
                update_api_response_param_value(api_response_value, param_name, [response_json[param_name], "VoAPI_PRODUCER"])
    else:
        print("Not Supported Struct in update_api_response_value_by_response_json: ", response_json)
    
def update_api_response_param_value(api_response_value, response_param_name, response_param_value_list):
    def traverse_and_update(param_dict, param_name, response_param_name, response_param_value_list):
        param_struct = param_dict[param_name]
        if param_struct[0] == "Array":
            for array_param_index in range(1, len(param_struct)):
                if type(param_struct[array_param_index]) == dict:
                    for array_param_name in param_struct[array_param_index]:
                        if param_struct[array_param_index][array_param_name]:
                            if (param_struct[array_param_index][array_param_name][0] != "Array") and (param_struct[array_param_index][array_param_name][0] != "Property"):
                                if (array_param_name == response_param_name):
                                    # same name var only update by first response var
                                    if param_struct[array_param_index][array_param_name][1] != response_param_value_list[1]:
                                        param_struct[array_param_index][array_param_name] = response_param_value_list
                            else:
                                traverse_and_update(param_struct[array_param_index], array_param_name, response_param_name, response_param_value_list)
                        else:
                            if (array_param_name == response_param_name):
                                param_struct[array_param_index][array_param_name] = response_param_value_list
                elif type(param_struct[array_param_index]) == list:
                    if (param_name == response_param_name):
                        param_struct[array_param_index] = response_param_value_list
                elif type(param_struct[array_param_index]) == bool:
                        # ignore is_required
                        continue
                else:
                    print("Not Supported Struct in update_api_response_param_value: ", param_struct[array_param_index])
        elif param_struct[0] == "Property":
            for property_param_name in param_struct[1]:
                if param_struct[1][property_param_name]:
                    if (param_struct[1][property_param_name][0] != "Array") and (param_struct[1][property_param_name][0] != "Property"):
                        if (property_param_name == response_param_name):
                            param_struct[1][property_param_name] = response_param_value_list
                    else:
                        traverse_and_update(param_struct[1], property_param_name, response_param_name, response_param_value_list)
                else:
                    if (property_param_name == response_param_name):
                        param_struct[1][property_param_name] = response_param_value_list
        else:
            print(param_struct)
            print("Error in traverse_and_update!!!")
        return
        
    # response_param_value only [], ["1", "VoAPI_SPECIFICATION"], ["1", "VoAPI_PRODUCER"]
    # just update, don't consider priority
    for api_response_part in api_response_value:
        if api_response_value[api_response_part]:
            for param_name in api_response_value[api_response_part]:
                if api_response_value[api_response_part][param_name]:
                    if (api_response_value[api_response_part][param_name][0] != "Array") and (api_response_value[api_response_part][param_name][0] != "Property"):
                        if (param_name == response_param_name):
                            # same name var only update by first response var
                            if api_response_value[api_response_part][param_name][1] != response_param_value_list[1]:
                                api_response_value[api_response_part][param_name] = response_param_value_list
                    else:
                        traverse_and_update(api_response_value[api_response_part], param_name, response_param_name, response_param_value_list)
                else:
                    if (param_name == response_param_name):
                        api_response_value[api_response_part][param_name] = response_param_value_list
    return 

def get_api_response_param_value(api_response_value, response_param_name):
    def traverse_and_get(param_dict, param_name, response_param_name):
        response_param_value = ""
        param_struct = param_dict[param_name]
        if param_struct:
            if param_struct[0] == "Array":
                for array_param_index in range(1, len(param_struct)):
                    if type(param_struct[array_param_index]) == dict:
                        for array_param_name in param_struct[array_param_index]:
                            if param_struct[array_param_index][array_param_name]:
                                if (param_struct[array_param_index][array_param_name][0] != "Array") and (param_struct[array_param_index][array_param_name][0] != "Property"):
                                    if (array_param_name == response_param_name):
                                        response_param_value = param_struct[array_param_index][array_param_name][0]
                                        return response_param_value
                                else:
                                    response_param_value = traverse_and_get(param_struct[array_param_index], array_param_name, response_param_name)
                    elif type(param_struct[array_param_index]) == list:
                        if (param_name == response_param_name):
                            print("Should Not Appear in get_api_response_param_value!!!")
                            response_param_value = param_struct[array_param_index][0]
                            return response_param_value
                    elif type(param_struct[array_param_index]) == bool:
                            # ignore is_required
                            continue
                    else:
                        print("Not Supported Struct in get_api_response_param_value: ", param_struct[array_param_index])
            elif param_struct[0] == "Property":
                for property_param_name in param_struct[1]:
                    if param_struct[1][property_param_name]:
                        if (param_struct[1][property_param_name][0] != "Array") and (param_struct[1][property_param_name][0] != "Property"):
                            if property_param_name == response_param_name:
                                response_param_value = param_struct[1][property_param_name][0]
                                return response_param_value
                        else:
                            response_param_value = traverse_and_get(param_struct[1], property_param_name, response_param_name)
            else:
                print(param_struct)
                print("Error in traverse_and_get!!!")
        else:
            if param_name == response_param_name:
                return response_param_value
    response_param_value = ""
    for api_response_part in api_response_value:
        if api_response_value[api_response_part]:
            for param_name in api_response_value[api_response_part]:
                if (api_response_value[api_response_part][param_name]):
                    if (api_response_value[api_response_part][param_name][0] != "Array") and (api_response_value[api_response_part][param_name][0] != "Property"):
                        if (param_name == response_param_name) and (api_response_value[api_response_part][param_name]):
                            response_param_value = api_response_value[api_response_part][param_name][0]
                            return response_param_value
                    else:
                        response_param_value = traverse_and_get(api_response_value[api_response_part], param_name, response_param_name)
    return response_param_value

def get_request_params(api_request):
    def parse_param_struct(param_struct):
        request_params = []
        if param_struct[0] == "Array":
            for array_param_index in range(1, len(param_struct)):
                temp_params = []
                if type(param_struct[array_param_index]) == dict:
                    for param_name in param_struct[array_param_index]:
                        if (param_struct[array_param_index][param_name][0] != "Array") and (param_struct[array_param_index][param_name][0] != "Property"):
                            request_params.append(param_name)
                        else:
                            temp_params = parse_param_struct(param_struct[array_param_index][param_name])
                        request_params += temp_params   
        elif param_struct[0] == "Property":
            for param_name in param_struct[1]:
                temp_params = []
                if (param_struct[1][param_name][0] != "Array") and (param_struct[1][param_name][0] != "Property"):
                    request_params.append(param_name)
                else:
                    temp_params = parse_param_struct(param_struct[1][param_name])
                request_params += temp_params
        else:
            pass
        return request_params
    # get header/query/body param name
    request_params = []
    for api_request_part in ["header", "query", "body"]:
        if api_request[api_request_part]:
            for param_name in api_request[api_request_part]:
                temp_params = []
                if (api_request[api_request_part][param_name][0] != "Array") and (api_request[api_request_part][param_name][0] != "Property"):
                    request_params.append(param_name)
                else:
                    temp_params = parse_param_struct(api_request[api_request_part][param_name])
                request_params += temp_params    
    return request_params

def get_consumers_or_producers(api_request_or_api_response):
    def parse_param_struct(param_struct):
        consumer_or_producer_dict = {}
        if param_struct[0] == "Array":
            for array_param_index in range(1, len(param_struct)):
                if type(param_struct[array_param_index]) == dict:
                    for param_name in param_struct[array_param_index]:
                        if (param_struct[array_param_index][param_name][0] != "Array") and (param_struct[array_param_index][param_name][0] != "Property"):
                            consumer_or_producer_dict[param_name] = param_struct[array_param_index][param_name][0]
                        else:
                            consumer_or_producer_dict.update(parse_param_struct(param_struct[array_param_index][param_name]))
        elif param_struct[0] == "Property":
            for param_name in param_struct[1]:
                if (param_struct[1][param_name][0] != "Array") and (param_struct[1][param_name][0] != "Property"):
                    consumer_or_producer_dict[param_name] = param_struct[1][param_name][0]
                else:
                    consumer_or_producer_dict.update(parse_param_struct(param_struct[1][param_name]))
        else:
            pass
        return consumer_or_producer_dict
    
    # get path/header/query/body param name
    consumers_or_producers = {}
    for api_request_or_response_part in api_request_or_api_response:
        if api_request_or_api_response[api_request_or_response_part]:
            for param_name in api_request_or_api_response[api_request_or_response_part]:
                if (api_request_or_api_response[api_request_or_response_part][param_name][0] != "Array") and (api_request_or_api_response[api_request_or_response_part][param_name][0] != "Property"):
                    consumers_or_producers[param_name] = api_request_or_api_response[api_request_or_response_part][param_name][0]
                else:
                    consumers_or_producers.update(parse_param_struct(api_request_or_api_response[api_request_or_response_part][param_name]))
    return consumers_or_producers

def solve_add_api_templates_json(add_api_templates_json):
    add_api_templates_list = []
    add_candidate_api_list = []
    for add_api_template_dict in add_api_templates_json:
        if (len(list(add_api_template_dict["api_request"]["body"].keys())) == 1) and (add_api_template_dict["api_request"]["body"][list(add_api_template_dict["api_request"]["body"].keys())[0]][0] == "MultipartParam"):
            # upload_api
            multipart_param = list(add_api_template_dict["api_request"]["body"].keys())[0]
            path_flag = False
            param_flag = False
            for api_path_keyword in ApiPathKeywords["upload_api"]:
                if api_path_keyword in add_api_template_dict["api_url"].lower():
                    path_flag = True
                    break
            for api_param_keyword in ApiParamKeywords["upload_api"]:
                if api_param_keyword in multipart_param.lower():
                    param_flag = True
                    break
            if (path_flag and (not param_flag)) or (param_flag):
                add_api_template_dict["api_request"]["body"][multipart_param] = ["String", [], ["MultiPartValue"], True]
                add_api_template = VoAPITemplate.ApiTemplate(add_api_template_dict["api_url"], add_api_template_dict["api_method"], add_api_template_dict["api_request"], add_api_template_dict["api_response"])
                add_api_templates_list.append(add_api_template)
                add_candidate_api_list.append([add_api_template, {"upload_api": [multipart_param]}])
        else:
            # other_api
            add_api_template = VoAPITemplate.ApiTemplate(add_api_template_dict["api_url"], add_api_template_dict["api_method"], add_api_template_dict["api_request"], add_api_template_dict["api_response"])
            add_api_templates_list.append(add_api_template)
            add_candidate_api = candidate_api_extraction([add_api_template])
            if add_candidate_api:
                add_candidate_api_list.append(add_candidate_api[0])
    return add_api_templates_list, add_candidate_api_list

def no_vul_oriented_api_format(api_template_list):
    no_vul_oriented_api_list = []
    for api_template in api_template_list:
        tag_params = []
        request_dict = copy.deepcopy(api_template.api_request)
        del request_dict["path"]
        request_params = get_consumers_or_producers(request_dict)
        for request_param in request_params:
            if request_params[request_param] == "String":
                tag_params.append(request_param)
        if tag_params:
            test_types = {}
            for api_type in ApiFuncList:
                test_types[api_type] = tag_params
            no_vul_oriented_api_list.append([api_template, test_types])
    return no_vul_oriented_api_list

def candidate_api_extraction(api_template_list):
    candidate_api_list = []
    for api_template in api_template_list:
        test_types = {}
        #request_params = get_request_params(api_template.api_request)
        request_dict = copy.deepcopy(api_template.api_request)
        del request_dict["path"]
        request_params = get_consumers_or_producers(request_dict)
        for api_type in ApiFuncList:
            if api_type == "upload_api":
                # ignore here. 
                # when solve "multipart/form-data", solve upload_api.
                continue
            path_flag = False
            param_flag = False
            tag_params = []
            for api_path_keyword in ApiPathKeywords[api_type]:
                if api_path_keyword in api_template.api_url.lower():
                    path_flag = True
                    break
            for request_param in request_params:
                for api_param_keyword in ApiParamKeywords[api_type]:
                    if (api_param_keyword in request_param.lower()) and (request_params[request_param] == "String"):
                        if request_param not in tag_params:
                            tag_params.append(request_param)
                        param_flag = True
                        break
            if path_flag and (not param_flag):
                test_types[api_type] = []
                for request_param in request_params:
                    if request_params[request_param] == "String":
                        test_types[api_type].append(request_param)
            if param_flag:
                test_types[api_type] = tag_params
        temp_dict = copy.deepcopy(test_types)
        for test_type in temp_dict:
            if not temp_dict[test_type]:
                del test_types[test_type]
        if test_types:
            #print(api_template.api_url, api_template.api_method, test_types)
            candidate_api_list.append([api_template, test_types])
    return candidate_api_list

def find_triggers(candidate_api, api_templates):
    triggers = []
    the_trigger_url = None
    if candidate_api.api_url in list(MicrocksTrigger.keys()):
        the_trigger_url = MicrocksTrigger[candidate_api.api_url]
    for api_template in api_templates:
        if the_trigger_url:
            if api_template.api_url == the_trigger_url:
                return [api_template]
        else:
            if api_template.api_method.lower() == "get":
                # if (api_template.api_url == candidate_api.api_url) and (api_template.api_method != candidate_api.api_method):
                #     triggers.append(api_template)
                if ("{" not in api_template.api_url) and (not get_request_params(api_template.api_request)):
                    triggers.append(api_template)
    return triggers

def parameter_values_generation(api_template, candidate_api_seq_relations):
    # CONSUMER
    for candidate_api_seq_relation in candidate_api_seq_relations:
        consumer_api = candidate_api_seq_relation["consumer_api"]
        consumer_param = candidate_api_seq_relation["consumer_param"]
        producer_api = candidate_api_seq_relation["producer_api"]
        producer_param = candidate_api_seq_relation["producer_param"]
        if consumer_api == api_template:
            consumer_param_value = get_api_response_param_value(producer_api.api_response_value, producer_param)
            if consumer_param_value:
                update_api_request_param_value(api_template.api_request_value, consumer_param, [consumer_param_value, "VoAPI_CONSUMER"])
    # ToDo: to support SUCCESS
    return

def api_seq_show(api_seq):
    show_str = ""
    for api_index in range(len(api_seq)-1):
        show_str += api_seq[api_index].api_method + " " + api_seq[api_index].api_url + "  -->  "
    show_str += api_seq[-1].api_method + " " + api_seq[-1].api_url
    return show_str

def record_hand_test_apis(output_dir, upload_apis):
    hand_test_file = output_dir + "hand_test_apis"
    hand_test_content = ""
    for upload_api in upload_apis:
        hand_test_content += "-------- VoAPI Hand Test API --------\n"
        hand_test_content += "API Type: Upload API\n"
        hand_test_content += "API Url: " + upload_api["api_url"] + "\n"
        hand_test_content += "API Method: " + upload_api["api_method"] + "\n"
        hand_test_content += "API MultipartParam: " + upload_api["multipart_param"] + "\n\n"
    f = open(hand_test_file, "w")
    f.write(hand_test_content)
    f.close() 

def record_unfinished_seq(candidate_api, candidate_api_seq, current_api, unfinished_seq_dir):
    unfinished_seq_filename = candidate_api.api_url.replace("/","!")
    unfinished_seq_content = "-------- VoAPI Unfinished Sequence --------\n"
    unfinished_seq_content += "Candidate API Url: " + candidate_api.api_url + "\n"
    unfinished_seq_content += "Candidate API Method: " + candidate_api.api_method + "\n"
    unfinished_seq_content += "Candidate API Seq: " + api_seq_show(candidate_api_seq) + "\n"
    unfinished_seq_content += "Failed API: " + current_api.api_method + " " + current_api.api_url + "\n"
    unfinished_seq_content += "Failed API Request: " + json.dumps(current_api.api_request_value, indent=2) + "\n"
    f = open(unfinished_seq_dir + unfinished_seq_filename, "a+")
    f.write(unfinished_seq_content)
    f.close()

def record_undetected_suspicious_api(suspicious_api, api_func, suspicious_param, undetected_suspicious_dir):
    undetected_suspicious_file = suspicious_api.api_url.replace("/","!")
    undetected_suspicious_content = "-------- VoAPI Undetected Suspicious API --------\n"
    undetected_suspicious_content += "Suspicious API Vul Type: " + APIFuncAndVulMapping[api_func] + "\n"
    undetected_suspicious_content += "Suspicious API Url: " + suspicious_api.api_url + "\n"
    undetected_suspicious_content += "Suspicious API Method: " + suspicious_api.api_method + "\n"
    undetected_suspicious_content += "Suspicious API Vul Param: " + suspicious_param + "\n\n"
    f = open(undetected_suspicious_dir + undetected_suspicious_file, "a+")
    f.write(undetected_suspicious_content)
    f.close()

def record_vul_api(vul_output_dir, api_func, vul_api, vul_param, test_payload, request_validation_api=False):
    if request_validation_api:
        vul_api_content = ""
    else:
        vul_api_content = "-------- VoAPI Vul API --------\n"
    vul_output_file = (vul_api.api_url + "VoAPI" + vul_param).replace("/","!")
    vul_api_content += "API Vul Type: " + APIFuncAndVulMapping[api_func] + "\n"
    vul_api_content += "Vul API Url: " + vul_api.api_url + "\n"
    vul_api_content += "Vul API Method: " + vul_api.api_method + "\n"
    vul_api_content += "API Vul Param: " + vul_param + "\n"
    vul_api_content += "API Test Payload: " + test_payload + "\n\n"
    if sys.platform.startswith("win"):
        vul_file_path = (vul_output_dir + vul_output_file).replace("\\","/")
    else:
        vul_file_path = vul_output_dir + vul_output_file
    f = open(vul_file_path, "a+")
    f.write(vul_api_content)
    f.close()

def write_log(log_file, log_str):
    f = open(log_file, "a+")
    f.write(log_str)
    f.close()

def write_every_candidate_api_test_log(log_file, candidate_api_seq, candidate_api_seq_relations, candidate_api_test_types):
    log_str = "#"*14 + "\n"
    log_str += "candidate_api_seq: " + str(candidate_api_seq) + "\n"
    for temp_api_template in candidate_api_seq:
        log_str += temp_api_template.api_url + " " + temp_api_template.api_method + "\n"
    log_str += "candidate_api_seq_relations: ---------------\n"
    for candidate_api_seq_relation in candidate_api_seq_relations:
        log_str += "producer_api: {0} {1}\nproducer_param: {2}\nconsumer_api: {3} {4}\nconsumer_param: {5}\n------------\n".format(candidate_api_seq_relation["producer_api"].api_url, candidate_api_seq_relation["producer_api"].api_method, candidate_api_seq_relation["producer_param"], candidate_api_seq_relation["consumer_api"].api_url, candidate_api_seq_relation["consumer_api"].api_method, candidate_api_seq_relation["consumer_param"])
    log_str += "candidate_api_test_types: " + str(candidate_api_test_types) + "\n"
    write_log(log_file, log_str)

def try_extract_upload_path(response_text):
    file_path_pattern = r"(?:[\\/][\w .-]+)+\.\w+"
    file_paths = re.findall(file_path_pattern, response_text)
    return file_paths

def sqlmap_test(baseurl, api_url, api_method, header_dict, request_dict_list, test_params, log_file):
    sqlmap_cmd = ["python", SQLMapPath]
    if baseurl.endswith("/"):
        baseurl = baseurl[:-1]
    api_path_dict, api_header_dict, api_query_dict, api_body_dict = request_dict_list
    if header_dict:
        api_header_dict.update(header_dict)
    # format api_url
    path_params = re.findall(r'({.*?})', api_url)
    if path_params and api_path_dict:
        for path_param in path_params:
            api_url = api_url.replace(path_param, str(api_path_dict[path_param[1:-1]]))
    sqlmap_url = baseurl + api_url
    if api_query_dict:
        sqlmap_url += "?"
        for api_query_key in api_query_dict:
            sqlmap_url += api_query_key + "=" + str(api_query_dict[api_query_key])
            sqlmap_url += "&"
        if sqlmap_url[-1] == "&":
            sqlmap_url = sqlmap_url[:-1]
    sqlmap_cmd += ["-u", "\"" + sqlmap_url + "\""]
    sqlmap_cmd += ["--method=" + "\"" + api_method + "\""]
    if api_header_dict:
        api_header_str = ""
        for api_header_key in api_header_dict:
            api_header_str += api_header_key + ":" + str(api_header_dict[api_header_key])
            api_header_str += "\\n"
        if api_header_str[-2:] == "\\n":
            api_header_str = api_header_str[:-2]
        sqlmap_cmd += ["--headers=" + "\"" + api_header_str + "\""]
    if api_body_dict:
        api_body_str = ""
        for api_body_key in api_body_dict:
            api_body_str += api_body_key + "=" + str(api_body_dict[api_body_key])
            api_body_str += ";"
        if api_body_str[-1] == ";":
            api_body_str = api_body_str[:-1]
        sqlmap_cmd += ["--data=" + "\"" + api_body_str + "\"", "--param-del=\";\""]
    test_param_str = "\""
    for test_param in test_params:
        test_param_str += test_param
        test_param_str += ","
    if test_param_str[-1] == ",":
        test_param_str = test_param_str[:-1]
    test_param_str += "\""
    sqlmap_cmd += ["-p", test_param_str, "--batch", "--smart"]
    sqlmap_cmd_str = " ".join(sqlmap_cmd)
    inject_param_list = []
    try:
        log_str = "---------------------SQLMap Test: " + time.asctime() + "-------------------\n"
        log_str += "sqlmap_cmd: " + sqlmap_cmd_str + "\n"
        write_log(log_file, log_str)
        param_num = len(test_params)
        pipe = subprocess.Popen(sqlmap_cmd_str, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        inject_param_pattern = r"'(.+)' might be injectable"
        count = 0
        for info in iter(pipe.stdout.readline, b''):
            sql_info = info.decode()
            if "heuristic (basic) test" in sql_info:
                count += 1
                match = re.search(inject_param_pattern, sql_info)
                if match:
                    inject_param_list.append(match.group(1))
            if count >= param_num:
                pipe.terminate()
                pipe.wait()
                break
        return inject_param_list
    except Exception as e:
        print(e)
        return inject_param_list
