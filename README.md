# shodan_revisited
Project Report: Shodan Revisited
By: Jenna Baccus, Philippe Bled and Bruce Huang
For: Dr. Tyler Moore
Course: CS-7193 Security Economics
 
Shodan Revisited
An update on Leverett’s study of Industrial Control System Connectivity
	
 
Abstract
	In 2011 Eireann P. Leverett proved that the misconception that Industrial Control Systems are segregated from the open internet was wrong. Now, in 2017, industrial control systems are still connected online in spite of a better understanding of the security risks industry-wide and security controls required by NERC-CIP (Leverett). Critical information about industrial control systems connecting protocols, operating systems, geographical locations and types can be found all too easily using Shodan.io. In the course of this research our team was able to find and categorize internet-facing SCADA (Supervisory Control and Data Acquisition) systems, water treatment facilities, telecommunication systems and system controllers such as Programmable Automation Controllers. Many of these devices are deployed on critical infrastructure sites such as electrical power grids, water facilities and nuclear power plants to enable remote control over operations. By being exposed the open internet, many Industrial Control Systems are inherently more vulnerable to targeted cyber reconnaissance and cyber attacks. The consequences of a cyber attack may cause genuine, physical harm to affected populations and on a much larger scale than previously seen. 
 
 
Introduction
Initial Research 
From 2009 to 2011 Éireann P Leverett conducted in depth research into the connectivity and vulnerability of internet-connected industrial control systems on a global scale. He published his findings as his PhD dissertation at Cambridge University in 2011. The primary objective of his research into the operational security of Industrial Control Systems (ICS) was to demonstrate that Industrial Control Systems are connected to the Internet and many internet-facing ports are exposed and vulnerable to open web access. In the past, it was a common misperception that ICS’s only communicated internally and had no outward facing points of connectivity to the world wide web. However, through his research in 2011 Leverett was able to prove that facilities and organizations implementing industrial control systems were connecting those systems to the internet on much larger scale than previously the assumed. He conducted his research using Shodan.io to scan for open ports on Industrial Control Systems that are connected to the internet. By either intentionally or unwittingly connecting open ports to the internet, corporations and organizations operating industrial control systems exposed their operations to more pervasive and dangerous cyber threats. The purpose of our research will be to re-create and run Leverett’s queries on Shodan and conduct a comparative analysis between his conclusion and the discoveries made in this research. We will use those findings to update Leverett’s initial research on ICS connectivity and demonstrate whether or not industrial control systems are more or less connected to the internet.
 
Background 
 
	Industrial control systems enable remote human control over different types of control systems and widespread instrumental devices, sensors and controls. Industrial controls systems operate differently depending the types of industry they’re deployed on and they’re built to electronically managed what used to be extremely physical operations. According to NIST special publication 800-82 and noted in Leverett’s research industrial control systems are typically deployed on oil and natural gas, transportation, chemical, pharmaceutical, water, electric and nuclear facility operations to allow for remote management of a large network of devices and controls. Industrial Control systems manage and control the key logical and physical operations of these facilities over vast networks that are increasing in complexity. Many of these industries provide essential resources such as water, electricity and telecommunications to an enormous populations and are the fundamental backbone of most modern societies. 
 
 
Methodology
 
 To complete the research, we recreated the following sections of Leverett’s research methodology. Our methodology began by running the table of queries provided in Leverett’s dissertation and pulling the unique IP address connections for each individual search using Shodan.io. Shodan acts as a search engine that enables users and researchers to discover internet connected devices and device types by scanning open HTTP, FTP, SSH and Telnet connections passively over the internet. However, some portions of these methods do stray from Leverett’s by using the Shodan API to search through the Shodan data. A banner sample is given:
 
HTTP/1.1 200 OK
	Date: Tue, 18 Apr 2017 06:36:22 GMT
	Server: Apache/1.3.31 (Unix) PHP/4.3.9 mod_ssl/2.8.20 OpenSSL/0.9.7e
 
From the string of information provided by the Shodan banner, we directly get city name, latitude and longitude of the city or the country. However due to the number of results we relied heavily on the ‘count’ method because the ‘search’ method gave more information than we needed for our research. We produced the number of countries by using the ‘count’ method and can get country counts from the API results. The ‘value’ give us ISO country code so now we can locate country and get the count.
The change of banner format brings us to another issue: the operating system is harder for Shodan to discover through a passive port or IP scan. After reviewing the format of the new banner, only three of Leverett’s former queries were able to provide operating system information from the connection. To solve this problem, the ‘operating system; column from the Shodan search results was isolated. Since Leverett does not directly mention this column, this is assumed to be another potential alteration of how Shodan presents it’s search results. Although the ‘operating system’ column should provide easier access to operating system information, the subsequent results were extremely limited. One of the possible reasons is this column is collected in a different way than it was in 2011. When checking the three queries whose banner information column which includes detailed operating system information, the corresponding operating system column does not present those same results. So we decided to combine the operating system column and banner information column to more accurately analyze the results and interpret it’s meaning. In order to analyze the operating system information from the banner, we used python to tokenize the banner and combined the results with the ‘operating system’ column to produce results necessary for analysis. With this information we will analyze the operating system information, and compare the geographical locations, by country, of the vulnerable ICS devices and servers. Finally, we conducted research into exploits for each operating system using ExploitDB, an online search engine tailored towards finding reported application vulnerabilities. We can now establish how Leverett’s assertions and conclusions about ICS connections have developed from the time his research was performed in 2011 to the present day by comparing the number of unique connections and discernible related information in R. Our primary means of analyzing our data sets and generating the appropriate visualizations was R.
 
Exploring the Results
 
	After extensive time conducting research on both Shodan.io and Exploit DB we were able to use R programming to clean through and analyze the data. The methodology delivered the following results from Shoda.io, python API’s, ExploitDB and R Statistical Programming language. 
 
Operating System Discovery and Comparison 
 
The research in Shodan discovered up to 1,966 individual connections that provided the operating system information for the connecting device, controller or computer. However, operating system information is more difficult for Shodan to produce results for through a passive port or IP scan. Thus, after reviewing the banner information, only three of Leverett’s former queries were able to provide operating system information from the connection results - Powerlink, Allen-Bradley and RTS+SCADA. The results of the operating system column was extremely limited which narrowed the scope of our exploit search parameters. The operating system information always follows after the server information, and since the server information is needed for the purpose of this research, we searched for the server and operating system together. After receiving the information from the banner, the results were combined with the ‘operating system’ column to produce reasonable results to analysis. With this information the operating system demographics were analyzed and compared to the number of total connections for each operating systems. The data revealed that the most popular operating system that is used is a Unix-based operating system. At least 1,655 Industrial Control System connections use Unix-based operating systems. When compared to the other connections that also produced operating system information, Unix-based systems account for 84.18% of the entire query.

 
ExploitDB was used to search for specific operating system exploits and those search results were compared to the total number of connections that produced operating system information. As the number of legitimate exploits discovered by Leverett was already limited by the information given through Shodan, we expected to find fewer exploits per operating system today. Our search parameters only included vulnerabilities in an operating system that could be exploited by a remote attacker. The exploit search parameters were limited because they had to explicitly match the searches for Remote Exploits as it was conducted previously by Leverett. The results totaled to 416 exploits for a minimum of 15 different operating systems. In 2011, Leverett found significantly more exploits than our research results produced. Our smaller count size could be due to a few different variables such as less information being available through Shodan or the institution and popularity of different protocols being exercised by ICS’s. However, Leverett states explicitly one cannot immediately assume it is exploitable due to security techniques such as perimeter-facing firewalls, intrusion detection systems and even anti-virus software.



 
 
 
Operating System
ICS Count
Remote Exploits
Ubuntu 2.6
1
14
Ubuntu 2.8
1
0
Ubuntu 2
4
1
Unix
1655
6
FreeBSD
5
129
Linux
18
62
Debian-5
21
0
HP-UX 11.x
23
4
Linux 2.4-2.6
5
5
Linux 2.4.x
5
2
Linux2.6.x
11
3
Windows 7 or 8
113
99
Windows XP
97
91
 
Table 2:
 
The total number of exploits per operating system is interesting in that the number of industrial control system connections with that operating system does not influence the number of exploits for that specific operating system. After discovering these preliminary results we decided to dive further into the data to discover the percentage of connections versus the percentage of remote exploits. A linear regression model was built in order to determine the significance between the number of total connections with operating system information to the related number of operating system exploits. The initial assumption was that the popularity of an operating system would inherently influence the total number of remote exploits. The results of the linear regression model demonstrated that there is not enough critical evidence to support the theory that operating system popularity is related to the number of its exploits. The null hypothesis was rejected due to a p-value of 0.3165 and a standard error of 2.4. Exploit information cannot be feasibly correlated with the popularity of an operating system in regard to Industrial Control System use. Table 3 shows that even though the most popular operating system is a unix-based operating system with a high percentage of ICS connections very few exploits were found in our research.
 
 

	Table 3
 
HTTP Response Codes
 
	Leverett’s research included looking at the HTTP version and the response codes that were presented when it intercepts a remote, unknown connection. In Leverett’s research results he was able to break down each individual HTTP responses by their associated code number. According to Leverett in his dissertation the HTTP response codes should give “insight into how those devices with an HTTP interface behave when a random connection is made”. (Leverett 32) The shodan results provided us with the information necessary to recreate his research and determine what types of codes are being received in 2017. Leverett discovered 7500 connections with only 17% of those connections requiring authentication (Leverett 32), and four different HTTP Response codes overall. The search results discovered 12 different codes, and of the 16,369 connections that provide the HTTP response codes, only 7.5% of them required immediate authentication. Proportional to the total dataset of 44,256 connections only 2.79% of those connections required authentication in our research and 42% allowed the connection to occur before requiring authentication. 51% of our connections provided the HTTP 1.1 302 code to redirect the URL However, the results cannot definitively show that this number is as terrifying as it appears because the dataset only includes results from Shodan. If a device existed segmented behind a firewall, Shodan may not be able to connect to the device or system IP address to receive thee HTTP Response Code in the first place. Even with the substantial increase in connections for our dataset, the decrease in proportional authentication requirements is still very disconcerting. 
	
	Table 4
 
Analysis of Protocols by Category instead of queries search keywords.
 
	A multitude of protocols that govern how different types of Industrial Control Systems operate and connect were discovered from Shodan. Rather than just presenting the totals for which queries produced results, by looking more in depth at the categories of systems and devices we were able to distinguish those that were most present online. By parsing out the the extraneous query data, R allowed us to independently measure the systems and devices used in Industrial Control Systems that are connected to the internet. Not only is this useful and interesting for our research, but it’s highly valuable information for the corporations and organizations that employ these devices and systems across their network. Our results and the following graph (Table 5) shows that HAN/BMS (Home Area/Automation Network and Building Management System)has the most devices connected to the internet with over 400 connections. The data also shows that PACs (Programmable Automation Controllers) showed the highest percentage of change from 2011 to 207 and have increased in connectivity by a ratio of 250.08%. PAC are a new type of PLC that have the characteristic of being programmable in modern languages, mostly C and C++,  in contrast PLC use Ladder Logic. The increase in the use of PAC can be attributed to the use of modern languages provide PACs greater functionalities and versatility than PLC. On the other hand, these factors also imply that PAC carry greater potential for vulnerabilities, as attackers are not bound to work in a specialized language but can use tools developed for other platforms.

	Table 5
 
 
Ratios of System and Device Categories from 2011 to 2017
 
Name
Ratio
PAC
250.08
Telemetry
100.33
PLC
77.46
Protocol Bridge
34.95
Historian
28.00
HMI
25.49
HAN/BMS
10.76
Embedded Web Server
1.74
RTU
1.07
BMS
0.46
SCADA
-0.43
HAN
-1.00
PCS
-1.00
Table 5: Ratio of Devices connected by Category.
 
 
Connected ICS Geolocation Analysis 
 
	Leverett’s initial research queries searched for industrial control systems on a global scale rather than focusing solely on first world countries such as the United States or the United Kingdom. He was prudent in stating in his dissertation that just because we can determine global connectivity of industrial controls systems that we should not make inferences towards a global trend. However, because this is an update to his past findings, the connections in this dataset can be effectively compared to those from 201l in order to determine if Leverett’s assertion of ICS connectivity is still prevalent. In this research the banner displayed information for each individual industrial controls system port connection and labeled each country using the ISO-3166 country code. For example, the United States of America is simple “US” or Denmark is labeled as “DK”.  Leverett used the country codes to identify the geographical location of the servers and devices. However when we attempted to replicate the Leverett’s methodology for establishing geo-location of servers and devices, we were limited extensively by the information we were able to obtain through Shodan. As a result of the change, the country codes cannot be obtained directly from the banner and had to search for this information for each country individually. 
	After cleaning the dataset and processing in the individual country codes, the dataset produced the top 20 nations with the most open industrial control connections across the globe. As shown in the table top contenders such as the United States, Canada, the United Kingdom and Japan. What is surprising is that our top 20 results do not include China, India or Russia, three of the fastest growing countries in the world. Another interesting find is that Norway, the Czech Republic and France demonstrate some of the largest growth in industrial control system connections in 2017. In the case of Norway, this could be because of a 4.3% growth of oil and gas in 2016 (tradingeconomics.com).
 
	Table 6 
 
	After the extent of the growth between the top 20 countries from 2011 to 2017 was determined, the total connections per country was totaled worldwide so that the relative change could be mapped globally . In this research the dataset presented significantly more countries with 1 or more internet-connected industrial control systems than Leverett. In Leverett’s dissertation research, he only found up to 72 countries with 7,489 individual industrial control system connections through Shodan.io. Reusing the same queries on Shodan and on the Shodan python API 111 individual countries with 44,256 individual industrial control system connections were found. The best way to demonstrate connection growth on such a large scale was for us to create maps in which the color of the country would indicate the amount of connections. The first map shows the number of connections per country from Leverett’s initial research in 2011 and was created in the R programming language. The United States, Canada and the United Kingdom, along with Norway, Sweden and Finland show the most instances of ICS connections. A scale of base log10 was used and is represented by a color for each order of magnitude.
	Table 7: Map of Log10 of the number of connections per country in 2011
 
	The second map was generated in R from the data pulled from Shodan.io, therefore corresponds to 2017. An increase of an order of magnitude in the number of connections was discovered, which explains the new category in dark red. Again the United States dominates the map as it is the only country with the number of connections in the tens of thousands.
	Table 8: Map of Log10 of the number of connections per country in 2017
Finally, the overall percentage change of every country was mapped to determine whether or not there are fewer or greater industrial control systems by country rather than on globally. By looking at the change per country rather than trying to determine if the change in ICS connections on a global scale is significant, the numerous variables that may have been required was avoided. Each country has its own economic industries, regulations and practices that govern how to operate industrial controls systems.
 

	Table 9: Map of Log10 of the difference of the  number of connections per country from 2011 to 2017.
 
Conclusion and Limitations
Limitations
Many challenges hindered the research due to both changes in technology, the Shodan interface and the natural restriction of time. Leverett’s secondary objective was to discover whether or not connectivity was increasing or decreasing over time. We wereunable to track and analyze industrial control system connections over multiple periods due to the time limitations imposed on us by the project parameters. However, a comparative analysis was conducted between the datasets re-using the Shodan queries provided in Leverett’s dissertation. By analyzing the different data collections a clear and updated answer to Leverett’s question of whether or not these systems are becoming more and less connected over time can be answered. Another challenge was the disarray of data and formatting issues with the shodan query banners. This issue was corrected by cleaning the data through a “semi-automatable process” based on the author’s methodology as prescribed in his dissertation. Regardless many queries did not produce operating system information in the results banner and operating system data was discovered from only three of the Shodan queries. One possible explanation is that the operating system column is collected in another way different from banner information. Another possible scenario preventing us from gathering this type of information from Industrial Control Systems is that corporations or organizations are deploying the appropriate security controls to prevent passive scans from gathering this information. The production of the operating system information is critical to determine vulnerability information on ExploitDB, however since we had significantly limited information from our queries we could only find exploits for those specific types of industrial control system protocols.
Another limitation to our research was determining the exact geographical location of each individual industrial control system connection. Even though Shodan.io banners present geolocational data, it only provided the country and relative timezone. There were only a few cases in which the results produced a precise location such as a city or district. We were also unable to track the specific location by individual internet service providers either. Leverett used autonomous system number data to plot his mappings. We also were only able to determine the category of devices using banner data from specific connections. We do not have his datasets which would include country, total connections, operating system, and specific device types. Device type would include more information to aid in our research for exploits. We only have results that measure the total number of devices connected per category. We can only compare his numbers to ours, and are not able to relate this results with other device categories. One potential explanation for these issues is that the shodan query banner format  is giving us a different information values than Leverett was able to get in 2011. Thus, rather than perfectly recreating his mappings of industrial control system connections we calculated the average longitude and latitude of each country to solve this issue and generate our mappings.
Finally, in his dissertation Leverett does not go into enough detail to how he chose and created his the queries for Shodan.io. Without his methodology for choosing and creating queries to search for industrial controls systems were bound to the queries only provided in his by within his dissertation. Even with his methodology we would be unable to explore the data of our own written queries since we don’t know the methodology he used to sort different queries. We cannot determine from his paper why the author did not specify the reason to study those those specific queries for industrial control system research..
 
5.2 Conclusions 
In spite of Leverett’s dissertation demonstrating the connectivity of ICS’s across the globe,  our team’s research shows definitively that industries deploying industrial control systems are still allowing remote and passive connections on many types of devices. Globally, we have seen a near 600% increase in the number of connections. The United States alone as produced upwards of 537% more industrial control system connections since 2011. The growth of Norway’s ICS connections could be in part because of a 4.3% growth of oil and gas in 2016. The expansion of their oil and gas sector in Baltics management systems such as SCADA systems and the integration of PLC and PAC controllers may also play a part, but we cannot confirm that assumption without further research. Only three countries, FInland, Greece and Slovenia, have shown a decrease in the number of connections per country. Our research has demonstrated that along with the rise of connections across the globe, operating system exploits have actually decreased. It may be that the exploits reported to ExploitDB may have decreased or that ICS management and security controls are better implemented such as software patches and vulnerability remediations. 
Operating system information per query has decreased significantly with a majority of operating systems being linux or unix related. Leverett’s research queries found 23 different operating systems with 793 total connections. Our research into Shodan only turned up 13 different operating systems. This research produced more connections overall and most industrial controls systems from our data is run on a unix-based operating system.We anticipated more exploits for Unix-based systems than we were able to discover using ExploitDB because in over 1,600 connections only 6 remote exploits were discovered. Industrial controls systems running on the Windows operating systems had 210 connections with 190 exploits. This may be because of the prevalent use of Windows XP in industrial control systems and because it is no longer supported by Microsoft. 
The development of more independent technology makes industrial control systems more versatile and easier to implement. The primary discovery from this analysis is the rise of PACs. Automation technology such as Programmable Automation Controllers (PAC) is growing and becoming widespread on a global scale. PAC’s have the biggest overall change, with telemetry close behind.  Since PAC are programed using modern languages, are fully functional computers, have little to no supervision and do not have physical means of I/O, the fact that they are connected to the internet makes them a potential for large scale vulnerabilities.(www.globalspec.com) HAN/BUS has the most internet connections for both datasets, however it can be a logical assumption that the large number of HAN/BUS connections is because it is web server interface for many types of devices. 
Finally, our HTTP response code research enabled us to analyze and compare the responses of devices to an unknown connection attempt from both version of HTTP/1.0 and HTTP/1.1. A huge majority of the industrial control system web servers are now utilizing HTTP/1.1, with only 5.8% of the connections that produced response codes running on HTTP/1.0.  Unfortunately, the response codes generated were discouraging. Out out of the entire dataset, only about 2% of the Shodan queries produced immediate authentication requests. While some blocked or redirected a connection, many may actually allow access the device or server interface without an authentication step beforehand. For ethical reasons, we did not attempt to access a device or server’s web interface.
Finally, countries using industrial controls systems have increased significantly but have continued implementing poor or sub-standard security practices. Newcomers maintain the trend set by the other nations and seem to not have different practices in relation to security. It is likely that industrial control systems lack inherent or advanced security features because of the rise of cheaply designed and manufactured technology. Shodan is an exemplary tool to aid auditors and security analysts to determine vulnerable devices and software deployed on industrial controls systems. With proper segmentation of industrial control systems and their devices, or by requiring access authentication many of these connections would be secure from malicious reconnaissance and attacks. 
 
Future Research Potential
This research into industrial control connections discovered many opportunities for potential, future academic inquiries. With the introduction of new technologies such as PAC’s and the improvements to the Shodan API, researchers could go more in depth with many of the subjects merely introduced in this paper. Any research conducted on actual exploits an attacker could possible use by taking advantage of the Shodan and ExploitDB resources could be very eye opening. With the increase in connectivity in the past six years, and open source information related to exploits, an attacker may possible gain control over a system or device. There is definite potential for academic research and ICS threat modeling. Also for the purpose of security, it is critical to answer why those devices and systems are connected. So it brings out another interesting topic about the reason behind the connections. With enough information about it and with the application of valuable statistical metrics, the security of those devices and systems could be significantly strengthened in the long run.
Also if the exact location of the connections could be determined, researchers might figure out whether those devices belong to critical infrastructure or corporate systems. Also, the Shodan API seems to retrieve more valuable data. When using the Shodan API, the search results return detail information which has more usability for research and empirical measurement. The API results more relevant data such as ASN, detailed location information like city, longitude and latitude, port number, transport protocol, server and operating system. Itcould be very valuable to both academics, corporations and public organizations to extending this research to match the two years Leverett spent gathering and analyzing data. 
Finally, the enormous increase in the use of specific devices such as Programmable Automation Controllers also presents a topic for valuable academic research. The use of PAC’s has increased by approximately 250% since 2011 according to our data. The rise of this devices popularity implies that organizations using industrial control systems are relying more heavily on automation to run physical process and data retrieval operations. We believe research into the vulnerabilities of devices that enable automation on critical systems could be extremely valuable and paramount in the future as the prevalence of automation continues to grow in a global economy. 
	
 
 

References
 
Éireann P. Leverett. Quantitatively Assessing and Visualising Industrial System Attack Surfaces. Retrieved March 2017 from http://www.cl.cam.ac.uk/~fms27/papers/2011-Leverett- industrial.pdf 
 
Anon. Norway GDP Growth Rate  1978-2017 | Data | Chart | Calendar | Forecast. Retrieved April 15, 2017 from http://www.tradingeconomics.com/norway/gdp-growth
 
Anon. Programmable Automation Controllers (PAC) Information. Retrieved April 27, 2017 from http://www.globalspec.com/learnmore/industrial_computers_embedded_systems/industrial_computing/programmable_automation_controllers_pacs 
 
Keith Stouffer, Joe Falco, and Karen Scarfone. 2011. Guide to Industrial Control Systems (ICS) Security. (June 2011). Retrieved March 2017 from http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82.pdf
 
 

 
Appendices:
 
Appendix A: 
The following coding scripts provided critical data from the Shodan.io API. The R programming language was used to create most of our graphs and maps. 
R Programming Scripts: Please refer to InfoSec Project script.r
Python API Scripts: Please refer to Country_and_Connections.py
 
 
Appendix B: Shodan Queries
The following queries produced the primary search results for this research. They are written in the Shodan.io search engine syntax. 
 
Shodan.io Queries
A850+Telemetry+Gateway
ABB+Webmodule
Allen-Bradley
BroadWeb
Cimetrics+Eplus+Web+Server
CIMPLICITY
EIG+Embedded+Web+Server
eiPortal
EnergyICT
HMS+AnyBuss-S+Web+Server
i.LON
ioLogik
Modbus+Bridge
ModbusGW
Modicon+M340+CPU
Niagara+Web+Server
Powerlink
Reliance+4+Control+Server
RTS+Scada
RTU560
SIMATIC+NET
Simatic+S7
SoftPLC
WAGO
 
