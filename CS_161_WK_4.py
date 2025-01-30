from CS_161_WK_4_Functions import *
#importing python file containing the functions

#The script will not run if the functions are called before they are defined

#calling function named average from imported file
#function calculates the average of the three numbers passed
#try changing the numbers to see the average change!
print(average(7,5,9))
print(average(6,6,7))

#print(num1)
#this will not work since the parameter was only declared in the function and not in the main program

#calling the function named dog_human_age from imported file
#calculates a dogs equivalent age in human years
#try passing a different number to see their age change!
print(dog_human_age(5))
print(dog_human_age(11))

#calling the function named car_value from imported file
#calculates the value of a car based on inital cost, how old the car is, and what type of car
#try passing a different type of car to see the different value after 5 years when the initial value was $10000
print(current_car_value(10000,5,input('What type of car do you have. German, Italian, or Japanese? ')))

#creating two variables that are passed to the function dog_to_human_2
#these two variables have no real use if I am reading the instructions properly
dog_name = (input('What is your dog\'s name? '))
dog_age = input('How old is Spot? ')

#according to the instructions, the function should always print the same string
#If I did understand it wrongly \_(._.)_/
dog_to_human_2()

#calling function ice_cream_price and passing an int
print(ice_cream_price(int(input('How many scoops would you like? '))))

#declairing variables for historical_ice_cream
months = input('enter a month, ex April: ')[:3]
years = input('enter a year from 1988 to 2024, ex 2018: ')

#calling historical_ice_cream
print('Ice cream cost $' + historical_ice_cream(months,years) + ' per half gallon in the year ' + years)