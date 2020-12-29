#!/usr/bin/env python3
import sys

user="User"
ip="IP"
algo="Algorithm"
host="Host"
cipher="Cipher"
   
iname="#"
i=0
print("-"*115)
print(f"|{iname:^3}|{user:^19}|{ip:^16}|{algo:^20}|{host:^20}|{cipher:^30}|")
print("-"*115)

user="undefined"
ip="undefined"
algo="undefined"
host="undefined"
cipher="undefined"

try:
    file=open(sys.argv[1],"r")
except:
    print("File not found.")
    sys.exit()
for line in file:
    if(line.find("debug1: kex")>0):
        list=line.split()
        if(list[7]=="algorithm:"):
            algo=list[8]
        elif(list[7]=="host"):
            host=list[10]
        elif(list[8]=="cipher:"):
            cipher=list[9]
    if(line.find("Accepted password")>0):
            list=line.split()
            user=list[8]
            ip=list[10]
            print(f"|{i:>3}|{user:<19}|{ip:<16}|{algo:<20}|{host:<20}|{cipher:<30}|")
            user="undefined"
            ip="undefined"
            algo="undefined"
            host="undefined"
            cipher="undefined"
            i=i+1
file.close()
print("-"*115)