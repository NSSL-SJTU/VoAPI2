import copy, random
from VoAPIGlobalData import *
from VoAPIUtils import *
class ApiTemplate(object):
    def __init__(self, api_url, api_method, api_request, api_response):
        if api_url.startswith("/"):
            self.api_url = api_url
        else:
            self.api_url = "/" + api_url
        self.api_method = api_method
        if "__body__" in api_request["body"].keys():
            if type(api_request["body"]["__body__"]) == dict:
                api_request["body"] = api_request["body"]["__body__"]
        self.api_request = api_request
        if "headerResponse" not in api_response:
            api_response["headerResponse"] = {}
        self.api_response = api_response
        self.api_request_value = self.init_request_value()
        self.api_response_value = self.init_response_value()

    def init_request_value(self):
        def generate_random_value(param_type):
            return RandomValueDict[param_type][random.randint(0,43)]
        
        def get_param_format(param_name):
            for format_str in ApiParamFormat:
                if format_str in param_name:
                    return [ApiParamFormat[format_str][random.randint(0,43)], "VoAPI_FORMAT"]
            return []
        
        def value_type_conversion(value_list, type):
            result_list = []
            if type == "Number":
                for value in value_list:
                    try:
                        result_list.append(float(value))
                    except:
                        continue
            elif type == "Int":
                for value in value_list:
                    try:
                        result_list.append(int(value))
                    except:
                        continue
            elif type == "Bool":
                for value in value_list:
                    if value.lower() == 'true':
                        result_list.append(True)
                    elif value.lower() == 'false':
                        result_list.append(False)
                    else:
                        continue
            else:
                result_list = value_list
            return result_list
                
        def param_assignment(param_struct, param_name=""):
            param_type = param_struct[0]
            example_value_list = param_struct[1]
            default_value_list = param_struct[2]
            # ToDO: Support is_required
            # is_required = param_struct[3]
            param_name_value = []
            if default_value_list:
                if "RESTler" not in default_value_list[0]:
                    default_value_list = value_type_conversion(default_value_list, param_type)
                    param_name_value = [default_value_list[0], "VoAPI_SPECIFICATION"]
                else:
                    param_name_value = [generate_random_value(param_type), "VoAPI_RANDOM"]
            if example_value_list:
                # example_value > default_value
                example_value_list = value_type_conversion(example_value_list, param_type)
                param_name_value = [example_value_list[0], "VoAPI_SPECIFICATION"]
            param_format_value = get_param_format(param_name)
            if param_format_value and param_name_value:
                if ParamValuePriority[param_format_value[1]] > ParamValuePriority[param_name_value[1]]:
                    param_name_value = param_format_value
            if param_name_value:
                return param_name_value
            else:
                return [generate_random_value(param_type), "VoAPI_RANDOM"]
        
        def traverse_and_assignment(param_dict, api_request_param_dict, param_name):
            param_struct = param_dict[param_name]
            api_request_param_struct = api_request_param_dict[param_name]
            if param_struct[0] == "Array":
                for array_param_index in range(1, len(param_struct)):
                    if type(param_struct[array_param_index]) == dict:
                        for array_param_name in param_struct[array_param_index]:
                            traverse_and_assignment(param_struct[array_param_index], api_request_param_struct[array_param_index], array_param_name)
                    elif type(param_struct[array_param_index]) == list:
                        param_struct[array_param_index] = param_assignment(param_struct[array_param_index])
                    elif type(param_struct[array_param_index]) == bool:
                        # ignore is_required
                        continue
                    else:
                        print("Not Supported param_struct in init_request_value: ", param_struct[array_param_index])
            elif param_struct[0] == "Property":
                if type(param_struct[1]) == list:
                    # fix api_resquest Struct
                    api_request_param_dict[param_name] = param_struct[1]
                    param_dict[param_name] = param_assignment(param_struct[1])
                elif type(param_struct[1]) == dict:
                    for property_param_name in param_struct[1]:
                        traverse_and_assignment(param_struct[1], api_request_param_struct[1], property_param_name)
                else:
                    print("Not supported param_struct[1] in init_request_value: ", param_struct[1])
            else:
                param_dict[param_name] = param_assignment(param_dict[param_name], param_name)
        api_request_value = copy.deepcopy(self.api_request)
        for api_request_part in api_request_value:
            if api_request_value[api_request_part]:
                if (len(api_request_value[api_request_part].keys()) == 1) and (type(api_request_value[api_request_part][list(api_request_value[api_request_part].keys())[0]]) == dict):
                    # Ignore meaningless first parameter names in OpenAPI V2 body parameters
                    api_request_value[api_request_part] = api_request_value[api_request_part][list(api_request_value[api_request_part].keys())[0]]
                    self.api_request[api_request_part] = self.api_request[api_request_part][list(self.api_request[api_request_part].keys())[0]]
                for param_name in api_request_value[api_request_part]:
                    traverse_and_assignment(api_request_value[api_request_part], self.api_request[api_request_part], param_name)    
        return api_request_value
    
    def init_response_value(self):
        def value_type_conversion(value_list, type):
            result_list = []
            if type == "Number":
                for value in value_list:
                    try:
                        result_list.append(float(value))
                    except:
                        continue
            elif type == "Int":
                for value in value_list:
                    try:
                        result_list.append(int(value))
                    except:
                        continue
            elif type == "Bool":
                for value in value_list:
                    if value.lower() == 'true':
                        result_list.append(True)
                    elif value.lower() == 'false':
                        result_list.append(False)
                    else:
                        continue
            else:
                result_list = value_list
            return result_list
        def param_assignment(param_struct):
            param_type = param_struct[0]
            example_value_list = param_struct[1]
            default_value_list = param_struct[2]
            # is_required = param_struct[3]
            param_name_value = []
            # response_value only support VoAPI_SPECIFICATION, if not, response_value = []
            if default_value_list:
                if "RESTler" not in default_value_list[0]:
                    default_value_list = value_type_conversion(default_value_list, param_type)
                    param_name_value = [default_value_list[0], "VoAPI_SPECIFICATION"]
            if example_value_list:
                # example_value > default_value
                example_value_list = value_type_conversion(example_value_list, param_type)
                param_name_value = [example_value_list[0], "VoAPI_SPECIFICATION"]
            return param_name_value
        
        def traverse_and_assignment(param_dict, api_response_param_dict, param_name):
            #print("param_dict: ", param_dict, param_name)
            param_struct = param_dict[param_name]
            api_response_param_struct = api_response_param_dict[param_name]
            #print("param_struct: ", param_struct)
            if param_struct[0] == "Array":
                for array_param_index in range(1, len(param_struct)):
                    if type(param_struct[array_param_index]) == dict:
                        for array_param_name in param_struct[array_param_index]:
                            traverse_and_assignment(param_struct[array_param_index], api_response_param_struct[array_param_index], array_param_name)
                    elif type(param_struct[array_param_index]) == list:
                        param_struct[array_param_index] = param_assignment(param_struct[array_param_index])
                    elif type(param_struct[array_param_index]) == bool:
                        # ignore is_required
                        continue
                    else:
                        print("Not Supported param_struct in init_response_value: ", param_struct[array_param_index])
            elif param_struct[0] == "Property":
                if type(param_struct[1]) == list:
                    # fix api_response Struct
                    api_response_param_dict[param_name] = param_struct[1]
                    param_dict[param_name] = param_assignment(param_struct[1])
                elif type(param_struct[1]) == dict:
                    for property_param_name in param_struct[1]:
                        traverse_and_assignment(param_struct[1], api_response_param_struct[1], property_param_name)
                else:
                    print("Not supported param_struct[1] in init_response_value: ", param_struct[1])
            else:
                param_dict[param_name] = param_assignment(param_dict[param_name])
                
        api_response_value = copy.deepcopy(self.api_response)
        for api_response_part in api_response_value:
            if api_response_value[api_response_part]:
                for param_name in api_response_value[api_response_part]:
                    traverse_and_assignment(api_response_value[api_response_part], self.api_response[api_response_part], param_name)
        return api_response_value

    def show(self):
        print("api_url: ", self.api_url)
        print("api_method: ", self.api_method)
        print("api_request: ", self.api_request)
        print("api_response: ", self.api_response)
        print("api_request_value: ", self.api_request_value)
        print("api_response_value: ", self.api_response_value)

    def show_txt(self):
        show_str = "api_url: " + self.api_url + "\n"
        show_str += "api_method: " + self.api_method + "\n"
        show_str += "api_request: " + str(self.api_request) + "\n"
        show_str += "api_response: " + str(self.api_response) + "\n"
        show_str += "api_request_value: " + str(self.api_request_value) + "\n"
        show_str += "api_response_value: "+ str(self.api_response_value) + "\n"
        show_str += "##################" + "\n"
        f = open("api_template.txt","a+")
        f.write(show_str)
        f.close()


# Example:
#     api_url = "/teams/{teamId}/memberships"
#     api_method = "Post"
#     api_request = {
#         "path": {
#             "teamId": ["String", [], ["RESTlerString"], False],
#         },
#         "header": {},
#         "query": {},
#         "body": {
#             "email": ["String", [], ["RESTlerString"], False],
#             "name": ["String", [], ["RESTlerString"], False],
#             "roles": ["Array",
#                 ["Int", [], ["0"], False],
#                 {
#                     "role1": ["String", ["my_role"], [], False],
#                     "role2": ["Array", {
#                         "role2-1": ["String", ["my_role2-1"], [], False]
#                     }, False]
#                 },
#                 ["String", [], ["RESTlerString"], False],
#                 False
#             ],
#             "url": ["String", [], ["RESTlerString"], False]
#         }
#     }
#     api_response = {
#         "bodyResponse": {
#             "$id": ["String", [], ["RESTlerString"], False],
#             "invited": ["Int", [], ["0"], False],
#             "name": ["String", [], ["RESTlerString"], False],
#             "teamId": ["String", [], ["RESTlerString"], False]
#         },
#         "headerResponse": {}
#     }