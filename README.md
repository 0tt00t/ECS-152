# ECS-152
Programming
This is a team assignment based on a 2-member team. Please complete the team formation assignment first before proceeding with this assignment. 

In Homework #1, you used whois command to find out which organization is assigned a particular AS number, and which IP address block is allocated to that organization (or AS). This lab shows an alternate method for mapping a particular IP address to an AS number that owns that address space by leveraging BGP routing tables. In Chapter 4, you learned about Internet routing hierarchy, and how routers in the wide-area Internet figure out the forwarding path to a destination IP address by using the BGP protocol to exchange routing information. A typical BGP routing table at a router X may look like this:

![prog1](https://user-images.githubusercontent.com/82366306/218199985-16720ad1-3d5d-4360-a70a-b11f123c1351.jpg)

Here is how you would interpret the first entry: From router X’s perspective, the shortest way to reach destination prefix 4.21.254.0/23 (i.e. all IP addresses that belong to this contiguous block) is to forward it along a path that will cross three networks (at the high level), identified by their AS numbers: 1239, 1299, and then 10355. Within each of these networks, there can be multiple routers that are involved in routing the packets, but that level of details (intra-domain routing) is masked and hidden from router X. The last network that you need to reach (in this case 10355) is typically known as the home AS that owns the destination prefix (in this case, 4.21.254.0/23).

If you run a traceroute experiment from router X to 4.21.254.0, you will get a router-level path between router X to 4.21.254.0, showing every single router that the ICMP packet traverses. If you run whois with the IP addresses of these routers as input, you will find that a group of routers belong to the first AS (1239), another group belongs to 1299, and the 3rd group belongs to 10355. Given the rich connectivity of the Internet backbone, there can be multiple paths to reach the same destinations. Since Classless Inter Domain Routing (CIDR) allows prefixes of arbitrary length, overlapping prefixes can exist in the same routing table. Routers forward packets to the most specific forwarding information, called longest prefix match. In this part of the lab, you will write a program that (i) takes an IP address as an input, (ii) performs the longest prefix match on a compressed version
of the routing table, and (iii) look up & output the home AS number for that IP address.

Your team is asked to develop this program in Python based on the following Google Colab template: 

https://colab.research.google.com/drive/1TKzE9cnUikHO4WicDXtPM1YVZS2EsXkV?usp=sharing Links to an external site. 

Please provide sufficient comments for us to understand your code and sample runs for demonstration. Make your code viewable by anyone with link. For your submission, please print out the colab notebook in a pdf and also provide us with the link. 
