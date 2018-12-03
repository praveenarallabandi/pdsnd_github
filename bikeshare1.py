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
    #for city (chicago, new york city, washington): 
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

          
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('Selected city ' + city)
    print('Selected month ' + month)
    print('Selected day ' + day)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
if time == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # TO DO: display the most common day of week
if time == 'day_of_week':
        days = ['Monday', 'Tuesday', 
        'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday']
        for d in days:
            if day_of_week.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]
    # TO DO: display the most common start hour
def popular_hour(df):
    
          most_pop_hour = int(df['start_time'].dt.hour.mode())
          if most_pop_hour == 0:
            am_pm = 'am'
            pop_hour_readable = 12
          elif 1 <= most_pop_hour < 13:
            am_pm = 'am'
            pop_hour_readable = most_pop_hour
          elif 13 <= most_pop_hour < 24:
            am_pm = 'pm'
            pop_hour_readable = most_pop_hour - 12
            print('The most popular hour of day for start time is {}{},'.format(pop_hour_readable, am_pm))


    # TO DO: display most commonly used start station
def popular_stations(df):
    pop_start = df['start_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))
    
    # TO DO: display most commonly used end station
def popular_stations(df):
    pop_end = df['end_station'].mode().to_string(index = False)
    print('The most popular end station is {}.'.format(pop_end)) 

    # TO DO: display most frequent combination of start station and end station trip
def popular_trip(df):
     most_pop_trip = df['journey'].mode().to_string(index = False)
     print('The most popular trip is {}.'.format(most_pop_trip))


     # TO DO: display total travel time

def total_trvel_time(df):
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()
    # TO DO: display mean travel time
def mean_trip_duration(df):
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
def users(df):
   
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))

    # TO DO: Display counts of gender
def gender(df):
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))


    # TO DO: Display earliest, most recent, and most common year of birth
def birth_years(df):
    
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))


def main():
            while True:
                city, month, day = get_filters()
                print('Here...')
                df = load_data(city, month, day)
                print('Here...123123')
                time_stats(df)
                print('Here...after TimeStatus')
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break

                if __name__ == "__main__":
                    main()
