import sys

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
# enter ode here

data = parse_nyt_data("data/covid/us-counties.csv")

print("numbers of record",len(data))

# Letting the program analyze only the records and data category i need  :
# Harrisonburg City, Virginia
# Rockingham County, Virginia

harrisonburg = []
rockingham = []

for entry in data:
    date = entry [0]
    county = entry [1]
    state = entry [2]
    cases = entry [4]

    if state == "Virginia" and county == "Harrisonburg":
        harrisonburg.append((date, cases))

    elif state == "Virginia" and county == "Rockingham":
        rockingham.append((date, cases))

# sort the record by date
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
for date,cases in rockingham:
    if cases > 0:
        rockingham_first_case = date
        break

print("\nQuestion 1")
print("Harrisonburg first recorded case was on", harrisonburg_first_case)
print("Rockingham first recorded case was on", rockingham_first_case)
    
 