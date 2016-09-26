---
layout: course_page
title: schedule
permalink: /535/schedule/
parent_course: 535
---

**Fall 2016 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6)

---

{:.green}
### 2016-09-26 Week 6 

#### Readings

[Rijndael flash animation](http://www.formaestudio.com/rijndaelinspector/archivos/Rijndael_Animation_v4_eng.swf)

[About AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

[About Rjindael s-box](https://en.wikipedia.org/wiki/Rijndael_S-box)

[About the s-box](http://crypto.stackexchange.com/questions/10996/how-are-the-aes-s-boxes-calculated)

*Cryptography* A more clearly written overview ==> [tanenbaum-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networks-5ed-tanenbaum-chapter-8.pdf)

*Cryptography* Another more clearly written overview ==> [kurose-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)

#### Topics

- RSA - asymetric ciphers
- Digital Signatures
- Secure Hash functions (SHA)


---

{:.gray}
### 2016-09-19 Week 5 

> [Homework 8 assigned](/535/hw8/)

#### Readings

[Rijndael flash animation](http://www.formaestudio.com/rijndaelinspector/archivos/Rijndael_Animation_v4_eng.swf)

[About AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

[About Rjindael s-box](https://en.wikipedia.org/wiki/Rijndael_S-box)

[About the s-box](http://crypto.stackexchange.com/questions/10996/how-are-the-aes-s-boxes-calculated)

*Cryptography* A more clearly written overview ==> [tanenbaum-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networks-5ed-tanenbaum-chapter-8.pdf)

*Cryptography* Another more clearly written overview ==> [kurose-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)

#### Topics
* *techniques*: bit shifting, rotatations, XOR
* symetric key encryption: block cipher ==> AES
* SHA
* RSA
	* PKI - public key infrastructure


---


{:.gray}
### 2016-09-12 Week 4 

> [Homework 7 assigned](/535/hw7/)

#### Readings

*Cryptography* A more clearly written overview ==> [tanenbaum-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networks-5ed-tanenbaum-chapter-8.pdf)

*Cryptography* Another more clearly written overview ==> [kurose-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)

*Cryptography* ==> [brooks-chapter-3.pdf]({{ site.baseurl }}assets/cs535/brooks-chapter-3.pdf)


#### Topics
* *techniques*: 
	- system command wrappers in python ```subprocess``` or ```envoy```
	- remote shells? 
* cryptography == making codes cryptanalysis == breaking codes
* monoalphabetic, polyalphabetic cipher
* symmetric key encryption
	- block chaining 
	- DES, AES
* public key cryptography
	- RSA

---

{:.gray}
### 2016-09-07 Week 3


> [Homework 6 assigned](/535/hw6/)

#### Topics
* ransomware and network access techniques: remote shell commands?
* basic cryptanalysis
* resources for cryptanalysis
	- you know the encryption method
	- you know the encryption key
	- you possess the ciphertext
	- you possess the cleartext

---

{:.gray}
### 2016-08-29 Week 2

**READING** ==> [subprocess package](https://docs.python.org/2/library/subprocess.html), [file I/O](https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)

[Homework 4 assigned](/535/hw4/)

{:.yellow} 
[Homework 5 assigned](/535/hw5/)

#### Topics
* Python review
	- tuples, slices, and loops, dictionaries
* Python
	- ```subprocess``` package, file i/o
* Simple networking with Python
* Simple substitution cipher
* Ransomware and network access techniques: remote shell commands?

---

{:.gray}
### 2016-08-22 Week 1

**READING** ==> Sections 1 through 5 in [SANDIA-98: A Common Language for Computer Security Incidents](http://prod.sandia.gov/techlib/access-control.cgi/1998/988667.pdf)

- [Homework 1](/535/hw1/) discussion
- [Homework 2 assigned](/535/hw2/)
- [Homework 3 assigned](/535/hw3/)

#### Topics

* What we mean by cyber security
* Taxonomy of Attacks (vulnerabilites, attacks, persistent threats)
* A framework for cybersecurity analysis

#### Attributes of Secure Systems

- Confidentiality ==> data privacy ensured (not public information)
- Authentication ==> authenticity of ownership ensured
- Integrity - information is immutable to those not authorized to change it
- Non-repudiation ==> neither sender nor receiver can deny that they performed a transaction
- Access control ==> access to information is controlled and limited to authorized parties
- Availability ==> protected and secure assets and information should remain available as needed (by authorized parties of course!)

```attack surface``` (how many components and to what degree can an attacker touch a system?) 

Examples: open sockets, open pipes, open rpc, number of services, web server scripts, accounts with elevated creds, percentage of file system with weak access controls

#### Major Threads in Vulnerability and Incidents

- Is it in the ```Design```, ```Implementation```, or ```Configuration``` of systems ... or is it all three?

#### Other ways of assessing vulnerability

- Social Engineering ==> the human problem in cyber attacks. Nigerian 419 scams, spam, phishing, pharming, spear-phishing, mules
- Authentication/Authorization
- Access permissions (file systems, etc..)
- Audits
- User Interface weaknesses

#### A Common Language for Computer Security Incidents

* class discussion

---

### 2016-09-05 Week 3
#### Topics
* Cryptology
* SSL/TLS


[comment]:### 2016-09-19 Week 5 
[comment]:### 2016-09-26 Week 6 
[comment]:### 2016-10-03 Week 7
[comment]:### 2016-10-10 Week 8 
[comment]:### 2016-10-24 Week 9
[comment]:### 2016-10-31 Week 10 
[comment]:### 2016-11-07 Week 11
[comment]:### 2016-11-14 Week 12
[comment]:### 2016-11-21 Week 13
[comment]:### 2016-11-28 Week 14

 



