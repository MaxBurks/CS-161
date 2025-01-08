#Max Burks 01/06/2025
#Week one homework

#bringing in needed libraries for seconds in month 
from datetime import *
import calendar
#setting pet_name and pet_type to correct species and name
pet_name = "Hazel"
pet_type = "cat"

#using f strings to include both variables in the string
print(f"I have a {pet_type} and her name is {pet_name}")

#setting variables to user input, assuming correct information is input
first_name = input("Enter your first name: ")
current_age = int(input("Enter your current age: "))
yearly_savings = int(input("Enter your yearly savings: "))

#printing name, age, added age, savings, multiplied and divided through f-strings
print(f"""Hello {first_name}, you are {current_age} years old.
In ten years you will be {current_age + 10}.
If you save {yearly_savings} each year, in 5 years you will have saved {yearly_savings * 5}.
Your average monthly savings is {yearly_savings/12}""")

#setting variables to pull information out of datetime and calendar libraries
#full_date gets all current information
#month_name pulls the current name of the month from full_date ex January
#current_month takes the current month as an integer
#days uses the calendar library to find how many days are in the month that current_month passes to it
full_date = datetime.now()
month_name = (full_date.strftime('%B'))
current_month = int(full_date.strftime("%m"))
days = (calendar.monthrange(0, current_month))[1]

#f-string prints the name of the month and seconds in said month through multiplication
print(f"The number of seconds in {month_name} is {days * 24 * 60 * 60}")

#gathers integer input for egg science
egg_num = int(input("Enter the number of eggs: "))

#using // and % for integer division and remainder
print(f"This makes {egg_num // 12} dozen eggs, with {egg_num % 12} left over")
