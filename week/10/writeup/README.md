Writeup 10 - Crypto II
=====

Name: Mingda Guo
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mingda Guo

## Assignment 10 Writeup

### Part 1 (70 Pts)
For the first part, I first connec to the server using python socket. Then I saw there are options listed. So I sent '1' to the server. Follow its response, I sent my message "fall18" and got its hash.

On the next step, I sent '2' fisrt and saw that the server was asking hash and data. Then I was trying to calculate the correct padding. I started the secret from 6 bytes. Since my message is 6 bytes and the end is 6 bytes, I got 64-12-8 = 44. So I created '\x80' and 43 '\x00' following secret + message. And changed the length byte to '\x60'.

However, after sending those data, the server said that the hash is not correct. So I tried to increase secret length until it reached 10. And the flag I got is CMSC389R-{i_still_put_the_M_between_the_DV}.

### Part 2 (30 Pts)

1. generating keys: gpg --gen-key then input the name and email address

2. import public key: gpg --import public.asc

3. encrypting message: gpg --output message.private --encrypt --recipient email@email.com message

