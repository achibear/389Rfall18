Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Mingda Guo
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mingda Guo

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. whois

2. "laz0 rh4x", "c0uc hpot4doz"

3. 104.248.224.85, 206.189.113.189. They connect from port 33794 and 53878.

4. 2749

5. It is going to happen tomorrow 15:00

6. They send update plan via google drive https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. they will met tomorrow


### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. 10/25/2018 at 12:40am(UTC)

2. laz0rh4x

3. 9. There are actually 11 sections

4. 
sec 1(ASCII text): Call this number to get your flag: (422) 537 - 7946
sec 2(Array of words): 314159265358979
sec 3(Coord): (123,49),(148,19),(237,126),(67,64),(61,213),(33,55),(195,65),(83,192)
sec 4(reference): 1
sec 5(ASCII text): The imfamous security pr0s at CMSC389R will never find this!

sec 6(ASCII text): The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

sec 7(coord): (24,97),(229,43),(220,126),(67,64),(99,137),(189,6),(179,59),(83,192)

sec 8(PNG): CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}

sec 9(ASCII text): AF(saSAdf1AD)Snz**asd1

sec 10(ASCII text): Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9

sec 11(array of dword): 408015160230420



5.
CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}

After decode sec10 data using base64, got:CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}

