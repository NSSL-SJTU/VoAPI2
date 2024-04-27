# -*- coding: UTF-8 -*-
import os, re, socket, argparse

RequestVulnerabilityList = ["ssrf", "command_injection", "xss"]

def create_verification_server(server_ip="127.0.0.1", server_port=4444):
    verification_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    verification_server.bind((server_ip, server_port))
    verification_server.listen(4)
    print("verification_server listen...")
    return verification_server

def vul_verification(verification_server, vul_dir):
    while True:
        try:
            socket_conn, _ = verification_server.accept()
            socket_data = socket_conn.recv(1024).decode('utf-8', errors='ignore')
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
        except socket.timeout:
            socket_conn.close()
            continue
        except Exception as e:
            socket_conn.close()
            print(e)
            continue
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verification_server_ip', help='Verification Server Ip', type=str, default="127.0.0.1", required=True)
    parser.add_argument('--verification_server_port', help='Verification Server Port', type=int, default=4444, required=True)
    parser.add_argument('--output', help='Output Dir Absolute Path', type=str, default="./", required=True)
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
    verification_server = create_verification_server(args.verification_server_ip, args.verification_server_port)
    vul_verification(verification_server, vul_dir)