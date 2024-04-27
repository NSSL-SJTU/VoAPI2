""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_account_recovery_post_secret = dependencies.DynamicVariable("_account_recovery_post_secret")

_account_recovery_post_userId = dependencies.DynamicVariable("_account_recovery_post_userId")

_account_verification_post_secret = dependencies.DynamicVariable("_account_verification_post_secret")

_account_verification_post_userId = dependencies.DynamicVariable("_account_verification_post_userId")

_database_collections__collectionId__put_name = dependencies.DynamicVariable("_database_collections__collectionId__put_name")

_functions__functionId__put_name = dependencies.DynamicVariable("_functions__functionId__put_name")

_storage_files__fileId__put_name = dependencies.DynamicVariable("_storage_files__fileId__put_name")

_teams__teamId__put_name = dependencies.DynamicVariable("_teams__teamId__put_name")

_teams__teamId__memberships_post_roles_0 = dependencies.DynamicVariable("_teams__teamId__memberships_post_roles_0")

def parse_accountrecoverypost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None
    temp_8173 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["secret"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8173 = str(data["userId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262 or temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_account_recovery_post_secret", temp_7262)
    if temp_8173:
        dependencies.set_variable("_account_recovery_post_userId", temp_8173)


def parse_accountverificationpost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7680 = None
    temp_5581 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7680 = str(data["secret"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5581 = str(data["userId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680 or temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_account_verification_post_secret", temp_7680)
    if temp_5581:
        dependencies.set_variable("_account_verification_post_userId", temp_5581)


def parse_databasecollectionscollectionIdput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_2060 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("_database_collections__collectionId__put_name", temp_2060)


def parse_functionsfunctionIdput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5588 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5588 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5588):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5588:
        dependencies.set_variable("_functions__functionId__put_name", temp_5588)


def parse_storagefilesfileIdput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9060 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9060:
        dependencies.set_variable("_storage_files__fileId__put_name", temp_9060)


def parse_teamsteamIdput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4421 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_4421 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4421):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4421:
        dependencies.set_variable("_teams__teamId__put_name", temp_4421)


def parse_teamsteamIdmembershipspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9775 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9775 = str(data["roles"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9775):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9775:
        dependencies.set_variable("_teams__teamId__memberships_post_roles_0", temp_9775)

req_collection = requests.RequestCollection([])
# Endpoint: /account, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account"
)
req_collection.add_request(request)

# Endpoint: /account, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account"
)
req_collection.add_request(request)

# Endpoint: /account/email, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("email"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/email"
)
req_collection.add_request(request)

# Endpoint: /account/logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/logs"
)
req_collection.add_request(request)

# Endpoint: /account/name, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("name"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/name"
)
req_collection.add_request(request)

# Endpoint: /account/password, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("password"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "oldPassword":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/password"
)
req_collection.add_request(request)

# Endpoint: /account/prefs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prefs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/prefs"
)
req_collection.add_request(request)

# Endpoint: /account/prefs, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prefs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "prefs":"""),
    primitives.restler_fuzzable_object("RESTlerObject"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/prefs"
)
req_collection.add_request(request)

# Endpoint: /account/recovery, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recovery"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "url":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_accountrecoverypost,
            'dependencies':
            [
                _account_recovery_post_secret.writer(),
                _account_recovery_post_userId.writer()
            ]
        }

    },

],
requestId="/account/recovery"
)
req_collection.add_request(request)

# Endpoint: /account/recovery, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recovery"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "password":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "passwordAgain":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "secret":"""),
    primitives.restler_static_string(_account_recovery_post_secret.reader(), quoted=True),
    primitives.restler_static_string(""",
    "userId":"""),
    primitives.restler_static_string(_account_recovery_post_userId.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/recovery"
)
req_collection.add_request(request)

# Endpoint: /account/sessions, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/sessions"
)
req_collection.add_request(request)

# Endpoint: /account/sessions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/sessions"
)
req_collection.add_request(request)

# Endpoint: /account/sessions/{sessionId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/sessions/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /account/sessions/{sessionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/sessions/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /account/verification, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("verification"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "url":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_accountverificationpost,
            'dependencies':
            [
                _account_verification_post_secret.writer(),
                _account_verification_post_userId.writer()
            ]
        }

    },

],
requestId="/account/verification"
)
req_collection.add_request(request)

# Endpoint: /account/verification, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("verification"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "secret":"""),
    primitives.restler_static_string(_account_verification_post_secret.reader(), quoted=True),
    primitives.restler_static_string(""",
    "userId":"""),
    primitives.restler_static_string(_account_verification_post_userId.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/account/verification"
)
req_collection.add_request(request)

# Endpoint: /avatars/browsers/{code}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("avatars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("browsers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quality="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/avatars/browsers/{code}"
)
req_collection.add_request(request)

# Endpoint: /avatars/credit-cards/{code}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("avatars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credit-cards"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quality="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/avatars/credit-cards/{code}"
)
req_collection.add_request(request)

# Endpoint: /avatars/favicon, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("avatars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("favicon"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("url="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/avatars/favicon"
)
req_collection.add_request(request)

# Endpoint: /avatars/flags/{code}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("avatars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("flags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quality="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/avatars/flags/{code}"
)
req_collection.add_request(request)

# Endpoint: /avatars/image, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("avatars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("image"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("url="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/avatars/image"
)
req_collection.add_request(request)

# Endpoint: /avatars/initials, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("avatars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("initials"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("color="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("background="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/avatars/initials"
)
req_collection.add_request(request)

# Endpoint: /avatars/qr, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("avatars"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("qr"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("text="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("size="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("margin="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("download="),
    primitives.restler_fuzzable_bool("RESTlerBool"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/avatars/qr"
)
req_collection.add_request(request)

# Endpoint: /database/collections, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections"
)
req_collection.add_request(request)

# Endpoint: /database/collections, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "read":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "rules":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "write":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections"
)
req_collection.add_request(request)

# Endpoint: /database/collections/{collectionId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_database_collections__collectionId__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections/{collectionId}"
)
req_collection.add_request(request)

# Endpoint: /database/collections/{collectionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_database_collections__collectionId__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections/{collectionId}"
)
req_collection.add_request(request)

# Endpoint: /database/collections/{collectionId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("collectionId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "read":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "rules":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "write":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_databasecollectionscollectionIdput,
            'dependencies':
            [
                _database_collections__collectionId__put_name.writer()
            ]
        }

    },

],
requestId="/database/collections/{collectionId}"
)
req_collection.add_request(request)

# Endpoint: /database/collections/{collectionId}/documents, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_database_collections__collectionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("documents"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filters="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderField="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderCast="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections/{collectionId}/documents"
)
req_collection.add_request(request)

# Endpoint: /database/collections/{collectionId}/documents, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_database_collections__collectionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("documents"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "data":"""),
    primitives.restler_fuzzable_object("RESTlerObject"),
    primitives.restler_static_string(""",
    "parentDocument":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "parentProperty":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "parentPropertyType":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "read":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "write":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections/{collectionId}/documents"
)
req_collection.add_request(request)

# Endpoint: /database/collections/{collectionId}/documents/{documentId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_database_collections__collectionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("documents"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections/{collectionId}/documents/{documentId}"
)
req_collection.add_request(request)

# Endpoint: /database/collections/{collectionId}/documents/{documentId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_database_collections__collectionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("documents"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections/{collectionId}/documents/{documentId}"
)
req_collection.add_request(request)

# Endpoint: /database/collections/{collectionId}/documents/{documentId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("database"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collections"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_database_collections__collectionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("documents"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "data":"""),
    primitives.restler_fuzzable_object("RESTlerObject"),
    primitives.restler_static_string(""",
    "read":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "write":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/database/collections/{collectionId}/documents/{documentId}"
)
req_collection.add_request(request)

# Endpoint: /functions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions"
)
req_collection.add_request(request)

# Endpoint: /functions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "events":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "execute":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "runtime":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "schedule":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "timeout":"""),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string(""",
    "vars":"""),
    primitives.restler_fuzzable_object("RESTlerObject"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("functionId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "events":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "execute":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "schedule":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "timeout":"""),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string(""",
    "vars":"""),
    primitives.restler_fuzzable_object("RESTlerObject"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_functionsfunctionIdput,
            'dependencies':
            [
                _functions__functionId__put_name.writer()
            ]
        }

    },

],
requestId="/functions/{functionId}"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}/executions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("executions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}/executions"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}/executions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("executions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "data":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}/executions"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}/executions/{executionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("executions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}/executions/{executionId}"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}/tag, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tag"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "tag":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}/tag"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}/tags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}/tags"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}/tags, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}/tags"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}/tags/{tagId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}/tags/{tagId}"
)
req_collection.add_request(request)

# Endpoint: /functions/{functionId}/tags/{tagId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_functions__functionId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/functions/{functionId}/tags/{tagId}"
)
req_collection.add_request(request)

# Endpoint: /health, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health"
)
req_collection.add_request(request)

# Endpoint: /health/anti-virus, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("anti-virus"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/anti-virus"
)
req_collection.add_request(request)

# Endpoint: /health/cache, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cache"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/cache"
)
req_collection.add_request(request)

# Endpoint: /health/db, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("db"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/db"
)
req_collection.add_request(request)

# Endpoint: /health/queue/certificates, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("queue"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("certificates"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/queue/certificates"
)
req_collection.add_request(request)

# Endpoint: /health/queue/functions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("queue"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("functions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/queue/functions"
)
req_collection.add_request(request)

# Endpoint: /health/queue/logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("queue"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/queue/logs"
)
req_collection.add_request(request)

# Endpoint: /health/queue/tasks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("queue"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tasks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/queue/tasks"
)
req_collection.add_request(request)

# Endpoint: /health/queue/usage, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("queue"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("usage"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/queue/usage"
)
req_collection.add_request(request)

# Endpoint: /health/queue/webhooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("queue"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webhooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/queue/webhooks"
)
req_collection.add_request(request)

# Endpoint: /health/storage/local, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("local"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/storage/local"
)
req_collection.add_request(request)

# Endpoint: /health/time, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("health"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("time"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/health/time"
)
req_collection.add_request(request)

# Endpoint: /locale, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locale"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/locale"
)
req_collection.add_request(request)

# Endpoint: /locale/continents, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locale"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("continents"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/locale/continents"
)
req_collection.add_request(request)

# Endpoint: /locale/countries, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locale"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("countries"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/locale/countries"
)
req_collection.add_request(request)

# Endpoint: /locale/countries/eu, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locale"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("countries"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("eu"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/locale/countries/eu"
)
req_collection.add_request(request)

# Endpoint: /locale/countries/phones, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locale"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("countries"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phones"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/locale/countries/phones"
)
req_collection.add_request(request)

# Endpoint: /locale/currencies, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locale"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("currencies"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/locale/currencies"
)
req_collection.add_request(request)

# Endpoint: /locale/languages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locale"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("languages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/locale/languages"
)
req_collection.add_request(request)

# Endpoint: /storage/files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/storage/files"
)
req_collection.add_request(request)

# Endpoint: /storage/files, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/storage/files"
)
req_collection.add_request(request)

# Endpoint: /storage/files/{fileId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_storage_files__fileId__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/storage/files/{fileId}"
)
req_collection.add_request(request)

# Endpoint: /storage/files/{fileId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_storage_files__fileId__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/storage/files/{fileId}"
)
req_collection.add_request(request)

# Endpoint: /storage/files/{fileId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("fileId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "read":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "write":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_storagefilesfileIdput,
            'dependencies':
            [
                _storage_files__fileId__put_name.writer()
            ]
        }

    },

],
requestId="/storage/files/{fileId}"
)
req_collection.add_request(request)

# Endpoint: /storage/files/{fileId}/download, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_storage_files__fileId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("download"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/storage/files/{fileId}/download"
)
req_collection.add_request(request)

# Endpoint: /storage/files/{fileId}/preview, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_storage_files__fileId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("preview"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("width="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("height="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("gravity="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quality="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("borderWidth="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("borderColor="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("borderRadius="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("opacity="),
    primitives.restler_fuzzable_number("RESTlerNumber"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rotation="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("background="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("output="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/storage/files/{fileId}/preview"
)
req_collection.add_request(request)

# Endpoint: /storage/files/{fileId}/view, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("storage"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_storage_files__fileId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("view"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/storage/files/{fileId}/view"
)
req_collection.add_request(request)

# Endpoint: /teams, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams"
)
req_collection.add_request(request)

# Endpoint: /teams, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "roles":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams"
)
req_collection.add_request(request)

# Endpoint: /teams/{teamId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__teamId__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{teamId}"
)
req_collection.add_request(request)

# Endpoint: /teams/{teamId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__teamId__put_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{teamId}"
)
req_collection.add_request(request)

# Endpoint: /teams/{teamId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("teamId", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_teamsteamIdput,
            'dependencies':
            [
                _teams__teamId__put_name.writer()
            ]
        }

    },

],
requestId="/teams/{teamId}"
)
req_collection.add_request(request)

# Endpoint: /teams/{teamId}/memberships, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__teamId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{teamId}/memberships"
)
req_collection.add_request(request)

# Endpoint: /teams/{teamId}/memberships, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__teamId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "roles":
    [
        """),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("""
    ],
    "url":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_teamsteamIdmembershipspost,
            'dependencies':
            [
                _teams__teamId__memberships_post_roles_0.writer()
            ]
        }

    },

],
requestId="/teams/{teamId}/memberships"
)
req_collection.add_request(request)

# Endpoint: /teams/{teamId}/memberships/{membershipId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__teamId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{teamId}/memberships/{membershipId}"
)
req_collection.add_request(request)

# Endpoint: /teams/{teamId}/memberships/{membershipId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__teamId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "roles":"""),
    primitives.restler_static_string(_teams__teamId__memberships_post_roles_0.reader(), quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{teamId}/memberships/{membershipId}"
)
req_collection.add_request(request)

# Endpoint: /teams/{teamId}/memberships/{membershipId}/status, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_teams__teamId__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "secret":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "userId":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{teamId}/memberships/{membershipId}/status"
)
req_collection.add_request(request)

# Endpoint: /users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderType="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users"
)
req_collection.add_request(request)

# Endpoint: /users, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("RESTlerString", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/logs"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/prefs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prefs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/prefs"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/prefs, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("prefs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "prefs":"""),
    primitives.restler_fuzzable_object("RESTlerObject"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/prefs"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/sessions, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/sessions"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/sessions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/sessions"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/sessions/{sessionId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/sessions/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/status, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "status":"""),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/status"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/verification, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("verification"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: appwrite.io\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "emailVerification":"""),
    primitives.restler_fuzzable_bool("RESTlerBool"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/verification"
)
req_collection.add_request(request)
