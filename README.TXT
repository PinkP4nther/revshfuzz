# revshfuzz
A tool for fuzzing for ports that allow outgoing connections

I recommend stopping all listening services as they could interfere with the binding in the script!

1 - Upload pd.php to target webserver
2 - sudo python revshfuzz.py http://target/pd.php

[user][D3V][revshfuzz]> sudo python revshfuzz.py http://127.0.0.1/pd.php
[sudo] password for user: 
[+] Port: 20 Allowed
[+] Port: 21 Allowed
[+] Port: 22 Allowed
[+] Port: 23 Allowed
[+] Port: 25 Blocked
[+] Port: 53 Allowed
[+] Port: 80 Allowed
[+] Port: 81 Allowed
[+] Port: 110 Blocked
[+] Port: 139 Blocked
[+] Port: 143 Blocked
[+] Port: 443 Allowed
[+] Port: 445 Allowed
[+] Port: 465 Allowed
[+] Port: 587 Allowed
[+] Port: 993 Allowed
[+] Port: 995 Allowed
[+] Port: 2222 Allowed
[+] Port: 3306 Allowed
[+] Port: 8000 Allowed
[+] Port: 8080 Allowed
[+] Port: 8181 Allowed
[+] Port: 8443 Allowed
[+] Port: 9050 Allowed
[+] Finished
