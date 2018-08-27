#! /usr/bin/env python
#
# Weak Firewall Rule Discovery Tool
# By @Pink_P4nther <pinkp4nther@protonmail.com>
# This tool can help discover allowed outgoing connections
#

VERSION = "0.0.2"
import socket
import sys
import requests
import threading
import select
import argparse

#socket.setdefaulttimeout(2)
#print(str(socket.getdefaulttimeout()))
banner = """
-=< Reverse Shell Fuzzer {} >=-
By @Pink_P4nther <pinkp4nther@protonmail.com>
A weak firewall rule discovery tool
""".format(VERSION)
print(banner)
# Common port list
commonPorts = [20,21,22,23,25,53,80,81,110,139,143,443,445,465,587,993,995,2222,3306,8000,8080,8181,8443,9050]

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("--url","-u",help="The URL of the pd.php script")
parser.add_argument("--mode","-m",choices=["a","c","l"],help="The port iteration mode. Modes: (a)ll,(c)ommon,(l)ist")
parser.add_argument("--list","-l",help="If mode is 'l' then use this to specify list path")
parser.add_argument("--bind","-b",help="Specify bind address: Default is 0.0.0.0")
parser.add_argument("--useragent","-ua",help="Specify user agent to request with: Default is Firefox Linux")
args = parser.parse_args()

# Parse URL
if args.url:
    URL = args.url
    print("[*] URL: {}".format(URL))
else:
    sys.exit("URL not specified! Use -h for help!")

# Parse Mode
if args.mode:
    MODE = args.mode
    print("[*] MODE: {}".format(MODE))
else:
    sys.exit("MODE not specified!")

# Parse Port List
if MODE == "l" and args.list:
    LISTPATH = args.list
    print("[*] LIST: {}".format(LISTPATH))
elif MODE == "l":
    sys.exit("[!] You must specify a port list: --list /path/to/list.lst")
else:
    pass

# Parse Bind Address
if args.bind:
    HOST = args.bind
else:
    HOST = "0.0.0.0"
print("[*] Bind Address: {}".format(HOST))

# Parse User Agent
if args.useragent:
    UA = args.useragent
else:
    UA = "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
print("[*] User Agent: {}".format(UA))
headers = {'User-Agent': str(UA)}

# Listens for connect back from PHP script
def lPort(PORT):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((str(HOST),int(PORT)))

    try:
        s.settimeout(1)
        s.listen(1)
        (conn, (ip,port)) = s.accept()
        print("[+] Outbound [Allowed] @ Port: {}".format(str(PORT)))

    except socket.timeout:
        print("[-] Outbound [Blocked] @ Port: {}".format(str(PORT)))
    except Exception as e:
        print("[!!!] Error: {}".format(str(e)))

# For each port listen for connect back from PHP script and request PHP script
def main():
    if MODE == "l":
        try:
            f = open(LISTPATH,"r")
            for port in f:
                URLtmp = str(URL + "?p=" + str(port))
                t1 = threading.Thread(target=lPort,args=(port,))
                t1.start()
                requests.get(URLtmp,headers=headers)
                t1.join()
        except Exception as e:
            sys.exit("[!] Error: {}".format(e))
    elif MODE == "c":
        for port in commonPorts:
            URLtmp = str(URL + "?p=" + str(port))
            t1 = threading.Thread(target=lPort,args=(port,))
            t1.start()
            requests.get(URLtmp,headers=headers)
            t1.join()
    elif MODE == "a":
        for port in range(0,65536):
            URLtmp = str(URL + "?p=" + str(port))
            t1 = threading.Thread(target=lPort,args=(port,))
            t1.start()
            requests.get(URLtmp,headers=headers)
            t1.join()
        
if __name__ == '__main__':
    if (len(sys.argv) < 2):
        sys.exit("usage: use -h for help")
    else:
        main()
        print("[*] Finished")
