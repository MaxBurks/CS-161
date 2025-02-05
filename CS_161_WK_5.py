#Max Burks
#2/5/25
#Week 5 homework assignment

#importing needed libraries
import requests

#setting variable to usr input through try except statement to validate data
try:
    usr_num = int(input('Enter an integer: '))
except ValueError:
    exit('Invalid input')

#using operand to check the remainder. if it is zero then the number is divisible by 5
if usr_num % 5 == 0:
    print('This number is divisible by 5.')
else:
    print('This number is not divisible by 5.')

#dictionary of states and capitals
state_cap = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
    }

#usr input for selecting a state. Should be properly formatted. Ex. Oregon
usr_state = input('Enter a State or Province (capitalized please): ')

#using if elif structure to check usr input against 6 different states
#print statement tells user who found what

print('If statement found:')
if usr_state == 'Oregon':
    print('Salem')
elif usr_state == 'Washington':
    print('Olympia')
elif usr_state == 'California':
    print('Sacramento')
elif usr_state == 'Minnesota':
    print('Saint Paul')
elif usr_state == 'Texas':
    print('Austin')
elif usr_state == 'Vermont':
    print('Montpelier')
else:
    print('State not found')

#spacing out each check and stating which one found what.
print('\nDictionary get() found')
#using .get() to iterate over the dictionary and print out the capital
print(state_cap.get(usr_state, 'State not found'))

#match casing  structure similar to if block, checking against same input and output
print('\nMatch Case found')
match usr_state:
    case 'Oregon':
        print('Salem')
    case 'Washington':
        print('Olympia')
    case 'California':
        print('Sacramento')
    case 'Minnesota':
        print('Saint Paul')
    case 'Texas':
        print('Austin')
    case 'Vermont':
        print('Montpelier')
    case _:
        print('State not found')

#function for calculating price a person would pay for pool usage
def pool_prices(age):
    '''This function determines what price a person would pay to enter a pool
        dependant on age.
        
        Peramiters
        ----------
        int: age
        
        Return
        ------
        int: num from if statement
        '''
    
    if age < 2:
        return 0
    
    elif age < 12:
        return 3
    
    elif age < 60:
        return 6
    
    else:
        return 4

#another variable set with try except for data validation, to be passed to the function pool_prices
try:
    age = int(input('Enter an age in the form of an integer: '))
    
except ValueError:
    exit('Invalid Input')

#receiving output from pool_prices with the argument of age
print(pool_prices(age))

#setting a variable with the requests library and getting the html of http://coccbobcat.com
#using try except to establish connection.
try:
    response = requests.get("http://coccbobcat.com")
except:
    exit('Unable to establish connection')

#setting var to 0 for counting purposes
count_160 = 0

#splitting the html into individual lines
lines = response.text.splitlines()

#iterating over said lines checking for '160'
#if there were multiple 160's in each line I would need to turn each line into a list, but I got lazy and it isn't needed
for line in lines:
    if '160' in line:
        count_160 +=1
#printing result of count    
print(f'The substring "160" appeared {count_160} times in the HTML source of http://coccbobcat.com.')