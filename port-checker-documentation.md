
Port Checker

OVERVIEW
The tool performs a check to determine if a specific port on a host machine remains accessible. The tool performs a basic TCP connection attempt to function. The port remains accessible when the connection establishment succeeds. The port remains inaccessible when the connection attempt results in an error or times out.

GOAL
The tool demonstrates fundamental networking concepts to users,
The system design maintains simplicity while ensuring users can understand all components.

PROCESS
The system requires users to specify a host address.
Users need to provide a valid port number for the  connection.
The system establishes a TCP socket connection.   
The system attempts to establish a connection to the specified host address and port number.
The script displays an open port message when it successfully establishes a connection.
The script displays a closed port  message when it encounters either a connection error or times out.

WHY THIS MATTERS IN CYBER
Security professionals need to understand port operations as a fundamental networking requirement.
Services become accessible to internet users through open ports.
Security analysts perform port scans to  identify active ports during their attack surface evaluations.
The project demonstrates my ability to understand basic TCP operations.,

SKILLS SHOWN  
Python
socket module
Input handling  
Basic networking logic

WHAT I LEARNED
The process of testing single ports became clear to me.
I learned about the operation of time-out mechanisms.
Scanning should only occur on trusted machines because of security reasons.
Attackers search for active ports during their network scans.
Security analysts use methods to minimize exposure of unnecessary system resources. 
