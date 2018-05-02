#!/usr/local/bin/python

# Program for displaing information about POSIX compliant OSes.

# Define the clear function, which clears the screen.


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Define the print_menu function, which displays the menu.


def print_menu():
    print "           +------------------------------------------+ "
    print "           |    Menu to show any of the following:    | "
    print "           + -----------------------------------------+ "
    print ""
    print "  1. Computer name                   5. Who is logged in now"
    print "  2. Operating system name           6. Who logged in most recently"
    print "  3. Time since last reboot          7. Help"
    print "  4. Process using most memory       8. Quit"
    print ""

# Define the computer_name fuction which returns the name of the computer.


def computer_name():
    print " The name of the computer is:"
    import os
    os.system('hostname')
    print ""
    raw_input("Hit the <Enter> key to continue...")

# Define the os_name fuction which returns the name of the operating system.


def os_name():
    print " The name of the operating system is:"
    import os
    os.system('uname')
    print ""
    raw_input("Hit the <Enter> key to continue...")

# Define the up_time fuction which returns the amount of time since a reboot.


def up_time():
    print " The elapsed time since the last reboot is:"
    import os
    os.system('uptime | cut -d "," -f1 | cut -c 11-')
    print ""
    raw_input("Hit the <Enter> key to continue...")

# Define the mem_top fuction which returns the top users of memory.


def mem_top():
    print " The top five processes using the most memory are:"
    import os
    # first we display the headings for the columns
    os.system('ps aux |awk \'{print $2, $4, $11}\' |sort -k2rn |tail -n1')
    # next we display the top 5 memory users
    os.system('ps aux |awk \'{print $2, $4, $11}\' |sort -k2rn |head -n5')
    print ""
    raw_input("Hit the <Enter> key to continue...")

# define the internal_ip function which we are not using right now.


def internal_ip():
    print "Left blank for now.\n"
    raw_input("Hit the <Enter> key to continue...")

# define the external_ip fuction which we are not using right now.


def external_ip():
    print "Left blank for now.\n"
    raw_input("Hit the <Enter> key to continue...")

# define the fuction for


def who_info():
    print " List of users currently logged in:"
    import os
    os.system('who -H')
    print ""
    raw_input("Hit the <Enter> key to continue...")

# define the fuction for choice four


def last_info():
    print " Searching for the list of last users logged in:"
    import os
    os.system('last |head -n 10')
    print ""
    raw_input("Hit the <Enter> key to continue...")

# define the help fuction


def help_function():
    clear()             # Clear the screen
    print "This is the help function"
    print ""
    print "This program was written in BASH by Dan Hogan.  The purpose of this"
    print "program is to display basic system information on computers running"
    print "POSIX complaint operating systems, such as UNIX, Linux, BSD, OSX."
    print ""
    print "The program displays a menu allowing the user to query information,"
    print "and displays that information to the screen."
    print ""
    raw_input("Hit the <Enter> key to continue...")


# main
clear()             # Clear the screen when we start

loop = True

while loop:         # While loop which will keep going until loop = False
    clear()         # clear the screen
    print_menu()    # Displays menu
    choice = input("Enter your choice [ 1 - 8 ]: ")

    if choice == 1:
        computer_name()
    elif choice == 2:
        os_name()
    elif choice == 3:
        up_time()
    elif choice == 4:
        mem_top()
    elif choice == 5:
        who_info()
    elif choice == 6:
        last_info()
    elif choice == 7:
        help_function()
    elif choice == 8:
        print "bye!"
        # You can add your code or functions here
        # This will make the while loop end.
        loop = False
    else:
        # Any integer inputs other than values 1-8 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")

