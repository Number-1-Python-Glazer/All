
failed-login-counter documentation

TITLE
Failed Login Counter  

OVERVIEW
The tool  examines log files to determine the number of unsuccessful login attempts. The tool searches for the word "FAILED "  in every line of the file. The system generates a simple number which enables users to detect unusual account behavior.

GOAL
The tool demonstrates fundamental log management techniques and entry-level security assessment methods.
The script maintains simplicity to enable users to understand its operational logic.,

PROCESS
The program  required users to specify the path of their log file.
The program accessed the file through read-only access.
The program searched each line for the presence of the word  "FAILED.",
The program raised its counter value whenever it detected the word.
The program displayed the accumulated total at the end of execution.

WHY THIS MATTERS IN CYBERSEC
Security incidents commonly include failed login attempts in their logs.,
Security analysts review authentication patterns to detect both repeated failure attempts and irregular time patterns.
The project demonstrates my ability to handle security logs at their most basic level.

SKILLS SHOWN
Basic Python
File reading
String matching 
Simple event counting
Clear and readable code

WHAT I LEARNED
Text logs can be read from logs.
The process of safe line-by-line examination becomes possible through this method.
The system produces basic results which support security analysis tasks. 
The analysis of abnormal authentication patterns became possible through this experience.
