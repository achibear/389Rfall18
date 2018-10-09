Writeup 5 - Binaries I
======

Name: Mingda Guo
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mingda Guo

## Assignment 5 Write up

Since I did the At@t style in CMSC216, I incorrectly mixed it with Intel style at first when writing the program. After revising my code, I encountered a weried problem.

The output of my code are "Hello zzzzz" and "Hello Hello World!". It looks like that my code inserted the character and copied the string correctly but didn't provide correct output length. I decided to use gdb to check this problem. However, I can not run each instruction individually at first. The break and step seems not working. So at that point, I could only see that the loop iterate correct times.

Then I restarted the machine, and the break and step command worked. By using those command, I found out that string pointers were pointing to the correct address which are "0x7fffffffe186" and "0x7fffffffe159".However, after execute instruction line by line, I realized that my_memset insert a lot of "/000" after those "z" so that the "!" had been overwritten. my_strncpy function also left extra information after the copying.

Next, I used the rest of my day trying to figure out the problem. But everything I tried failed. For example, I tried to use decompiler to check instructions. I tried to specify how many bytes are transfering by using "ptr byte []" as presented in slide. But it gave me the "invalid size for operand" error. I also tried "byte []" and other byte numbers. But all gave me "invalid size for operand". At last, I tried to read the X86-64 intel manul and didn't get useful information as well. 

At this point, I have to give up and prepare for other exams.
 


