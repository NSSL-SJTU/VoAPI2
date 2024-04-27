import json
from lark import Lark, Transformer
from VoAPITemplate import *

# class ApiTemplate(object):
#     def __init__(self, api_url: str, api_method:str, api_request_parameters, api_response):
#         self.api_url = "/api/blog/posts"
#         self.api_method = "Get"
#         self.api_request_parameters = {
#           "path": {},
#           "header": {},
#           "query": {
#             "page": ["Int", [], ["10"], False],
#             "per_page": ["Int", [], ["5"], False]
#           },
#           "body": {}
#         }
#         self.api_response = {
#           "bodyResponse": {
#             "items": ["Array", {
#               "id" : ["Int", ["22"], [], False],
#               "body": ["String", ["my first blog post"], [], False],
#               "checksum": ["String", ["abcde"], [], False]
#             }],
#             "page": ["Int", [], ["10"], False],
#             "per_page": ["Int", [], ["5"], False],
#           },
#           "headerResponse": {}
#         }

class Parser(Transformer):
    def api_template(self, args):
        return {
            "request_id": args[0],
            "api_request_parameters": args[1],
            "api_response": args[2],
        }

    def request_id(self, args):
        # print(args.pretty())
        # return args
        return {
            "api_url": args[0],  # .children[0].value[1:-1],
            "api_method": args[2].children[0].value,
        }
    # def request_parameters(self, args):

    def request_parameters(self, args):
        # print(args)
        return {"path": args[0], "header": args[1], "query": args[2], "body": args[3]}

    def request_parameters_header(self, args):
        # request_parameters_header "query" "=" request_parameters_header "body" "=" request_parameters_header "}"
        # print(args)
        dict_list = [arg for arg in args if arg is not None]
        request_parameter_dict = {}
        for dict_ele in dict_list:
            request_parameter_dict.update(dict_ele)
        return request_parameter_dict

    def request_parameters_header_element(self, args):
        # request_parameters_header_element: "(" parameter_payload_source "," request_parameters_payload ")"
        # print(args[1])
        return args[1]

    def request_parameters_payload(self, args):
        # request_parameters_payload: request_parameters_payload_parameter_list | request_parameters_payload_example
        # print(args[0])
        return args[0]

    def request_parameters_payload_parameter_list(self, args):
        # request_parameters_payload_parameter_list: "ParameterList" "(" ["seq"] "[" request_parameter? (";" request_parameter)* "]" ")"
        dict_list = [arg for arg in args if arg is not None]
        request_parameter_dict = {}
        for dict_ele in dict_list:
            request_parameter_dict.update(dict_ele)
        if len(request_parameter_dict) == 1 and "" in request_parameter_dict:
            return request_parameter_dict[""]
        
        # print(request_parameter_dict)
        return request_parameter_dict

    def request_parameter(self, args):
        # request_parameter: "{" "name" "=" request_parameter_name "payload" "=" tree_node "serialization" "=" parameter_serialization "}"
        # print(args)
        name = args[0]
        payload = args[1]
        if isinstance(payload, dict) and "" in payload and len(payload) == 1:
            payload = payload[""]
        return {name: payload}

    def tree_node(self, args):
        # tree_node: leaf_node | internal_node
        # print(args[0])
        node = args[0]
        # if isinstance(node, dict) and "" in node and len(node) == 1:
        #     return node[""]
        return node 

    def internal_node(self, args):
        # internal_node: "InternalNode" "(" inode_data "," seq_internal_node ")"
        # pass
        inode_data = args[0]
        seq_internal_node = args[1]
        if inode_data["propertyType"] == "Object":
            return seq_internal_node
        else:
            return {
                inode_data["name"]: [
                    inode_data["propertyType"],
                    seq_internal_node,
                    inode_data["isRequired"],
                ]
            }

    def enum_type(self, args):
        # enum_type: "Enum" enum_args
        # enum_args: "(" enum_tag "," type_name "," value_list "," option_value ")"
        # enum_arg: ESCAPED_STRING | type_name | value_list | option_value 
        # enum_tag: ESCAPED_STRING
        return args[0]
        # pass

    def enum_args(self, args):
        # enum_args: "(" enum_tag "," type_name "," value_list "," option_value ")"
        enum_tag, type_name, value_list, option_value = args
        return [type_name, value_list, option_value]
    
    def value_list(self, args):
        # value_list: "[" value? (";" value)* "]"
        return [arg for arg in args if arg is not None]
    
    # def value_list(self, args):


    def option_value(self, args):
        # option_value: "Some" ESCAPED_STRING | none
        if args[0] is None:
            return []
        return [args[0]]

    def seq_internal_node(self, args):
        # seq_internal_node: ["seq"] "[" tree_node (";" tree_node)* "]"
        # print(args)
        # return args
        seq_node = {}
        # pprint(args)
        for arg in args:
            seq_node.update(arg)
        if len(seq_node) == 1 and "" in seq_node:
            return seq_node[""]
        return seq_node

    def inode_data(self, args):
        # inode_data: "{" "name" "=" inner_node_name "payload" "=" fuzzing_payload_option "propertyType" "=" nested_type "isRequired" "=" boolean "isReadOnly" "=" boolean "}"
        name = args[0].children[0]
        # print('name',name)
        # fuzzing_payload_option = args[1]
        property_type = args[2].children[0].value

        is_required = args[3]
        return {"name": name, "propertyType": property_type, "isRequired": is_required}

    def leaf_node(self, args):
        # leaf_node: "LeafNode" "{" "name" "=" leaf_node_name "payload" "=" fuzzing_payload "isRequired" "=" boolean "isReadOnly" "=" boolean "}"
        name = args[0]
        fuzzing_payload = args[1]
        # print(fuzzing_payload)
        is_required = args[2]
        if isinstance(fuzzing_payload, tuple):
            fuzzing_payload, fuzzing_type = fuzzing_payload
            assert isinstance(fuzzing_payload, dict)
            if fuzzing_type == "Array":
            # solve Constant object
                for key in fuzzing_payload:
                    for ele in fuzzing_payload[key]:
                        if isinstance(ele, list):
                            ele.append(is_required)
                return {name: fuzzing_payload }
            elif fuzzing_type == "String":
                for key in fuzzing_payload:
                    if isinstance(fuzzing_payload[key], list) and len(fuzzing_payload[key]) == 3:
                        fuzzing_payload[key].append(is_required)
                return {name: ["Property", fuzzing_payload, is_required]}
            else:
                assert False              
        return {name: fuzzing_payload + [is_required]}

    def leaf_node_name(self, args):
        return args[0]

    def fuzzing_payload(self, args):
        # fuzzing_payload: payload_fuzzable | payload_constant | payload_parts | any
        fuzz_payload = args[0]
        # print(type(fuzz_payload))
        if type(fuzz_payload) == str and "Constant" in fuzz_payload:
            begin_pos = fuzz_payload.find('"')
            end_pos = fuzz_payload.rfind('"')
            fuzz_dict = json.loads(fuzz_payload[begin_pos+1:end_pos])
            fuzz_dict_ans = {}
            isArray = False
            isString = False
            for key in fuzz_dict:
                if isinstance(fuzz_dict[key], list):
                    fuzz_dict_ans[key] = ["Array"]
                    for ele in fuzz_dict[key]:
                        fuzz_dict_ans[key].append(["String", [], ele])
                    isArray = True
                elif isinstance(fuzz_dict[key], str):
                    isString = True
                    fuzz_dict_ans[key] = ["String", [], fuzz_dict[key]]
            return (fuzz_dict_ans, "String" if isString else "Array")
            # return fuzz_dict_ans
        return fuzz_payload
    
    def payload_constant(self, args):
        # payload_constant: "Constant" "(" primitive_type value ")"
        primitive_type = args[0]
        value = args[1]
        return [primitive_type, [value], []]

    def payload_fuzzable(self, args):
        return args[0]

    def payload_fuzzable_args(self, args):
        # payload_fuzzable_args: "primitiveType" "=" primitive_type "defaultValue" "=" default_value "exampleValue" "=" example_value "parameterName" "=" parameter_name "dynamicObject" "=" dynamic_object
        primitive_type = args[0]
        # default_value = args[1]
        if isinstance(primitive_type, str):
            example_value = args[2]
            default_value = args[1]
            return [primitive_type, example_value, default_value]
        else:
            # primitive_type is enum_type
            enum_list = primitive_type
            default_value = args[1]
            # print(default_value)
            # print(enum_list)
            enum_list[2] += default_value
            return enum_list
        
    def handle_fuzzable_value(self, string):
        neat_string = string.strip()
        if neat_string.startswith('"') and neat_string.endswith('"'):
            return neat_string[1:-1]
        # return string.strip()

    def default_value(self, args):
        # default_value: default_any_value
        # return args[0].children[0].value
        return [self.handle_fuzzable_value(args[0].children[0].value)]
    
    def example_value(self, args):
        return args[0]

    def example_option_value(self, args):
        # example_option_value: none | example_any_value
        # example_any_value: /.+?(?=param)/s
        # print(args[0])
        if args[0] is None:
            return []
        return [self.handle_fuzzable_value(args[0].children[0].value)]

    def primitive_type(self, args):
        # primitive_type: type_name | enum_type
        return args[0]

    def response(self, args):
        # response: "response" ":" ("Some" response_type | none)
        # response_type:  "{" "bodyResponse" "=" tree_node_option "headerResponse" "=" response_type_headerresponse "linkAnnotations" "=" ignored_field "}"
        # tree_node_option: "Some" "(" tree_node ")" | none
        if args[0] is None:
            return {"bodyResponse": {}}
        return {"bodyResponse": args[0]}

    def response_type(self, args):
        # response_type:  "{" "bodyResponse" "=" tree_node_option "headerResponse" "=" response_type_headerresponse "linkAnnotations" "=" ignored_field "}"
        # print(args)
        return args[0]

    def tree_node_option(self, args):
        if args[0] is None:
            return {}
        return args[0]

    none = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False
    ESCAPED_STRING = lambda self, args: args.value[1:-1]
    type_name = lambda self, args: args[0].value
    value = lambda self, args: args[0]
    any = lambda self, args: args[0].value

class Convert():
    def __init__(self, lark_file:str, fsharp_struct_file:str):
        self.SPLITTER = "#############"
        self.lark_file = lark_file
        self.text_file = fsharp_struct_file
        with open(self.lark_file, "r", encoding='utf-8') as f:
            self.fsharp_struct_grammar = f.read()
        with open(self.text_file, "r", encoding='utf-8') as f:
            self.fsharp_struct_text = f.read()
        self.fsharp_parser = Lark(self.fsharp_struct_grammar, start="api_template", parser="earley")
        self.api_templates = [] 
        self.transformer = Parser()
        for api_struct in self.fsharp_struct_text.split(self.SPLITTER):
            if "requestId" not in api_struct:
                continue
            # print('api_struct', api_struct)
            tree = self.fsharp_parser.parse(api_struct)
            api_info_dict = self.transformer.transform(tree)
            #print(api_info_dict)
            api_template = ApiTemplate(api_info_dict["request_id"]["api_url"], api_info_dict["request_id"]["api_method"], api_info_dict["api_request_parameters"], api_info_dict["api_response"])
            self.api_templates.append(api_template)

    def get_api_templete_list(self):
        return self.api_templates
# def generate_api_templete_list(filename:str):


# with open("f.lark", "r") as f:
#     fsharp_struct_grammar = f.read()
# with open("fsharp_struct.txt", "r") as f:
#     fsharp_struct_text = f.read()



# fsharp_parser = Lark(fsharp_struct_grammar, start="api_template", parser="earley")
# tree = fsharp_parser.parse(fsharp_struct_text)
# transformer = Parser()
# result = transformer.transform(tree)
# pprint(result)
# api_template = ApiTemplate(result["request_id"]["api_url"], result["request_id"]["api_method"], result["api_request_parameters"], result["api_response"])
# pprint(api_template)
        
def parse_restler_compile(api_info_file):
    convert = Convert("RESTlerCompileStruct.lark", api_info_file)
    api_template_list = convert.get_api_templete_list()
    return api_template_list