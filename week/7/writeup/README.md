Writeup 7 - Forensics I
======

Name: Mingda Guo	
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mingda Guo

## Assignment 7 writeup

### Part 1 (40 pts)

1. This is a image file with tpe JPEG.

2. Illinois, Chicago, Arbor Center For Eye Care

3. 2018.08.22 16:33:24.00(GPS) and 11:33:24(local)

4. iphone8 back camera 3.99mm

5. 539.537

6.CMSC389R-{look_I_f0und_a_str1ng}

### Part 2 (55 pts)

In this task, I first run the binary file and saw nothing but "where is your flag". So I decided to use Cutter to look its assembly code. From the assembly, I saw this file wrote things to "/tmp/.stego". But when I entered this directory, I didn't find this file. So I went back to assembly and tried to manually go over assembly code. 

After getting lost in those assembly registers and function calls, I started to wonder what the dot means before stego. So I googled and realized it mean hidden file. So I revealed the file and saw it was JPEG like file by using exiftool. But when I tried to open the file using image viewer, I failed. So looked the file type agian and see it's JFIF format. 

Then I searched the header format for JFIF and got 0xff-d8. So I ran "xxd stego" and saw it started with 00ffd8. I realized the extra "00" is the reason that caused problem. But I had no idea what to do at that point. So I did more searching on google and tried to find a way to delete the first bit. 

At last, I found out that I can use "dd bs=1c skip=1" to skip the first bit. Then I got a file that can be opened by image viewer. I opened it and saw a yellow stegosaurus. Therefore I used "steghide info" to view the file with password "stegosaurus" and saw a embedded file named "flag". I extract the file and got the flag: CMSC389R-{dropping_files_is_fun}
