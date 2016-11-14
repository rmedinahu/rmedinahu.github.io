---
layout: course_page
title: schedule
permalink: /535/schedule/
parent_course: 535
---

**Fall 2016 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6), [7](#week-7), [8](#week-8), [9](#week-9), [10](#week-10), [11](#week-11), [12](#week-12)

---


{:.green}
### 2016-11-14 Week 12 

#### Readings

> *Black Hat Python*  ==> [Chapter 4](https://www.nostarch.com/blackhatpython)


#### Topics
- network based attacks (ARP poisoning and packet sniffing)
- case study: HTML input forms


---


{:.gray}
### 2016-11-07 Week 11 

#### Readings

> *Vulnerability Overview*  ==> [Sections 9.7 -> 9.9 (p.639-684)]({{ site.baseurl }}assets/cs535/modern-operating-systems-4ed-tanenbaum-chapter-9.pdf)
> *Black Hat Python*  ==> [Chapter 4](https://www.nostarch.com/blackhatpython)


#### Topics
- Trojan Horses, Viruses, Worms, Spyware, and Rootkits ... *OH MY!*

---

{:.gray}
### 2016-10-31 Week 10 

#### Readings

> *Vulnerability Overview*  ==> [Sections 9.7 -> 9.9 (p.639-684)]({{ site.baseurl }}assets/cs535/modern-operating-systems-4ed-tanenbaum-chapter-9.pdf)

- Trojan Horses, Viruses, Worms, Spyware, and Rootkits ... *OH MY!*

#### Topics
- vulnerabilities
- case study: HTML input forms
- Kali Linux 

{% highlight c %}
	#include <stdio.h>
	#include <string.h>

	void vulnerable() {
		char s[100], g[100] = "Hello ";
		gets(s);
		strcat(g, s);
		printf(g);
	}

	int main(int argc, char *argv[]) {
		char creeper[128];
		int innocent = 99;
		
		printf("BEFORE innocent=%d \n", innocent);
		gets(creeper);
		printf(creeper);
		printf("\nAFTER innocent=%d \n", innocent);
		
		// vulnerable();
	}
{% endhighlight c %}

{% highlight c %}
#include <stdio.h> 
#include <string.h>
int main(int argc, char *argv[]) { 
	int value = 5;
	char buffer_one[8], buffer_two[8];
	strcpy(buffer_one, "one"); /* Put "one" into buffer_one. */ 
	strcpy(buffer_two, "two"); /* Put "two" into buffer_two. */
	printf("[BEFORE] buffer_two is at %p and contains \'%s\'\n", buffer_two, buffer_two); 
	printf("[BEFORE] buffer_one is at %p and contains \'%s\'\n", buffer_one, buffer_one); 
	printf("[BEFORE] value is at %p and is %d (0x%08x)\n", &value, value, value);
	printf("\n[STRCPY] copying %d bytes into buffer_two\n\n", strlen(argv[1])); 
	strcpy(buffer_two, argv[1]); /* Copy first argument into buffer_two. */
	printf("[AFTER] buffer_two is at %p and contains \'%s\'\n", buffer_two, buffer_two); 
	printf("[AFTER] buffer_one is at %p and contains \'%s\'\n", buffer_one, buffer_one); 
	printf("[AFTER] value is at %p and is %d (0x%08x)\n", &value, value, value);
}
{% endhighlight c %}


---

{:.green}
### 2016-10-17 Week 9 

#### Readings

> Please read the following prior to Monday, October 24: 

> *Vulnerability Overview*  ==> [Sections 9.7 -> 9.9 (p.639-684)]({{ site.baseurl }}assets/cs535/modern-operating-systems-4ed-tanenbaum-chapter-9.pdf)



#### Topics

- Vulnerabilities

---

{:.gray}
### 2016-10-10 Week 8 

> [Midterm assigned](/535/midterm/)

#### Readings

*Network Security (Sections 8.3 & 8.6) ==> [kurose-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)


#### Topics

- SSL/TLS - Basics of Secure Network Communication
- Midterm reports

---


{:.gray}
### 2016-10-03 Week 7 


#### Readings

*Cryptography* A more clearly written overview ==> [tanenbaum-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networks-5ed-tanenbaum-chapter-8.pdf)

*Cryptography* Another more clearly written overview ==> [kurose-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)

#### Topics

- asymetric ciphers (Diffie-Hellman, RSA)
- Digital Signatures
- Secure Hash functions (SHA, MD5)

---

{:.gray}
### 2016-09-26 Week 6 

> [Homework 9 assigned](/535/hw9/)

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


 
[comment]:### 2016-11-14 Week 12SSL insecurity - heartbleed. poodle.
[comment]:### 2016-11-21 Week 13
[comment]:### 2016-11-28 Week 14

 



