#-----------------------------------------------------------------------------#
# COURSE: CMPS 3500                                                           #
# CLASS Project                                                               #
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR             #
# DATE: 11/01/2021                                                            #
# STUDENT 1: Dominic Fanucchi                                                 #
# STUDENT 2: Ronaldo Mojica                                                   #
# STUDENT 3:                                                                  #
# DESCRIPTION: IMPLEMENTATION OF A STATISTICS SUMMARY CALCULATOR              #
#-----------------------------------------------------------------------------#

import csv, sys, os, math

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print 31 * "-", "M A I N  M E N U", 31 * "-"
    print " 1.       Count"
    print " 2.       Unique"
    print " 3.       Mean"
    print " 4.       Median"
    print " 5.       Mode"
    print " 6.       Standard Deviation (SD)"
    print " 7.       Variance"
    print " 8.       Minimum"
    print " 9.       20 Percentile (P20)"
    print "10.       40 Percentile (P40)"
    print "11.       50 Percentile (P50)"
    print "12.       60 Percentile (P60)"
    print "13.       80 Percentile (P80)"
    print "14.       Maximum"
    print "15.       End Program"
    print 80 * "-"

def my_mean(s):
    return sum(s) / len(s)

def my_median(s):
    n = len(s)
    index = n // 2
    if n % 2:
        return sorted(s)[index]
    return sum(sorted(s)[index - 1:index + 1]) / 2

from collections import Counter
def my_mode(s):
    c = Counter(s)
    return [k for k, v in c.items() if v== c.most_common(1)[0][1]]

# TODO : ask walter if indexing should begin at 1?
def my_20P(s):
    return sorted(s)[int(math.ceil(0.2 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.4 * len(s)))-1]

def my_40P(s):
    return sorted(s)[int(math.ceil(0.4 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.4 * len(s)))-1]

def my_50P(s):
    return sorted(s)[int(math.ceil(0.5 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.5 * len(s)))-1]

def my_60P(s):
    return sorted(s)[int(math.ceil(0.6 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.6 * len(s)))-1]

def my_80P(s):
    return sorted(s)[int(math.ceil(0.8 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.8 * len(s)))-1]

def my_count(s):
    return len(s)
    # ask if using built in functions is okay
    # if not, write function definition below

def my_min(s):
    return min(s)
    # ask if using built in functions is okay
    # if not, write function definition below

def my_max(s):
    return max(s)
    # ask if using built in functions is okay
    # if not, write function definition below

def my_variance(s):
    # step 1:
    ordered = sorted(s)
    n = my_mean(ordered)
    # step 2:
    difference = [0] * len(s)
    for i in range(len(difference)):
        difference[i] = ordered[i] - n
    # step 3:
    for i in range(len(difference)):
        difference[i] = difference[i] ** 2
    # step 4:
    sd_sum = 0.0
    for i in range(len(difference)):
        sd_sum += difference[i]
    # step 5:
    variance = sd_sum / len(s) # <---- this is the variance
    return variance
    # step 6:
    # return sd = variance ** 2

def my_standard_deviation(s):
    # step 1:
    ordered = sorted(s)
    n = my_mean(ordered)
    # step 2:
    difference = [0] * len(s)
    for i in range(len(difference)):
        difference[i] = ordered[i] - n
    # step 3:
    for i in range(len(difference)):
        difference[i] = difference[i] ** 2
    # step 4:
    sd_sum = 0.0
    for i in range(len(difference)):
        sd_sum += difference[i]
    # step 5:
    variance = sd_sum / len(s) # <---- this is the variance
    # step 6:
    sd = variance ** 2
    return sd

# naming csv files
rideshare = "Boston_Lyft_Uber_Data.csv"
sample = "InputDataSample.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv files
with open(sample, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)

	# extracting field names through first row
	fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)

	# get total number of rows
	#print("Total number of rows: %d"%(csvreader.line_num))

# printing the field names
#print('Field names are: ' + ', '.join(field for field in fields))

# printing first 5 rows
#print('\nFirst 5 rows are:\n')

#for row in rows[:5]:
	# parsing each column of a row
#	for col in row:
#		print("%10s"%col),
#	print('\n')

sample_data_A = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
sample_data_B = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5, 10, 2, 13, 20, 5, 2, 15, 1, 0]
sample_data_C = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Descriptor    Column A    Column B")
print("**********    ********    ********")
print('Count         {a:8d}    {b:8d}'.format(a = my_count(sample_data_A), b = my_count(sample_data_B)))
print('Unique        {a:8d}    {b:8d}'.format(a = 0, b = 0) + ' <-- requires data to be in row/col form find and not an array')
print('Mean          {a:8d}    {b:8d}'.format(a = my_mean(sample_data_A), b = my_mean(sample_data_B)))
print('Median        {a:8d}    {b:8d}'.format(a = my_median(sample_data_A), b = my_median(sample_data_B)))
print('Mode          {a:}    {b:}'.format(a = my_mode(sample_data_A), b = my_mode(sample_data_B)))
print('SD            {a:8.2f}    {b:8.2f}'.format(a = my_standard_deviation(sample_data_A), b = my_standard_deviation(sample_data_B)))
print('Variance      {a:8.2f}    {b:8.2f}'.format(a = my_variance(sample_data_A), b = my_variance(sample_data_B)))
print('Minimum       {a:8d}    {b:8d}'.format(a = my_min(sample_data_A), b = my_min(sample_data_B)))
print('P20           {a:8d}    {b:8d}'.format(a = my_20P(sample_data_A), b = my_20P(sample_data_B)))
print('P40           {a:8d}    {b:8d}'.format(a = my_40P(sample_data_A), b = my_40P(sample_data_B)))
print('P50           {a:8d}    {b:8d}'.format(a = my_50P(sample_data_A), b = my_50P(sample_data_B)))
print('P60           {a:8d}    {b:8d}'.format(a = my_60P(sample_data_A), b = my_60P(sample_data_B)))
print('P80           {a:8d}    {b:8d}'.format(a = my_80P(sample_data_A), b = my_80P(sample_data_B)))
print('Maximum       {a:8d}    {b:8d}'.format(a = my_max(sample_data_A), b = my_max(sample_data_B)))
print ""


# set to true to see menu
# turned off for sample data testing
loop = False
while loop:
    print_menu()
    choice = input("Enter your choice [1-15]: ")
    if choice == 1:
        clear_screen()
        print "Menu 1 has been selected!\n"
        loop = False
    elif choice == 2:
        clear_screen()
        print "Menu 2 has been selected!\n"
    elif choice == 3:
        clear_screen()
        print "Menu 3 has been selected!\n"
    elif choice == 4:
        clear_screen()
        print "Menu 4 has been selected!\n"
    elif choice == 5:
        clear_screen()
        print "Menu 5 has been selected!\n"
    elif choice == 6:
        clear_screen()
        print "Menu 6 has been selected!\n"
    elif choice == 7:
        clear_screen()
        print "Menu 7 has been selected!\n"
    elif choice == 8:
        clear_screen()
        print "Menu 8 has been selected!\n"
    elif choice == 9:
        clear_screen()
        print "Menu 9 has been selected!\n"
    elif choice == 10:
        clear_screen()
        print "Menu 10 has been selected!\n"
    elif choice == 11:
        clear_screen()
        print "Menu 11 has been selected!\n"
    elif choice == 12:
        clear_screen()
        print "Menu 12 has been selected!\n"
    elif choice == 13:
        clear_screen()
        print "Menu 13 has been selected!\n"
    elif choice == 14:
        clear_screen()
        print "Menu 14 has been selected!\n"
    elif choice == 15:
        os.system('cls' if os.name == 'nt' else 'clear')
        print "\n! P R O G R A M   T E R M I N A T E D !"
        print 39 * '-'
        sys.exit()

        #Terminate code completely 
        #Add M key that allows user to go back to menuy options.
        #Add code that takes user back to Menu
    else:
        raw_input("Wrong option selection. Enter any key to try again...")
        
