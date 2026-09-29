'''
Partner Names: Yousef & Pavan
'''

# Part 1:

#Create a file named “dow.py” and inside, create a function that takes three parameters called `getDayOfTheWeek(year, month, day)`.
year = ""
month = "" 
day = ""

def main():
    user_option = input("Pick an option: \n1. Get the day of the week\n2. Make a Calender\n--> ")
    if user_option == "1":
        getDayOfTheWeek(year, month, day)
    else:
        print("error")

def getDayOfTheWeek(year, month, day): 

#March 03, 2027
    
    user_date = input("Enter a date: ").strip()
    if "," not in user_date:
        print("Please enter a valid date")
        return
    month_day, year_string = user_date.strip().split(",")
    year = int(year_string)
    elements = month_day.strip().split()
    if len(elements) != 2:
        print("Please enter a valid date")
        return
    month_name = elements[0].lower()
    day = int(elements[1])

    months = [
        {'month': "january", 'month_value': 1},
        {'month': "february", 'month_value': 2},
        {'month': "march", 'month_value': 3},
        {'month': "april", 'month_value': 4},
        {'month': "may", 'month_value': 5},
        {'month': "june", 'month_value': 6},
        {'month': "july", 'month_value': 7},
        {'month': "august", 'month_value': 8},
        {'month': "september", 'month_value': 9},
        {'month': "october", 'month_value': 10},
        {'month': "november", 'month_value': 11},
        {'month': "december", 'month_value': 12},
    ]

    month_value = None

    for item in months:
        if item['month'] == month_name:
            month_value = item['month_value']
            break

    if month_value is None:
        print("Invalid Month")
        return


    monthCodes = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    monthCode = monthCodes[month_value - 1]
    if leapyear == True:
        monthCode
    day_of_week = [
        {'day': "Saturday", 'day_value': 0},
        {'day': "Sunday", 'day_value': 1},
        {'day': "Monday", 'day_value': 2},
        {'day': "Tuesday", 'day_value': 3},
        {'day': "Wednesday", 'day_value': 4},
        {'day': "Thursday", 'day_value': 5},
        {'day': "Friday", 'day_value': 6},
    ]
    
    yearLastTwoDigits = year % 100
    numberOfTwelves = yearLastTwoDigits // 12
    remainder = yearLastTwoDigits % 12
    numberOfFours = remainder // 4

    if isLeapYear(year) and (month_value == 1 or month_value == 2):
        monthCode = monthCode - 1

# if 1600

    dow_calculation = (remainder + numberOfTwelves + numberOfFours + day + monthCode) % 7
    for item in day_of_week:
        if item['day_value'] == dow_calculation:    
            dow_final = item['day']
            break


    print(f"month: {month_value} year: {year} day: {day}")
    print(f"month code: {monthCode}")
    print(f"dow = {dow_final}")



def isLeapYear(year):
    if year % 400 == 0:
        leapyear = True
    elif year % 100 == 0:
        leapyear = False
    elif year % 4 == 0:
        leapyear =  True
    else: 
        leapyear = False
    

main()



