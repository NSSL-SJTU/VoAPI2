# -*- coding: UTF-8 -*-
import os, re, ssl, socket, argparse
from OpenSSL import crypto

RequestVulnerabilityList = ["ssrf", "command_injection", "xss"]

def create_cert(certificate_dir):
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)
    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = "CN"
    cert.get_subject().ST = "VoAPIProvince"
    cert.get_subject().L = "VoAPILocality"
    cert.get_subject().O = "VoAPIOrganization"
    cert.get_subject().OU = "VoAPIUnit"
    cert.get_subject().CN = "VoAPI"
    cert.get_subject().emailAddress = "beet1e@VoAPI.local"
    cert.set_serial_number(0)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')
    if not certificate_dir.endswith("/"):
        certificate_dir = certificate_dir + "/"
    with open(certificate_dir + "certificate.crt", "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
    with open(certificate_dir + "private.key", "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))
    return certificate_dir + "certificate.crt", certificate_dir + "private.key"

def create_verification_server(server_ip, server_port, certificate_file, key_file):
    verification_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=certificate_file, keyfile=key_file)
    ssl_verification_server = context.wrap_socket(verification_server, server_side=True)
    ssl_verification_server.bind((server_ip, server_port))
    ssl_verification_server.listen(4)
    print("https verification_server listen...")
    return ssl_verification_server

def vul_verification(verification_server, vul_dir):
    while True:
        try:
            socket_conn, _ = verification_server.accept()
            socket_data = socket_conn.recv(1024).decode('utf-8', errors='ignore')
            print(socket_data)
            if socket_data:
                for RequestVulnerability in RequestVulnerabilityList: 
                    if RequestVulnerability in socket_data:
                        print("find ", RequestVulnerability)
                        print(socket_data)
                        vul_filename = socket_data[socket_data.find(RequestVulnerability)+len(RequestVulnerability):socket_data.find(" HTTP/")]
                        vul_output_dir = vul_dir + RequestVulnerability + "/"
                        if not os.path.exists(vul_output_dir):
                            os.makedirs(vul_output_dir)
                        vul_api_content = "-------- VoAPI Vul API --------\n"
                        vul_api_content += "API Vul Type: " + RequestVulnerability + "\n"
                        vul_api_content += "Vul API Url: " + vul_filename[:vul_filename.find("VoAPI")] + "\n"
                        vul_api_content += "API Vul Param: " + vul_filename[vul_filename.find("VoAPI")+len("VoAPI"):] + "\n\n"
                        vul_filename = vul_filename.replace("/", "!")
                        vul_filename = re.sub(r'[<>:"/\\|?*]', '@', vul_filename)
                        f = open(vul_output_dir + vul_filename,"a+")
                        f.write(vul_api_content)
                        f.close()
                        break
                socket_conn.close()
        except ssl.SSLError as e:
            continue
        except socket.timeout:
            socket_conn.close()
            continue
        except Exception as e:
            #socket_conn.close()
            print(e)
            continue
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verification_server_ip', help='Verification Server Ip', type=str, default="127.0.0.1", required=True)
    parser.add_argument('--verification_server_port_for_https', help='Verification Server Port For HTTPS', type=int, default=4445, required=True)
    parser.add_argument('--output', help='Output Dir Absolute Path', type=str, default="./", required=True)
    parser.add_argument('--certificate_dir', help='Certificate Dir Absolute Path', type=str, default="./VoAPIVerificationCert", required=True)
    args = parser.parse_args()
    if args.output == "./":
        output_dir = os.path.abspath('.')
    else:
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        output_dir = args.output
    if not output_dir.endswith("/"):
        output_dir = output_dir + "/"
    vul_dir = output_dir + "vul/"
    if not os.path.exists(vul_dir):
        os.makedirs(vul_dir)
    if args.certificate_dir == "./VoAPIVerificationCert":
        certificate_dir = os.path.abspath('.') + os.sep + "VoAPIVerificationCert"
    else:
        certificate_dir = args.certificate_dir
    certificate_file = ""
    key_file = ""
    for file_name in os.listdir(certificate_dir):
        if os.path.isfile(os.path.join(certificate_dir, file_name)):
            if ".crt" in file_name or ".pem" in file_name:
                certificate_file = os.path.join(certificate_dir, file_name)
            elif ".key" in file_name:
                key_file = os.path.join(certificate_dir, file_name)
    if (not certificate_file) or (not key_file):
        certificate_file, key_file = create_cert(certificate_dir)
    ssl_verification_server = create_verification_server(args.verification_server_ip, args.verification_server_port_for_https, certificate_file, key_file)
    vul_verification(ssl_verification_server, vul_dir)