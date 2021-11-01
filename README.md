# Statistics-Summary-Calculator-for-Descriptive-Data
CSUB CMPS 3500 Fall 2021 Group Project

### Requirements 
Your Statistics Summary Calculator should have the following features:

1. <b>Data Loading:</b> Your program should read data from csv files, Note that the input list will have up to 10 columns and one million rows and could be unordered and contain repeated, missing, incorrect and or misleading values. Test your function with the following data sets:
        <ul>
          <li>InputDataSample.csv</li>
          <li>Boston_Lyft_Uber_Data.csv</li>
        </ul>

2. <b>Data Cleaning:</b> Your program should be able to perform the follwing cleaning tasks:
	<ul>
		<li>Load the csv file and stored into an array or data frame</li>
        <li>Eliminate columns with non-numerical data</li>
        <li>Eliminate all rows with missing values in any of the columns</li>
        <li>Eliminate all rows with empty values on any of the columns</li>
        <li>Eliminate all rows with duplicated values</li>
        <li>Eliminate all empty rows.</li>
	</ul>

3. <b>Function implementation:</b> All functions must be implemented by the team, predesigned libraries like pandas or scikit-learn may not be used

4. <b>Searching capability:</b> Your program should have an option <b>search any element</b> in a given column or in the entire data set. <br>Example: Search in column</br>
			
		$ Search (25, "Column1")
        25 is present 12 times in column Column1.
        Details:
        *********************************
        25 is present in Column 1 row 25
        25 is present in Column 1 row 365
        .
        .
        .

    Example: Search in data set

        $ Search (25, "DataSet")
        25 is present 31 times in the data set.
        Details:
        *********************************
        25 is present in Column 1 row 25
        25 is present in Column 1 row 365
        .
        .
        25 is present in Column 2 row 1182
        .
        .
        .

#### Statistical Operations
You calculator should output the following statistical operations:
	<ul>
    	<li>Count</li>
    	<li>Unique</li>
    	<li>Mean</li>
    	<li>Median</li>
    	<li>Mode</li>
    	<li>Standard Deviation (SD)</li>
    	<li>Variance</li>
    	<li>Minimum</li>
    	<li>20 Percentile (P20)</li>
    	<li>40 Percentile (P40)</li>
    	<li>50 Percentile (P50)</li>
    	<li>60 Percentile (P60)</li>
    	<li>80 Percentile (P80)</li>
		<li>Maximum</li>
	</ul>

#### Output the results

The output of the data summary for InputDataSample.csv should look like this:

    Descriptor    Column A    Column B   ...
    **********    ********    ********
    Count             .           .
    Unique            .           .
    Mean
    Median
    Mode
    SD
    .
    .
    .

### General Guidelines
<ul>
	<li>All opeartions should be implemented by the students</li>
	<li>Identify all group members in the header of the main part of each code, this is an example in phyton.</li>
</ul>

       # course: cmps3500
       # CLASS Project
       # PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
       # date: 09/10/09
       # Student 1: John Smith
       # Student 2: Juan Garcia
       # description: Implementation of a statistics summary Calculator
     
<ul>
	<li>Use meaningful names and avoid made-up acronyms and maintain naming conventions which are uniform throughout.</li>
	<li>Use comments wisely, comments should not explain step by step what the code is doing, comments should be cleverly </li>
    placed to say WHY something has been coded in a certain way. The name of something is informative about when 
    and how to use the object.</li>
	<li>Test your code. Tests serve as an executable specification of the code and examples of its use.</li>
	<li>Keep you code simple. Good code is not "clever". It does things in straightforward, obvious ways</li>
</ul>
	
#### Error handling should be implemented
Ask yourself some of the following questions:
<ul>
    <li>What would happen I get a file that is corrupted?</li>
    <li>What if 2 of the columns don't have the same number of rows?</li>
    <li>What if the programs takes too much to load the data set?</li>
    <li>What if you divide by zero?</li>
    <li>What if there is an error in one of the formulas?</li>
</ul>
Your program should display an error message whenever an illegal input or operation happens.


### A Graphic Interface is expected but not required
