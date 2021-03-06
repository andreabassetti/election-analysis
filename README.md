# Election-Analysis

## Project Overview 
The purpose of this project is to help the election commission have a complete overview of the election results. They want the break down of the votes by county and candidates. Additionally, they want to know which county had the largest turn out and who the winner of the election is. 

## Election-Audit Results
- There were 369,711 total votes cast in this congressional election. 

- The breakdown of the number of votes and the percantage of total votes by county is as follows: Jefferson: 10.5% (38,855), Denver: 82.8% (306,055), and Arapahoe: 6.7% (24,801)

- Denver had the largest number of votes. 

- The breakdown of the number of votes and the percantage of total votes by candidate is as follows: Charles Casper Stockham: 23.0% (85,213) , Diana DeGette: 73.8% (272,892), and Raymon Anthony Doane: 3.1% (11,606) 

- Diana DeGette wont the election with a 73.8%  majority which was a total of 272,892 votes.

## Election Audit Summary: 
The code written to analyze this elections results should be considered to analyze any future election. With minimal manipulation, this code can process results in a very short period of time, giving the election committee answers quickly an accurately. There are two components of code that would need to be manipulated. Refer to the sections below to see where and how those manipulations should be conducted.  

### File Pathways
For the code to work, it needs to refer to the file where the election data is stored and the file where we want to save the results. It is essential that these lines of code be update with the new files, otherwise the code will not know where to pull data from and it will not work. The lines that need to be edited are shown below. 
- Line 9: `file_to_load = os.path.join("Resources", "election_results.csv")`
- Line 11: `file_to_save = os.path.join("analysis", "election_analysis.txt")`

There are three components to these lines, the variable, the command, and file pathway. The variables `file_to_load` and `files_to_save` MUST remain as they are. The command `= os.path.join` MUST remain as it is. The file pathway, is what needs the manipulation. Make sure to replace both the pathway and the file name correctly. 

### Column Index
For the code to work, it needs to refer to the correct column in excel. Given that not all of raw data from the election results is recorded in the same way, it is important to make sure that the code is pulling the right information. The lines that need to be edited are shown below. 
- Line 50: `candidate_name = row[2]`
- Line 53: `county_name = row[1]`

The only thing that needs manipulation in these lines of code are the numbers. Find the colomn in your source data with the relevant information and make sure that it matches the number displayed in the code (it should be the column number minus 1, since the first column will be 0). 

## Resources
- Data Source: election_results.csv
- Software: Python, 3.8.8, Visual Studio Code, 1.59.1

