#!/bin/python3

import argparse
import socket
import sys 

def main():
    ports_help = "Specify the port/ports:1) a for all of the ports. 2)d for prominant ports. 3)specify a range like 2-56. 4)specify few ports separated by comma"

    parser = argparse.ArgumentParser()
    
    parser.add_argument("target", help="Specify the target/targets")
    parser.add_argument("-p", "--port", help=ports_help, default="d")

    args = parser.parse_args()

    ports =  portGen(args.port)  
    portScan(args.target, ports)

def portGen(option):
    if option == "d":
        ports = [21, 22, 23, 25, 53, 80, 110, 123, 143, 161, 194, 443]
    
    elif any(map(str.isdigit, option)):
        if isdash(option):
            bounds = list(map(int, option.split("-")))
            ports = [*range(bounds[0], bounds[1]+1)]

    elif option.lower() == "a":
        ports = [*range(1, 65536)]

            
    else:
        print("Unknown option for ports")
        return 0

    return ports


def isdash(string):
    for x in string:
        if x == "-":
            return True
    return False


def portScan(target, ports):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        result = s.connect_ex((target, port))
        if not result:
            try:
                port_name = socket.getservbyport(port)
            except:
                port_name = ""
            print(f"port {port} is open: {port_name}")
        s.close()


if __name__ == '__main__':
    main()
