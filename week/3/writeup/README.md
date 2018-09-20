Writeup 3 - OSINT II, OpSec and RE
======

Name: Mingda Guo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mingda Guo

## Assignment 3 Writeup

### Part 1 (100 pts)
1. The first vulnerability is the opening port. I think it is wise to close the port if you don't need to use it. And if you must open some port, at least filter the packet using some techniques like firewall. So attacker can not easily scan the port and get useful information from it.

2. The second vulnerability is the leaking information caused by robot.txt. Attcker can easily access robot.txt and see there is a secret page. So according to https://webmasters.stackexchange.com/questions/9197/disallow-robots-txt-from-being-accessed-in-a-browser-but-still-accessible-by-spi, it is better to not put secret page into robot.txt. And if you want to hide them from crawling, just use password to protect the page.

3. The last vulnerability is the weak username and password. Since he posts his name, social media and email username puiblicly, he should pick something that unrelated to those as admin username. he should also build a more strcit password rule including longer length and more character combinations. And in order to make brute force completely useless,maybe he can even require multi-way authentication like we need to enter the number from our phone to login to ELMS.
