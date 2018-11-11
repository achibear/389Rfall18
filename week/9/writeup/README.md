Writeup 9 - Crypto I
=====

Name: Mingda Guo
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mingda Guo

## Assignment 9 Writeup

### Part 1 (60 Pts)
In this part, I wrote loops to hash each line in the password file with each salt. And then compare the result to the hash values in hash file. However, when I first run it, I can not find match result. So I tried to debug it and found out that I forget to delete the newline character after reading hash from hash faile. So I used strip() function to delete it and found a match.

But I was only able to find one match at that point. Although I felt there should be more than one match, the program seems correct. So I continued to part2. After finished part2, I suddenly realized that I forgot to put strip() function in the last loop so that only the first try had newline character removed. So I added that in the loop and found 4 matches:

-------SUCCESS------
salt: k
password: neptune

-------SUCCESS------
salt: m
password: jordan

-------SUCCESS------
salt: p
password: pizza

-------SUCCESS------
salt: u
password: loveyou


### Part 2 (40 Pts)

For this part, I first use the socket send and receive function to communicate with 142.93.117.193 and port 7331. Then I see the server is asking me the hash values. So I write code to first slice the target string from received data. Then hash that string and send it to the server.

However, I got some problems at that point. I found out that my hash output is different than the expected value. After some testing, I saw that my string is in byte format. So I was trying to decode it to normal string. This didn't help much since the hash function requires encoded object. Then I realized that maybe the string I hashed contains newline character. So I used strip() to delete it and get the correct value.

Next, I saw that the server is asking more hash values. So I wrote an extra loop to keep hash and send until there is no "Find me..." in returned data. By running the program, I saw the flag CMSC389R-{H4sh-5l!ngInG-h@sH3r}.

