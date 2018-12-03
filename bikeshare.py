import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: 
    print('Hello! Let\'s explore some US bikeshare data!')
    # for city('chicago', 'new york city', 'washington' ):
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

        # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february',
                'march', 'april',
                'may', 'june', 'all']

    while True:
        month = input(str('\nWould you like to search by one of the following months?\nJanuary, February, March, April, May, June, or all?\n ').lower())
        if month in months:
            break
        else:
            print ('Your answer does not match any of the above options, please try again!\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
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
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main