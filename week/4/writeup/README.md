Writeup 3 - Pentesting I
======

Name: Mingda Guo
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mingda Guo

## Assignment 4 Writeup

### Part 1 (45 pts)
The first thing I tried is to find the place to inject command. By using "nc cornerstoneairlines.co 45", I found out there is a place to enter ip address. Thus I entered the address with the command "142.93.117.193; ls /". At the end of returning message, I saw there were system directories. So I know I found the right place to inject code. Next, I was trying to get the shell because I felt it is too inconvience to check each directories mannully. I googled and tried to bind the shell which didn't work. And I also tried to reversly connect server to my machine which was also failed. Thus I have to check files by hand. I used "ls /home/" and saw there is a file called flag.txt. Finally, I used "cat /home/flag.txt" and got the flag CMSC389R-{p1ng_as_a_$erv1c3}.

Then I was trying to find the script that the server uses. I tried to dicover every directories that were listed by using "ls" command. Then, I found out that there is a script called "container_startup.sh" under the "opt" directory. So I "cat" it and found out that this script was used to get input from user and echo corresponding output. Since the code will run whatever input it gets, the suggestion for Fred is to escape characters like ';'. By doing so, if people try to inject code, the server will only treat their code as normal string rather than code that needs to be run.

### Part 2 (55 pts)
For this part, the first thing I was tring to do is to implement things I did in part 1. I copied socket sending and receiving code from assignment2 and sent a simple test command. I got the expected return message so that I know my code is on the right track. Then I add more functionalities to the program to perform iteraction with user input. However, at this point, I met the problem that the "pull" option was not always working properly. Sometimes it won't return the file I want. After serveral possible solutions, I thought maybe it was because of the size of my recv() is not big enough. So the output of second command may be dropped occasionally. So I changed 1024 to 4096 and the problem was solved.

Next, I realized that I need to split the string returned in order to generate correct output to screen or my local file. This step costs me a lot of time. I tried to write my own substring method and it didn't work as I expected even after several fixes and changes. So I searched goole and didn't found a good method until I realized that the split() function can not only splite string by character but also by string. So I used "echo ENDPOINT; " command to insert "ENDPOINT" to the return message and used plit("ENDPOINT ") to parse the string. 
