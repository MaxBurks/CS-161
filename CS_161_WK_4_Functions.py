import csv

def average(num1,num2,num3) -> int:
    '''this function returns an averaged number in an int based on 3 integer inputs
        Parameters
        ----------
        int: num1
        int: num2
        int: num3
        
        Return
        ------
        int: number average
        '''
    return (num1+num2+num3)/3

def dog_human_age(dog_age) -> int:
    '''this function returns a human equivalent of dog years in an int based on 1 integer input
        Parameters
        ----------
        int: dog_age
        
        Return
        ------
        int: human years
    '''
    return 24+(dog_age-2)*4


def current_car_value(price,year,car_type) -> str:
    '''This function returns the value of a car in an int based on 2 integer inputs and one string input
        Parameters
        ----------
        int: price
        int: year
        str: car_type
        
        Return
        ------
        str: car value
    '''
    
    car_value = price
    
    if car_type == 'German':
        for year_passed in range(year):
            car_value -= car_value*.05
        return('The value of the ' + car_type + ' car will be $' + str(round(car_value,2)) + ' after ' +str(year) + ' years')
    elif car_type == 'Japanese':
        for year_passed in range(year):
            car_value -= car_value*.07
        return('The value of the ' + car_type + ' car will be $' + str(round(car_value,2)) + ' after ' +str(year) + ' years')
    elif car_type == 'Italian':
        for year_passed in range(year):
            car_value += car_value*.05
        return('The value of the ' + car_type + ' car will be $' + str(round(car_value,2)) + ' after ' +str(year) + ' years')
    
    else:
        return('Received an invalid input')

def dog_to_human_2() -> str:
    '''this function prints out a predetermined statement in a str

        Parameters
        ----------
        no real parameters are passed to the function
        
        Return
        ------
        print statement

    '''
    print('Your Spot is 22.3 years old')
    
def ice_cream_price(scoops) -> str:
    '''this function returns the cost of an ice cream in a str based on 1 integer input
        Parameters
        ----------
        int:scoops
        
        Return
        ------
        str: total scoop cost
    
    '''
    scoop_cost = scoops * 1.15 +2.25
    return('A ' + str(scoops) + '-scoop cone will cost $' + str(scoop_cost))
    
def historical_ice_cream(month,year) -> str:
    '''this function returns the cost of an ice cream in a str based on 1 string input and 1 integer input
        Parameters
        ----------
        str: month
        int: year
        
        Return
        ------
        str: ice cream cost
    '''

    try:
        with open('ice cream price index.csv') as month_index:
            month_iterator = csv.reader(month_index)
            for row in month_iterator:
                for cell in row:
                    if month == cell:
                        set_month = row.index(month)
                        
        with open('ice cream price index.csv') as year_index:
            year_iterator = csv.reader(year_index)
            for row in year_iterator:
                if year in (row[0]):
                    set_year = row[0]
        
        with open('ice cream price index.csv') as price_cream:
            price = csv.reader(price_cream)
            for row in price:
                if set_year in row[0]:
                    return (str(row[set_month]))
    except FileNotFoundError:
        exit('file not found. check github @ https://github.com/MaxBurks/CS-161')
        
if __name__ == '__main__':
    print(historical_ice_cream('Apr','2018'))