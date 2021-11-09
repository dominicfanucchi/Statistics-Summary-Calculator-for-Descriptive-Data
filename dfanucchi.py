# COURSE: CMPS 3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
# DATE: 11/01/2021
# STUDENT 1: Dominic Fanucchi
# DESCRIPTION: Personal code file for Statistics Summary Calculator


# test function for file importing
def say_hello():
	print('Hello, this is the beginning of a Statistics Summary Calculator\n')
	print('For CSUB CMPS 3500 Programming Languages!')

def main_menu():
    def print_menu():
        print(30 * "-", "M A I N  M E N U", 30 * "-")
        print(76 * "-")

    loop = True
    int_choice = -1

    while loop:
        print_menu()
        choice = input("Enter your choice [n - n]: ")

        if choice == '1':
            print("choice 1 was selected.")
            int_choice = 1
            loop = False
        elif choice == '2':
            print("choice 2 was selected.")
            choice = ''
            int_choice = 2
            loop = False
        else:
            input("Wrong menu selection. Enter any key to try again...")
     return [int_choice, choice]
