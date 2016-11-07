---
layout: course_page
title: schedule
permalink: /350/schedule/
parent_course: 350
---

**Fall 2016 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6), [7](#week-7), [8](#week-8), [9](#week-9), [10](#week-10), [11](#week-11), [12](#week-12)

---

{:.green}
### 2016-11-07 Week 12 

#### Readings

- Network basics - [A Day in the Life...]({{ site.baseurl }}assets/
a-day-in-the-life-of-a-web-request.pptx)

#### Topics
- Kali linux
- Network basics
- Network vulnerabilities
	* ARP poisoning
	* Man in the middle atatck
- Packet sniffing


---


{:.gray}
### 2016-10-31 Week 11 

#### Readings

> *Vulnerability Overview*  ==> [Sections 9.7 -> 9.9 (p.639-684)]({{ site.baseurl }}assets/cs535/modern-operating-systems-4ed-tanenbaum-chapter-9.pdf)


#### Topics
- Kali linux
- buffer overflows
- GDB buffer overflow simulation


---


{:.gray}
### 2016-10-24 Week 10 

#### Readings

> *Vulnerability Overview*  ==> [Sections 9.7 -> 9.9 (p.639-684)]({{ site.baseurl }}assets/cs535/modern-operating-systems-4ed-tanenbaum-chapter-9.pdf)


#### Topics
- Kali linux
- buffer overflows

---

{:.gray}
### 2016-10-17 Week 9 

>[Homework 7 assigned](/350/hw7)

#### Readings

> Please read the following prior to Monday, October 24: 

> *Vulnerability Overview*  ==> [Sections 9.7 -> 9.9 (p.639-684)]({{ site.baseurl }}assets/cs535/modern-operating-systems-4ed-tanenbaum-chapter-9.pdf)


#### Topics

- Vulnerabilities

---

{:.gray}
### 2016-10-10 Week 8 

#### Readings

> Midterm project work.


#### Topics

- Digtial signatures


---

{:.gray}
### 2016-10-03 Week 7 

>[Homework 6 assigned](/350/hw6)

>[Midterm project assigned](/350/midterm)

#### Readings

[Sections 8.2.2 and 8.3]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)

#### Topics
- review cipher block encryption
- RSA - asymetric ciphers
- Digital Signatures and Hashes
- Secure Hash functions
- PKI (public key infrastructure)

---

{:.gray}
### 2016-09-26 Week 6 

#### Readings

[Sections 8.2.2 and 8.3]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)

#### Topics
- bit shifting and manipulations (our print bits function)
- RSA - asymetric ciphers
- Digital Signatures
- Secure Hash functions


---


{:.gray}
### 2016-09-19 Week 5 

#### Readings

[Rijndael flash animation](http://www.formaestudio.com/rijndaelinspector/archivos/Rijndael_Animation_v4_eng.swf)

[About AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

[About Rjindael s-box](https://en.wikipedia.org/wiki/Rijndael_S-box)

[About the s-box](http://crypto.stackexchange.com/questions/10996/how-are-the-aes-s-boxes-calculated)

*Cryptography* A more clearly written overview ==> [tanenbaum-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networks-5ed-tanenbaum-chapter-8.pdf)

*Cryptography* Another more clearly written overview ==> [kurose-chapter-8.pdf]({{ site.baseurl }}assets/cs535/computer-networking-6ed-kurose-etal-chapter-8.pdf)

#### Topics
* *techniques*: python bit shifting, rotatations, XOR
* symetric key encryption
* block ciphers (DES, AES)


---


{:.gray}
### 2016-09-12 Week 4 

#### Readings

[Python virtualenv for isoloating python environments](https://virtualenv.pypa.io/en/stable/)

[Python virtualenvwrapper for simpler virtualenvs](https://virtualenvwrapper.readthedocs.io/en/latest/)

[Python subprocess for spawning child processes](https://docs.python.org/2/library/subprocess.html)

[comment]:[The Magic of XOR](https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/BitOp/xor.html)

#### Topics

* Python virtual environments
* Python shell simulation
	- {:.yellow} ==> *shell injection* ALERT!
* more socket programming
* cryptanalysis: cracking the code


---

{:.gray}
#### 2016-09-07 Week 3

**READINGS** 

[Python socket library](https://docs.python.org/2/library/socket.html)

#### Topics

* Ransomware attacks
* socket programming and client/server networking



{% highlight python %}
"""Simple server application"""

import socket

#  server host (local machine)
host = 'localhost' 

#  machine port
port = 7000

#  CONNECTION tuple
conn = (host, port)

#  number of requests before need to thread...
backlog = 5

#  max length of data buffer (bytes) 
size = 1024

#  create a socket object. AF_INET = ipv4 addressing  SOCK_STREAM = transport protocol (tcp)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#  force server to release socket immediately if killed
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

#  bind the socket to connection
s.bind(conn) 

#  listen for events on the socket
s.listen(backlog)

#  poll for incoming connections then send response
while 1:
    print 'Server ready, willing and able!'

    # waits for connection then returns a tuple representing socket connection object
    client, address = s.accept()
 
    # reads in the payload sent by a client
    data = client.recv(size) 
    
    if data: 
        print 'Client at ', address[0], 'sent ==> ', data
        
        #  send a message back to the client
        client.send('Thanks for the info!')

    client.close() # close the connection with client
{% endhighlight %}


{% highlight python %}
"""Simple client application"""

import socket

#  server host (local machine)
host = 'localhost' 

#  machine port
port = 7000

#  server info as tuple
SERVER = (host, port)

#  max length of data buffer (bytes) 
size = 1024

#  create a socket AF_INET = ipv4 addressing SOCK_STREAM = transport protocol (tcp)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to a server 
s.connect(SERVER)

# send data to server 
s.send('now is the time for all ...')

# wait for/read in response from server
data = s.recv(size) 

# what'd we get?
print '\nServer RESPONSE:\n> ', data

# close connection
s.close()

{% endhighlight %}


---


{:.gray}
#### 2016-08-29 Week 2
**READINGS** 

[Python data structures](https://docs.python.org/2/tutorial/datastructures.html)

#### Topics
* Python review ```type()```, ```str()```, etc...
	- data types, type casting
* Python review ```mylist[]```, ```mylist()```, ```mylist{}```, ```range(100)```
	- *vectors*: lists, tuples, dictionaries, slices, loops
* Simple frequence analysis
* Dictionary lookups
* List comprehensions allow you to concisely and clearly specify the following.

	{% highlight python %}
	evens = []
		for i in range(10):
			if i % 2 == 0:
				evens.append(i)

	#comprehension shortens the above to:

	evens = [i for i in range(10) if i%2 == 0]
	{% endhighlight python %}


* Random numbers


{% highlight python %}
	import random
	# Generate a random between 0 and 10 inclusive
	random_int = random.randint(0, 10)

	# Use a list comprehension to generate a thousand random integers between 0 and 10 inclusive.
	rands = [random.randint(0, 10) for i in range(1000)]
{% endhighlight python %}


* Rotations and cycles
* Simple substitution ciphers

---

{:.gray}
#### 2016-08-22 Week 1

**READINGS**

1. Sections 1 through 5 in [SANDIA-98: A Common Language for Computer Security Incidents (pdf)](http://prod.sandia.gov/techlib/access-control.cgi/1998/988667.pdf)
2. [Panama Papers Data Breach](https://www.theguardian.com/news/2016/apr/03/what-you-need-to-know-about-the-panama-papers)

#### Topics

* What do we mean by cyber security?
* Case study: Web application vulnerability?

#### Attributes of Secure Systems

- Confidentiality ==> data privacy ensured (not public information)
- Authentication ==> authenticity of ownership ensured
- Integrity - information is immutable to those not authorized to change it
- Non-repudiation ==> neither sender nor receiver can deny that they performed a transaction
- Access control ==> access to information is controlled and limited to authorized parties
- Availability ==> protected and secure assets and information should remain available as needed (by authorized parties of course!)

#### Major Concepts in Assessing Vulnerability

**Key term** ==> ```attack surface``` - how many components and to what degree can an attacker touch a system?

- Design => software is vulnerable by design
- Implementation => design is sound, implementation is weak
- Configuration => configuration and settings weak

more ...

- Social Engineering ==> the human problem in cyber attacks. Nigerian 419 scams, spam, phishing, pharming, spear-phishing, mules
- Authentication/Authorization
- Access permissions (file systems, etc..)
- Audits
- User Interface

#### Case Study: Panama Papers (article found by Ali Bhutta)

PANAMA PAPERS: Mossack Fonseca compromised.  

VICTIM ==> Financial organizations and other individuals

VULNERABILITY ==> word press plugin (revolution slider) allowing access to remote shell on web host

DATA BREACHED ==> emails and files containing sensitive financial data ==> 11.5m documents and 2.6 terabytes of information

**Key term** ==> ```attack vector``` - the series of vulnerabilities and exploits needed to carry out attack

```ATTACK VECTOR```:

* plugin ==> wp-config exposed ==> db access creds in plaintext ==> db contained email plugin creds in plain text
* drupal vulnerability -> sql injection -> client login -> access to documents

Breach summary (from article) ...

>	Their web server was using out of date firewall.
>	We’ve recognized that they were using the most common WordPress vulnerabilities, Revolution Slider.
>	Their web server was on the similar network as their mail servers founded in Panama.
>	They were serving sensitive client data from their portal website which comprises a customer login to access that data.

---


[comment]:### 2016-11-14 Week 12
[comment]:### 2016-11-21 Week 13
[comment]:### 2016-11-28 Week 14