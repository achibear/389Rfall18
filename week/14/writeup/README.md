Writeup 10 - Crypto II
=====

Name: Mingda Guo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mingda Guo

## Assignment 10 Writeup

### Part 1 (70 Pts)
At first, I saw there was a about page that gave "cornerstoneairlines.co:8080/about". So I was wondering if there exists a flag page. By typing "cornerstoneairlines.co:8080/flag", it gave error meesage saying Sinatra doesn't know this file. 

Then, inspired by Sinatra, I thought I can use injection in the slides. I saw that there were item ids associated with items. So I tried to use "cornerstoneairlines.co:8080/item?id=0' or '1'='1' --" which didn't work. I also tried to change "1=1" to "true" but it solved nothing.

Next, I noticed that the webpage automacally change the space and ' to %20 and %27. So I typed "http://cornerstoneairlines.co:8080/item?id=0%27%20or%20true%20--%20" and it listed all items as I wanted.

Therefore I found the flag CMSC38R-{y0U-are_the_5ql_n1nja}.

### Part 2 (30 Pts)

1. The first one wants me to pop a alert. So I added "?query=<script>alert()</script>" after the url.

2. In this part, simply enter javascript code doesn't work. Since I can see that the source code doesn't escape html code, so I tried to google how to invoker javascript in html code. However, didn't find useful resources. So I opened the hint and saw that I can use image and onerror. So I typed <img src="" onerror="alert()"></img> in the post and it worked.

3. Since it mentioned about url, I found this html code is suspicous: https://xss-game.appspot.com/level3/frame#9'%20onerror='alert()'. Thus after I entered https://xss-game.appspot.com/level3/frame#1'%20onerror='alert()' to url bar, it worked.

4. When I created a timer, I saw this url: https://xss-game.appspot.com/level4/frame?timer=3. From the hint, I examine the timer.html and found that I can use '); alert(' to perform attack.

5. From the hints, I saw the parameter 'next' in source code is vulnerable such that after I place javascript:alert() in the url, the alert will pop up.

6. Since this challenge mentioned about external js file, I first googled the js file that pop up alert and found https://gist.github.com/ndob/a.js. However, when I added this link to the end of url, it says unable to load url containning "http". So I deleted the https part and it said the script was loaded but no alert pop up. So I checkred hints and saw it suggested using google.com/jsapi?callback=foo. After examine its ouput, I changed foo to alert and it worked.


