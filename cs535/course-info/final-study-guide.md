---
layout: course_page
title: Final Exam Study Guide
permalink: /535/final-study-guide/
parent_course: 535
---

## Overview
The final exam will be given online in D2L. This is an open book exam.

### Relevant Reading:

**GENERAL**

[tanenbaum-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networks-5ed-tanenbaum-chapter-8.pdf)

[kurose-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)

Hacking 2nd Ed. (chapter 3)

Black Hat Python (chapters 4 and 5)

**AES**

[Rijndael flash animation on AES](http://www.formaestudio.com/rijndaelinspector/archivos/Rijndael_Animation_v4_eng.swf)

[About AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)


### Topics

[WEEK 1](http://rmedinahu.github.io/535/schedule/#week-1)

- attack surface (note the various areas of vulnerabilities)
- attack vector
- attributes of secure systems (be able to name and describe)

[WEEK 3](http://rmedinahu.github.io/535/schedule/#week-3)

- ransomware attack: what is it and what is an example attack vector?
- cryptanalysis
- caesar cipher: why is it weak and how is it analyzed?

[WEEK 4](http://rmedinahu.github.io/535/schedule/#week-4) 
[WEEK 5](http://rmedinahu.github.io/535/schedule/#week-5) 
[WEEK 6](http://rmedinahu.github.io/535/schedule/#week-6)
[WEEK 7](http://rmedinahu.github.io/535/schedule/#week-7)
[WEEK 8](http://rmedinahu.github.io/535/schedule/#week-8)

- block cipher
- symetric vs asymetric key encryption
- AES standard: 
	- understand the basic cryptographic premise underlying the algorithm
	- understand why it is considered secure
- SHA
- RSA / PKI
- digital signatures: what is it and what are components
- secure hash functions
- SSL/TLS and secure network communication

VULNERABILITIES:

**Vulnerabilities: In Software**

- what are common attack vectors?
- code injection
	- buffer overflow attack
	- format string attack
- ```GDB```: understand how we can use to analyze the stack
- stack, stack frames and relation to buffer overflow attacks

**Vulnerabilities: In NETWORKS**

- what are common attack vectors?
- ARP poisoning
	- Man in the middle atatck
- packet sniffing

**Vulnerabilities: In WEB APPLICATIONS**

- what are common attack vectors?
- exposed installation and configuration files
- sql injection
- brute force attack on directories
- brute force attack on html forms 