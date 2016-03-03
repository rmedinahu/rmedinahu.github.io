---
layout: course_page
title: 
permalink: /457/hw/cs457p2p-protocol-part2/
parent_course: 457
---

cs457 P2P PART 2 Application Protocol

**Overview**: This p2p application replicates a very simple distributed hash table (e.g., the database items are collected and assembled by connected clients). This protocol is similar to the previous [protocol part 1](/457/hw/cs457p2p-protocol-part1/). We implment a two-step protocol in which the client first *registers* with a db server called a ```TRACKER```. Once registered with the ```TRACKER```, the client then iteratively requests single database items from their nearest neighbor (their predecessor). When the client has collected all of the items it must then **assemble** the items in their correct **logical** order.

Messages are sent in packets defined as tuples e.g., ```(COMMAND, msg)```

ECHO FOR TESTING:

>	(ECHO, MYHANDLE)

REGISTRATION HANDSHAKE:

**Client requests registration by sending the following tuple to ```TRACKER``` server:**

>	(REGISTER, handle_str, port_num)


**Client receives a) neighbor's ip, b) neighbor's handle, c) neighbor's port number, d) database size, e) a db item to host**:

>	(REG_INIT, ip_str, handle_str, port_num, dbsize_int, dbitem_packet)

NOTE: db_item_packet is a tuple ==> ```(seq_num, data_str)```
----

NEW NEIGHBOR UPDATE:

**Server receives message from the ```TRACKER``` to update the ip address of nearest neighbor:**

>	(UPDATE_NBR, handle_str, ip_str, port_num)

**Server does not need to respond to ```TRACKER```. But should update NEIGHBOR_CONNECTION information.**

PING REQUESTS:

**Server receives message from ```TRACKER``` to verify existence.**

>	(PING, time)

**Server should respond as follows:

>	(PING, MYHANDLE) # MYHANDLE is your server's handle set up at application startup.

QUERY HANDLING

**client sends nearest neighbor query request:**

>	(QUERY, seq_num_int)


**Neighbor responds with result**

>	(QUERY_RESULT, (seq_num_int, data_str))

*Notes: a) the data in this message is itself a tuple  b) the data tuple may be None (or null) in cases where data was not found. (None, None)**


**EXAMPLE**

*Client 1 completes REGISTRATION HANDSHAKE*

*Client 2 completes REGISTRATION HANDSHAKE*

*Client 2 sends QUERY to Client 1 (Client 1 is Client 2's nearest neighbor):*

>	(QUERY, 0)                   # Client 2 requesting db item 0 from Client 1
>	(QUERY_RESULT, (0, 'Blue'))  # Client 1 fetches item and sends result as response to Client 2



**TRANSACTION COMPLETION**

After the client as successfully received all db items from the network it can assemble the items in their logical order and print the final secret message. At this point, the client portion of the p2p app is finished but the server should remain running providing its services (db items) for others.

 