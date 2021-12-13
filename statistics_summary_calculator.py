#-----------------------------------------------------------------------------#
# COURSE: CMPS 3500                                                           #
# CLASS Project                                                               #
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR             #
# DATE: 11/01/2021                                                            #
# STUDENT 1: Dominic Fanucchi                                                 #
# STUDENT 2: Ronaldo Mojica                                                   #
# DESCRIPTION: IMPLEMENTATION OF A STATISTICS SUMMARY CALCULATOR              #
#-----------------------------------------------------------------------------#

import csv, sys, os, math, array as arr, traceback, time

def clear_screen():
    # used to clear the screen so that the display is clean
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
    print 80 * "-"
    print " m.       Menu Screen"
    print " s.       Search"
    print " l.       List First 10 Rows Of Data"
    print " q.       End Program"
    print 80 * "-"

def my_len(dataframe):
    # naive method to count length of data container
    counter = 0
    for item in dataframe:
        counter+=1
    return counter

def my_sum(dataframe):
    total = 0
    for count in dataframe:
        total = total + dataframe
    return total

def my_mean(dataframe):
    # naive method to count the mean of dataframe
    return sum(s) / my_len(s)

def my_median(dataframe):
    n = my_len(dataframe)
    index = n // 2 # <-- floor division operator to return an int
    if n % 2:
        return my_quicksort(dataframe)[index] # odd number
    return sum(my_quicksort(dataframe)[index - 1:index + 1]) / 2 # even number

# from collections import Counter
def my_mode(dataframe):
    sorted_frame = my_quicksort(dataframe)
    
    # empty list to append the count of each numbers occurence in the dataframe
    tmp_lst = []
    i = 0
    while i < my_len(sorted_frame) :
        tmp_lst.append(sorted_frame.count(sorted_frame[i]))
        i += 1
    
    # create temporary dictionary to hold the relationship between
    # the sorted list and its occurences within the datafram
    tmp_dataframe_dict = dict(zip(sorted_frame, tmp_lst))
    
    # final dictionary holds all the highest (key, value) occurences from the
    # temporary dictionary
    dataframe_dict = { 
        key for (key, value) in tmp_dataframe_dict.items() 
        if value == max(tmp_lst) 
    }

    # casting the dict as a string and removing unncessary characters
    output = str(dataframe_dict).strip("set([]), ")
    return output

def my_20P(s):
    return my_quicksort(s)[int(math.ceil(0.2 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.4 * len(s)))-1]

def my_40P(s):
    return my_quicksort(s)[int(math.ceil(0.4 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.4 * len(s)))-1]

def my_50P(s):
    return my_quicksort(s)[int(math.ceil(0.5 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.5 * len(s)))-1]

def my_60P(s):
    return my_quicksort(s)[int(math.ceil(0.6 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.6 * len(s)))-1]

def my_80P(s):
    return my_quicksort(s)[int(math.ceil(0.8 * len(s)))]
    # use this return if indexing begins at 1
    # return sorted(s)[int(math.ceil(0.8 * len(s)))-1]

def my_count(dataframe):
    # could delete this function definition and just call my_len() instead
    return my_len(dataframe)

def my_variance(dataframe):
    # step 1:
    ordered = my_quicksort(dataframe)
    n = my_mean(ordered)
    # step 2:
    difference = [0] * my_len(dataframe)
    for i in range(my_len(difference)):
        difference[i] = ordered[i] - n
    # step 3:
    for i in range(my_len(difference)):
        difference[i] = difference[i] ** 2
    # step 4:
    sd_sum = 0.0
    for i in range(my_len(difference)):
        sd_sum += difference[i]
    # step 5:
    variance = sd_sum / my_len(dataframe) # <---- this is the variance
    return variance

def my_standard_deviation(dataframe):
    # step 1:
    ordered = my_quicksort(dataframe)
    n = my_mean(ordered)
    # step 2:
    difference = [0] * my_len(dataframe)
    for i in range(my_len(difference)):
        difference[i] = ordered[i] - n
    # step 3:
    for i in range(my_len(difference)):
        difference[i] = difference[i] ** 2
    # step 4:
    sd_sum = 0.0
    for i in range(my_len(difference)):
        sd_sum += difference[i]
    # step 5:
    variance = sd_sum / my_len(dataframe) # <---- this is the variance
    # step 6:
    sd = variance ** 2
    return sd

from random import randint as random
def my_quicksort(dataframe):
    # if the input array is less than two elements then return the array
    if my_len(dataframe) < 2:
        return dataframe

    # array's to hold elements while being sorted
    low, same, high = [], [], []

    # selecting pivot element at random
    pivot = dataframe[random(0, my_len(dataframe) - 1)]

    for item in dataframe:
        # Elements that are smaller than the `pivot` go to the 'low' list.
        # Elements that are larger than 'pivot' go to the 'high' list.
        # Elements that are equal to 'pivot' go to the 'same' list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return my_quicksort(low) + same + my_quicksort(high)

def my_binarysearch(dataframe, searched):
    # iterative binary search
    low = 0
    high = my_len(dataframe) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if dataframe[mid] < x:
            low = mid + 1
        elif dataframe[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

def my_unique(dataframe):
    sorted_frame = my_quicksort(dataframe)
    tmp_dataframe= []
    count = 0
    for i in sorted_frame:
        if i not in tmp_dataframe:
            count += 1
            tmp_dataframe.append(i)
    return count

def my_min(dataframe):
    # fining min of data structure elements is as easy as picking the first
    # element after sorting
    tmp = my_quicksort(dataframe)
    return tmp[0]
    
def my_max(dataframe):
    # finding max of data structure elements is as easy as picking the last
    # element after sorting
    tmp = my_quicksort(dataframe)
    return tmp[-1] # <-- grabbed last item using negative indexing

# naming csv files
rideshare = "Boston_Lyft_Uber_Data.csv"
sample = "InputDataSample.csv"

sample_read= open(sample, 'r')
file = csv.DictReader(sample_read)

col_A = arr.array('i', [])
col_B = arr.array('i', [])

for col in file:
    col_A.append(int(col['Column A']))
    col_B.append(int(col['Column B']))

#print('column A: ', col_A)
#print('column B: ', col_B)

# # initializing the titles and rows list
# fields = []
# rows = []

# # reading csv files
# with open(sample, 'r') as csvfile:
# 	# creating a csv reader object
# 	csvreader = csv.reader(csvfile)

# 	# extracting field names through first row
# 	fields = next(csvreader)

# 	# extracting each data row one by one
# 	for row in csvreader:
# 		rows.append(row)

# 	# get total number of rows
# 	print("Total number of rows: %d\n"%(csvreader.line_num))

# # printing the field names
# print('Field names are: ' + ', '.join(field for field in fields))

# # printing first 5 rows
# print('\nFirst 5 rows are:\n')

# for row in rows[:5]:
# 	# parsing each column of a row
# 	for col in row:
# 		if col.isdigit():
# 			print("%10s"%col),
# 	print('\n')

# print("Descriptor    Column A                            Column B")
# print("**********    ********                            ********")
# print('Count         {a:<32d}    {b:<32d}'.format(a = my_count(col_A), b = my_count(col_B)))
# print('Unique        {a:<32d}    {b:<32d}'.format(a = my_unique(col_A), b = my_unique(col_B)))
# print('Mean          {a:<32d}    {b:<32d}'.format(a = my_mean(col_A), b = my_mean(col_B)))
# print('Median        {a:<32d}    {b:<32d}'.format(a = my_median(col_A), b = my_median(col_B)))
# print('Mode          {a:<32s}    {b:<32s}'.format(a = my_mode(col_A), b = my_mode(col_B)))
# print('SD            {a:<30.2f}      {b:<30.2f}'.format(a = my_standard_deviation(col_A), b = my_standard_deviation(col_B)))
# print('Variance      {a:<30.2f}      {b:<30.2f}'.format(a = my_variance(col_A), b = my_variance(col_B)))
# print('Minimum       {a:<32d}    {b:<32d}'.format(a = my_min(col_A), b = my_min(col_B)))
# print('P20           {a:<32d}    {b:<32d}'.format(a = my_20P(col_A), b = my_20P(col_B)))
# print('P40           {a:<32d}    {b:<32d}'.format(a = my_40P(col_A), b = my_40P(col_B)))
# print('P50           {a:<32d}    {b:<32d}'.format(a = my_50P(col_A), b = my_50P(col_B)))
# print('P60           {a:<32d}    {b:<32d}'.format(a = my_60P(col_A), b = my_60P(col_B)))
# print('P80           {a:<32d}    {b:<32d}'.format(a = my_80P(col_A), b = my_80P(col_B)))
# print('Maximum       {a:<32d}    {b:<32d}'.format(a = my_max(col_A), b = my_max(col_B)))
# print ""

def load_data(csv_path):
    """
    reads csv to python list of lists in save way and checks if all rows has the same number of columns
    :param csv_path: path to input csv
    :return:
    """
    try:
        # checks is file exists in file system
        if not os.path.exists(csv_path):
            print("Input path {} does not exists")
            sys.exit(0)
        # reads file line by line to python list of lists
        with open(csv_path, 'r') as f:
            lines = [x.strip().split(',') for x in f.readlines()]
        # extracting columns (first) row to validate another rows by nu,ber of columns
        columns = lines[0]
        # validate another rows by nu,ber of columns. We are tying to avoid rows with different number of columns
        rows_of_the_valid_len = [x for x in lines if len(x) == len(columns)]

        return rows_of_the_valid_len
    except Exception as e:
        print("Exception in load_data: {}".format(str(e)))
        print(traceback.format_exc())


def clean_data(dataframe):
    """
    Data Cleaning: performs the following cleaning tasks:
        - Eliminate columns with non-numerical data
        - Eliminate all rows with missing values in any of the columns
        - Eliminate all rows with empty values on any of the columns
        - Eliminate all rows with duplicated values
        - Eliminate all empty rows.

    :param dataframe: input list of lists
    :return: dataframe cleaned
    """
    try:
        # first step - getting indexes of columns with all the numeric values.
        digit_columns_indexes = []

        for column_index in range(len(dataframe[0])):
            # merging all the data into one big string, replacing commas, spaces.
            columns_data = ''.join([x[column_index] for x in dataframe[1:]]).replace(',', '').replace('.', '').replace(
                ' ', '')
            # checking if the string is numeric
            if columns_data.isdigit():
                digit_columns_indexes.append(column_index)
        print("Indexes of columns with numerical data only:")
        print(digit_columns_indexes)

        # list of lists to store filtered dataframe
        cleaned_df = []
        i = 0

        # the quickest way to avoid duplicates is using a helper-dictionary
        duplicate_detector_dict = {}
        for row in dataframe:
            i += 1
            new_row = [row[i].strip() for i in digit_columns_indexes]
            # checking for duplicate and add to the final df only if the row if now a duplicate and has no empty cells
            try:
                duplicate_detector_dict[','.join(new_row)]
                continue
            except Exception:
                pass
            duplicate_detector_dict[','.join(new_row)] = ''
            # checking for empty cells
            if '' not in new_row:
                cleaned_df.append(new_row)
        print("Columns of the filtered dataframe: {}".format(str(cleaned_df[0])))
        print("Rows in the filtered dataframe: {}".format(len(cleaned_df)))
        return dataframe
    except Exception as e:
        print("Exception in clean_data: {}".format(str(e)))
        print(traceback.format_exc())


def get_parameters(command):
    """
    extracting number and column name from command
    :param command:
    :return:
    """
    try:
        # extracting a digit number, so 25 from Search (25, "DataSet")
        digit_number = command.split('Search (')[1].split(', "')[0]
        # extracting a columns name, so column1 from Search (25, "column1")
        column = command.split(', "')[1].split('")')[0]
        return digit_number, column
    except Exception as e:
        print("Exception in get_parameters: {}".format(str(e)))
        print(traceback.format_exc())


def validate_command(command, dataset):
    """
    checking if the column is valid
    :param command:
    :return:
    """
    try:
        # extracting column names
        columns = dataset[0]

        # checking if column structure is Search (N, "D")
        if 'Search (' not in command or ', "' not in command or '")' not in command:
            print("Command structure is wrong.")
            return False

        # extracting number and column name to validaate them
        digit_number, column = get_parameters(command)
        # validate number
        if not digit_number.replace(',', '').replace('.', '').strip().isdigit():
            print("Value {} is not a number. Please pass a numeric value as first parameter".format(digit_number))
            return False
        # validate column name
        if column not in columns and column != "DataSet":
            print('{} is not a valid column name. Please use "DataSet" if you want to search in the entire data set.'.format(column))
            return False
        return True
    except Exception as e:
        print("Exception in validate_command: {}".format(str(e)))
        print(traceback.format_exc())


def search_in_column(df, digit, column):
    """
    search value in column and print reports
    :param df:
    :param digit:
    :param column:
    :return:
    """
    try:
        # index by the column name
        column_index = df[0].index(column)

        # optimised version of
        # present_indexes = [df.index(x) for x in df if x[column_index] == digit]

        # here we are trying to find row indexes with some value
        present_indexes = []
        i = 0
        for row in df:
            if row[column_index] == digit:
                present_indexes.append(i)
            i += 1
        print("{} is present {} times in column {}.".format(digit, str(len(present_indexes)), column))

        # printing the detailed report
        if len(present_indexes) > 0:
            print("Details:\n*********************************")
            for index in present_indexes:
                print("{} is present in column  |{}|, row {}".format(digit, column, str(index)))
        return len(present_indexes)
    except Exception as e:
        print("Exception in search_in_column: {}".format(str(e)))
        print(traceback.format_exc())


def main():

    try:
        # print("Which file would you like to load?\n\t1. Boston_Lyft_Uber_Data\n\t2.InputDataSample\n\t3.Presentation")
        # if raw_input == "1":
        #     df = load_data(rideshare)
        # elif raw_input == "2":
        #     df = load_data(sample)

        clear_screen()
        # data load
        df = load_data(sample)
        print("Dataframe loaded")

        # data cleaning
        clean_df = clean_data(df)
        print("Dataframe cleaned\n")

        time.sleep(3)
        clear_screen()

        loop = True
        while loop:
            time.sleep(3.5)
            print_menu()
            choice = raw_input("Enter your choice [1-14, q, m, l or s]: ")
            if choice == "1":
                clear_screen()
                print "Count has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('Count         {a:<32d}    {b:<32d}'.format(a = my_count(), b = my_count()))
            elif choice == "2":
                clear_screen()
                print "Unique has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('Unique        {a:<32d}    {b:<32d}'.format(a = my_unique(), b = my_unique()))
            elif choice == "3":
                clear_screen()
                print "Mean has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('Mean          {a:<32d}    {b:<32d}'.format(a = my_mean(col_A), b = my_mean(col_B)))
            elif choice == "4":
                clear_screen()
                print "Median has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('Median        {a:<32d}    {b:<32d}'.format(a = my_median(col_A), b = my_median(col_B)))
            elif choice == "5":
                clear_screen()
                print "Mode has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('Mode          {a:<32s}    {b:<32s}'.format(a = my_mode(col_A), b = my_mode(col_B)))
            elif choice == "6":
                clear_screen()
                print "Standard Deviation (SD) has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('SD            {a:<30.2f}      {b:<30.2f}'.format(a = my_standard_deviation(col_A), b = my_standard_deviation(col_B)))
            elif choice == "7":
                clear_screen()
                print "Variance has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('Variance      {a:<30.2f}      {b:<30.2f}'.format(a = my_variance(col_A), b = my_variance(col_B)))
            elif choice == "8":
                clear_screen()
                print "Minimum has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('Minimum       {a:<32d}    {b:<32d}'.format(a = my_min(col_A), b = my_min(col_B)))
            elif choice == "9":
                clear_screen()
                print "20 Percentile (P20) has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('P20           {a:<32d}    {b:<32d}'.format(a = my_20P(col_A), b = my_20P(col_B)))
            elif choice == "10":
                clear_screen()
                print "40 Percentile (P40) has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('P40           {a:<32d}    {b:<32d}'.format(a = my_40P(col_A), b = my_40P(col_B)))
            elif choice == "11":
                clear_screen()
                print "50 Percentile (P50) has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('P50           {a:<32d}    {b:<32d}'.format(a = my_50P(col_A), b = my_50P(col_B)))
            elif choice == "12":
                clear_screen()
                print "60 Percentile (P60) has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('P60           {a:<32d}    {b:<32d}'.format(a = my_60P(col_A), b = my_60P(col_B)))
            elif choice == "13":
                clear_screen()
                print "80 Percentile (P80) has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                print('P80           {a:<32d}    {b:<32d}'.format(a = my_80P(col_A), b = my_80P(col_B)))
            elif choice == "14":
                clear_screen()
                print "Maximum has been selected!\n\n\n"
                print("Descriptor    Column A                            Column B")
                print("**********    ********                            ********")
                ('Maximum       {a:<32d}    {b:<32d}'.format(a = my_max(col_A), b = my_max(col_B)))
            elif choice == "q":
                os.system('cls' if os.name == 'nt' else 'clear')
                print "\n! P R O G R A M   T E R M I N A T E D !"
                print 39 * '-'
                sys.exit()
            elif choice == "m":
                #Add M key that allows user to go back to menu options.
                clear_screen()
                pass
            elif choice == "l":
                pass
            elif choice == 's':
                # Search data set
                print('Please enter Search (N, "D") command\nD can be a column name or "DataSet" if you want to search DataSet')
                print('Example: Search in column\n\t$ Search (25, "Column1")')
                print('Example: Search in data set\n\t$ Search (25, "DataSet")')

                # reading command in while loop
                while True:
                    command = raw_input("Please enter command\n")
                    # command validation
                    if validate_command(command, clean_df):
                        digit_number, column = get_parameters(command)
                        print('\nCommand is valid!\n')
                        # looking for value in some column
                        if column != "DataSet":
                            search_in_column(clean_df, digit_number, column)
                            break
                        else:
                            # looking for value in the entire dataset
                            print("Searching in the entire data set.")
                            total = 0
                            for column in df[0]:
                                total += search_in_column(clean_df, digit_number, column)
                            print("{} is present {} times in the data set.".format(digit_number, str(total)))
                            break
                    else:
                        print('Command is not valid! Please try again using Search (N, "D") structure')
            else:
                raw_input("Wrong option selection. Please enter any key to try again...")

    except Exception as e:
        print("Exception in main: {}".format(str(e)))
        print(traceback.format_exc())

# entry point of the script
if __name__ == "__main__":
    main()