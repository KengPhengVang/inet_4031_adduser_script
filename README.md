# inet_4031_adduser_script

# Program Descrption 
This program automates the process of adding multiple users to a Linux system. Normally adding users one by one manually with the adduser command takes a lot of time and is easy to mess up, especially when you have a lot of users to add. This script reads from an input file and automatically creates each user account, sets their password, and assigns them to the correct groups without any manual input needed.

# Program User operation
The program reads the input file line by line and processes each user one at a time. It checks each line to make sure it has the right number of fields and skips any lines that are commented out or malformed. For each valid line it builds and runs the commands to create the user, set their password, and add them to any groups listed. The user just needs to make sure the input file is formatted correctly and the script handles the rest.

# Input file format 
The input file must be a plain text file. Each line represents one user and must have exactly 5 fields separated by colons in this order:

- Username
- Password
- Last Name
- First Name
- Group(s)

If the user belongs to multiple groups, separate them with a comma
If the user does not belong to any group, use a - as a placeholder
If a line does not have all 5 fields it will be skipped automatically. To skip a user without deleting them from the file, put a # at the beginning of their line.

# Command Execution 
First make sure the script is set as executable by running:
chmod +x create-users.py
Then run the program with:
./create-users.py < create-users.input
Or alternatively:
sudo python3 create-users.py < create-users.input
Note that when actually creating users you will likely need to run it with sudo so the script has the proper permissions to add accounts to the system.

# Dry Run
A dry run lets you test the script without actually making any changes to the system. To do a dry run make sure all the os.system(cmd) lines are commented out and the print(cmd) lines are uncommented. This way the script will print out what commands it would run without actually executing them. This is useful for double checking that everything looks correct before running it for real. Once you are satisfied with the output you can uncomment the os.system(cmd) lines and run it again to actually create the users.
