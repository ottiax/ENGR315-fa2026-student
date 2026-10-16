import sys


"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###
import sys



# Being able to Determine the pathway to NYT COVID data and utilization of the print function.

data = parse_nyt_data("data/covid/us-counties.csv")

print("Number of records:", len(data))



# Letting the program analyze only the records and data category i need  :
# Harrisonburg City, Virginia
# Rockingham County, Virginia

harrisonburg = []
rockingham = []

for entry in data:

    date = entry[0]
    county = entry[1]
    state = entry[2]
    cases = entry[4]

    if state == "Virginia" and county == "Harrisonburg city":
        harrisonburg.append((date, cases))

    elif state == "Virginia" and county == "Rockingham":
        rockingham.append((date, cases))


# Sort the records by date
harrisonburg.sort()
rockingham.sort()



# QUESTION 1
# Find the first positive cases in Harrisonburg and Rockingham County

harrisonburg_first_case = None

for date, cases in harrisonburg:
    if cases > 0:
        harrisonburg_first_case = date
        break


rockingham_first_case = None

for date, cases in rockingham:
    if cases > 0:
        rockingham_first_case = date
        break


print("\nQUESTION 1")
print("First positive case in Harrisonburg:", harrisonburg_first_case)
print("First positive case in Rockingham County:", rockingham_first_case)



# QUESTION 2
# Find the date with the greatest number of NEW cases


# Harrisonburg 

harrisonburg_max_new_cases = -1
harrisonburg_max_new_date = None

previous_cases = 0

for date, cumulative_cases in harrisonburg:

    new_cases = cumulative_cases - previous_cases

    if new_cases > harrisonburg_max_new_cases:
        harrisonburg_max_new_cases = new_cases
        harrisonburg_max_new_date = date

    previous_cases = cumulative_cases


#  Rockingham County 

rockingham_max_new_cases = -1
rockingham_max_new_date = None

previous_cases = 0

for date, cumulative_cases in rockingham:

    new_cases = cumulative_cases - previous_cases

    if new_cases > rockingham_max_new_cases:
        rockingham_max_new_cases = new_cases
        rockingham_max_new_date = date

    previous_cases = cumulative_cases


print("\nQUESTION 2")
print("Harrisonburg greatest number of new cases:",
      harrisonburg_max_new_cases,
      "on",
      harrisonburg_max_new_date)

print("Rockingham County greatest number of new cases:",
      rockingham_max_new_cases,
      "on",
      rockingham_max_new_date)



# QUESTION 3
# Find the worst seven-day period of new cases in Harrisonburg and Rockingham County


# First create a (date, new_cases) list using the formula from question 2:

harrisonburg_new_cases = []

previous_cases = 0

for date, cumulative_cases in harrisonburg:

    new_cases = cumulative_cases - previous_cases

    harrisonburg_new_cases.append((date, new_cases))

    previous_cases = cumulative_cases


rockingham_new_cases = []

previous_cases = 0

for date, cumulative_cases in rockingham:

    new_cases = cumulative_cases - previous_cases

    rockingham_new_cases.append((date, new_cases))

    previous_cases = cumulative_cases



# determine the worst days of new cases in Harrisonburg

harrisonburg_worst_total = -1
harrisonburg_worst_start = None
harrisonburg_worst_end = None

for i in range(len(harrisonburg_new_cases) - 6):

    seven_day_total = 0

    for j in range(7):
        seven_day_total += harrisonburg_new_cases[i + j][1]

    if seven_day_total > harrisonburg_worst_total:

        harrisonburg_worst_total = seven_day_total

        harrisonburg_worst_start = harrisonburg_new_cases[i][0]

        harrisonburg_worst_end = harrisonburg_new_cases[i + 6][0]



# same for Rockingham County 


rockingham_worst_total = -1
rockingham_worst_start = None
rockingham_worst_end = None

for i in range(len(rockingham_new_cases) - 6):

    seven_day_total = 0

    for j in range(7):
        seven_day_total += rockingham_new_cases[i + j][1]

    if seven_day_total > rockingham_worst_total:

        rockingham_worst_total = seven_day_total

        rockingham_worst_start = rockingham_new_cases[i][0]

        rockingham_worst_end = rockingham_new_cases[i + 6][0]


print("\nQUESTION 3")

print("Harrisonburg worst seven-day period:",
      harrisonburg_worst_start,
      "to",
      harrisonburg_worst_end)

print("Total new cases:",
      harrisonburg_worst_total)


print("Rockingham County worst seven-day period:",
      rockingham_worst_start,
      "to",
      rockingham_worst_end)

print("Total new cases:",
      rockingham_worst_total)