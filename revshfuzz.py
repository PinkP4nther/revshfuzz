#
# Weak Firewall Rule Discovery Tool
# By @Pink_P4nther
# This tool can help discover allowed outgoing connections
#

import socket
import sys
import requests
import threading
import select

#socket.setdefaulttimeout(2)
#print(str(socket.getdefaulttimeout()))

# VARIABLES
commonPorts = [0,20,21,22,23,25,53,80,81,110,139,143,443,445,465,587,993,995,2222,3306,8000,8080,8181,8443,9050]
if len(sys.argv) >= 2:
    URL = str(sys.argv[1])
HOST = "0.0.0.0"
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
headers = {'User-Agent': str(UA)}

# Listens for connect back from PHP script
def lPort(PORT):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((str(HOST),PORT))

    try:
        s.settimeout(1)
        s.listen(1)
        (conn, (ip,port)) = s.accept()
        print("[+] Port: {} Allowed".format(str(PORT)))

    except socket.timeout:
        print("[-] Port: {} Blocked".format(str(PORT)))
    except Exception as e:
        print("[!!!] Error: {}".format(str(e)))

# For each port listen for connect back from PHP script and request PHP script
def main():
    for port in commonPorts:
        URLtmp = str(URL + "?p=" + str(port))
        t1 = threading.Thread(target=lPort,args=(port,))
        t1.start()
        requests.get(URLtmp,headers=headers)
        t1.join()
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <http://URL/pd.php>".format(sys.argv[0]))
    else:
        main()
        print("[+] Finished")
