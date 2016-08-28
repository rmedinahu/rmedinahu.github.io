---
layout: course_page
title: schedule
permalink: /350/schedule/
parent_course: 350
---

**Fall 2016 Schedule of Topics**

Jump to week[n] ==> [1](#week-1)

---

{:.green}
#### 2016-08-29 Week 2
**READINGS**

#### Topics
* Python review
* little hacks: substitution cipher and simple frequence analysis
* TCP/UDP client server and remote shells?

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


[comment]:### 2016-09-05 Week 3 
[comment]:### 2016-09-12 Week 4 
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