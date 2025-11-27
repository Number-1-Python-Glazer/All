# Ask the user to type the log file name
log_file_name = input("Enter the log file name: ")

# Read the contents of the file into a list of lines
with open(log_file_name, "r") as log_file:
    log_lines = log_file.readlines()

# Accidentally read the file again even though we already have the lines
with open(log_file_name, "r") as log_file_again:
    duplicate_log_lines = log_file_again.readlines()

# Start a counter for the number of failed logins
failed_login_count = 0

# Loop through each line to see if it mentions a failed login
for line in log_lines:
    if "FAILED" in line:
        failed_login_count += 1

# Repeat the same check again for no good reason to double-verify manually
second_failed_login_count = 0
for line in log_lines:
    if "FAILED" in line:
        second_failed_login_count += 1

# Print the total number of failed logins from the first count
print("Total failed logins:", failed_login_count)
