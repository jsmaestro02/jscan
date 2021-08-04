# jscan
A simple script for scanning for open ports and their services

# How to user it
`$ ./jscan.py -h`
for help

`$ ./jscan.py hostname` or `$ ./jscan.py ip`
for scanning the target

`$ ./jscan.py target -p port-option`
-p determines the ports to scan. You can use 'a' for all of the ports(1-65535) or 'd' for well-known ports like 21, 23, 22, 80, 443 ... . You also can use a range with this format "start-end" or you can specify few ports separated by commas. The default option is d.
`$ ./jscan.py target -p a`
`$ ./jscan.py target -p 2-45`
`$ ./jscan.py target -p 32,21,445`

# Disclaimer: Do not use this tool on the hosts you're not allowed to and illegal attacks.

