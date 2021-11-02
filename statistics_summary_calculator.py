# COURSE: CMPS 3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
# DATE: 11/01/2021
# STUDENT 1: Dominic Fanucchi
# STUDENT 2: 
# STUDENT 3: 
# DESCRIPTION: IMPLEMENTATION OF A STATISTICS SUMMARY CALCULATOR

# file imports
import dfanucchi as df

# importing csv module
import csv

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
	print("Total number of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are: ' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
	# parsing each column of a row
	for col in row:
		print("%10s"%col),
	print('\n')


df.say_hello()

