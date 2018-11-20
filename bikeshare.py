mport time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('\n\nHello! Let\'s explore some US bikeshare data!')

    while True:
        city = input(str('\nWhich city would you like to see data on?'
'New York City, Chicago, or Washington?\n ').lower())
        if city in ('washington', 'chicago', 'new york city'):
            break
        elif city == 'new york':
            city += ' city'
            break
        else:
            print('\n\nYour answer does not match any of the above options, please try again!\n')


    months = ['january', 'february',
            'march', 'april',
            'may', 'june', 'all']

    while True:
        month = input(str('\nWould you like to search by one of the following months?\nJanuary, February, March, April, May, June, or all?\n ').lower())
        if month in months:
            break
        else:
            print ('Your answer does not match any of the above options, please try again!\n')

    days = ['all', 'monday', 'tuesday',
    'wednesday, thursday, friday',
    'saturday', 'sunday']

    while True:
        day = input(str('\nWould you like to search by one of the following days?\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all of them?\n' ).lower())
        if day in days:
            break
        else:
            print ('Your answer does not match any of the above options, please try again!\n')
return city, month, day
    print('-'*40)
