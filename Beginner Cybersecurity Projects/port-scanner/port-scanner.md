Overview
The  Python-based Port Scanner Lite tool performs port scans across multiple ports which users can specify by IP address or hostname. The tool enables users who are new to port scanning to learn about the scanning process. The tool demonstrates how to access ports and verify their responses and store the obtained results.

This is the scenario 
A junior analyst operates within a laboratory environment to conduct system testing. The system requires identification of TCP connection-responsive ports. The script demonstrates fundamental scanning principles which security professionals use in their laboratory work.

Purpose  
The program demonstrates networking fundamentals.
The program demonstrates Python script demonstrates how to process user input and perform connection tests.
The program demonstrates effective error management through its organized structure,.

What the script really does
The program requests users to enter their target IP address or hostname.
The program requires users to specify both the starting and ending port numbers.
The program checks if the input values fall within valid ranges.
The socket module enables the script to perform TCP connection attempts.
The program displays all active ports to the user interface.  
The program generates a brief summary after completing its operations.

Why it is useful
Open ports expose services.
Security checks require the identification of all accessible ports.
Users can develop their skills through basic scanning operations before using advanced security tools.

Learning outcomes
The program demonstrates TCP port functionality.
The Python script demonstrates how to use socket for basic operations.
The program contains straightforward loops and functions.
The program checks user input for valid values.
The program includes basic error handling mechanisms.

How it works
The program requires users to enter their information.
The program transforms all port numbers into numerical values.
The program runs through each port in sequence.
The program uses socket.connect_ex with a short timeout for connection attempts.
The port responds when the result equals zero.
The program displays all active ports through the terminal output.
The program generates a summary report after completing its operations.

Limitations
The tool operates at a slow pace.
The tool scans ports individually instead of performing simultaneouss scans.
The tool lacks functionality to detect specific services.
The tool lacksall support for sophisticated scanning techniques.
The tool serves as a basic educational tool for security learning purposes.

Future upgrades
The program should accept command-line arguments.
The program should enable users to choose between saving results to a TXT file or not.
The program should display timing information.
The program should include pre-defined lists of standard network ports.

Skills shown
Decently Basic Python.
Networking awareness.
Clear coding style.
Readable comments.
Foundational security understanding.
