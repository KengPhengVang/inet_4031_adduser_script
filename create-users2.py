#!/usr/bin/python3
# INET4031
# KengPheng Vang
# 3/18/2026
# 3/19/2026
# These imports bring in libraries that will help provide the proper tools for interacting with this file
import os	# Gives access to OPS functions
import re	# Allows ability to search, match, and manipulate text 
import sys	# Provides functions to interact with the python interpreter 

def main():
    # Asks the user if they want to do a dry run or not
    dry_run_input = input("Would you like to run in dry-run mode? (Y/N): ")
    dry_run = dry_run_input.strip().upper() == 'Y'

    for line in sys.stdin:
        # The character it is looking for is a hashtag (#). It is specifically looking for a hashtag because if it is text base (comments), it will always start with a hashtag
        # There are two possibilities on why it is looking for hashtag, either to let the system know to disregard it, or to scan for comments as input
        match = re.match("^#",line)
        # This code cleans up and breaks down a string to ensure that it is usable
        fields = line.strip().split(':')
        # This if statement skips the line if it is a comment or if it doesn't have 5 field after the splittng
        # If it evaluates to true, then the continue statement will run. This means that the it will skip that line and move onto the next one in the loop. 
        # It relies on both of them. The match variable came from the re.match() and checks if the line started with a #. Then, the fields variable, which it comes from the .split(), holds the list of pieces that we've split the line into.
        # It is doing that because it supposed to have exactly 5 fields separated by colons. 
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("==> Skipping commented out line: %s" % (line.strip()))
                else:
                    print("==> Error: The following line does not have enough fields and was skipped: %s" % (line.strip()))
            continue
        # The purpose of the next three lines are to pull out the specific columns from the line. 
        # It relates to /etc/passwd for example: Field 0: Name, Field 1: passsword, and the next 2 being the first and last name.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        # The split is being done because field 4 has all groups listed but they are separated by commas, so this splits it again to get each of the group by itself and be able to loop them later
        groups = fields[4].split(',')
        # This just prints out what acount is being worked on
        print("==> Creating account for %s..." % (username))
        # This builds the linux command to create the user account. The disable password means that the password will not be set through adduser. Gecgos will display the name info. The command gets stored in cmd.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        print(cmd)
        if not dry_run:
            os.system(cmd)
        # It it just letting the user know the script has moved on to the password step
        print("==> Setting the password for %s..." % (username))
        # It uses echo to print the password twice and pipes it into passwd. The reason why it is entered twice is because passwd asks to confirm it. 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        print(cmd)
        if not dry_run:
            os.system(cmd)
        for group in groups:
            # This checks if the group is a dash. If group does is not a dash, then it will run the adduser command and add the user to that group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                if not dry_run:
                    os.system(cmd)

if __name__ == '__main__':
    main()
