---
layout: course_page
title: 
permalink: /457/hw/cs457p2p-protocol-part1/
parent_course: 457
---

cs457 P2P PART 1 Application Protocol

**Overview**: This p2p application replicates a very simple distributed hash table (e.g., the database items are collected and assembled by the client). In Part 1, we implment a two-step protocol in which the client first *registers* with a db server called a *```TRACKER```*. Once registered with the ```TRACKER```, the client then iteratively requests single database items from the ```TRACKER```. When the client has collected all of the items it must then **assemble** the items in their correct **logical** order.

**PROTOCOL STEP 1 - REGISTRATION**

The client first connects to the ```TRACKER``` requesting *registration* by simply sending the string, REGISTER, to the ```TRACKER```.

REQUEST MESSAGE FORMAT:

>	REGISTER

The ```TRACKER``` server responds to registration request with a response that simply indicates the SIZE of the db (e.g., the number of items in the db).

```TRACKER``` RESPONSE MESSAGE FORMAT:

>	N *where N is an integer >= 0*


**PROTOCOL STEP 2 - COLLECT DB ITEMS**

Once a client as registered it will have knowledge of the magnitude of the db (SIZE). With this information the client can then loop, each time asking the server for a db items from 0 to N-1. Each db item has sequence number where 0 >= ```SEQNUM``` < N (this is its "hash").


REQUEST DB ITEM MESSAGE FORMAT (request to ```TRACKER```):

>	N *where N is an integer value 0 >= ```SEQNUM``` < N*


```TRACKER``` RESPONSE MESSAGE FORMAT:

The ```TRACKER``` responds to db item requests by sending a packet containing two values in the form of a tuple. The first value is the item's logical sequence order and the second is the item's value. This is in the form: ```(SEQNUM, VALUE)```

>	(N, VALUE)

On receiving a response from the ```TRACKER```, the client must ```deserialize``` the packet using ```pickle```, then place the item ```VALUE``` in the client's locally created db at index given by ```SEQNUM```. NOTE: the locally created db must be set up after a successful REGISTRATION request.


**TRANSACTION COMPLETION**

After the client as successfully received all db items from the ```TRACKER``` it can then assemble the items in their logical order and print the final secret message.

 