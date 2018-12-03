import time
import pandas as pd
import numpy as np
import collections
from datetime import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

class BikeShare:
    def __init__(self, city, month, day):
        self.city = city
        self.month = month
        self.day = day
        self.df = None
            
    def load_data(self):
        """
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """
        print('Printing city ' + self.city)
        print('Printing month ' + self.month)
        print('Printing day ' + self.day)

        headers = ['id', 'start_time', 'end_time', 'trip_duration', 'start_station', 'end_station', 'user_type', 'gender', 'birth_year']
        dtypes = {'id': 'str', 'start_time': 'str', 'end_time': 'str', 'trip_duration': 'str', 'start_station': 'str', 'end_station': 'str', 'user_type': 'str', 'gender': 'str', 'birth_year': 'str'}
        dateCols = ['start_time', 'end_time']
        
        if self.city == 'chicago':
            self.df = pd.read_csv("./chicago.csv", sep=',', header=None, names=headers, dtype=dtypes, parse_dates=dateCols)
            self.df['start_time'] = pd.to_datetime(self.df['start_time'], errors='coerce')
            self.df['trip_duration'] = pd.to_numeric(self.df['trip_duration'], errors='coerce')
            self.df['birth_year'] = pd.to_numeric(self.df['birth_year'], errors='coerce')
            print(self.df.head(5))

        if self.city == 'washington':
            self.df = pd.read_csv("./washington.csv", sep=',', header=None, names=headers, dtype=dtypes, parse_dates=dateCols)
            self.df['start_time'] = pd.to_datetime(self.df['start_time'], errors='coerce')
            self.df['trip_duration'] = pd.to_numeric(self.df['trip_duration'], errors='coerce')
            self.df['birth_year'] = pd.to_numeric(self.df['birth_year'], errors='coerce')
            print(self.df.head(5))

        if self.city == 'new york':
            self.df = pd.read_csv("./new_york_city.csv", sep=',', header=None, names=headers, dtype=dtypes, parse_dates=dateCols)
            self.df['start_time'] = pd.to_datetime(self.df['start_time'], errors='coerce')
            self.df['trip_duration'] = pd.to_numeric(self.df['trip_duration'], errors='coerce')
            self.df['birth_year'] = pd.to_numeric(self.df['birth_year'], errors='coerce')
            print(self.df.head(5))
        # return df // TODO 

    def time_stats(self, df):
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
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            for d in days:
                if day_of_week.capitalize() in d:
                    day_of_week = d
                df = df[df['day_of_week'] == day_of_week]
        
    # TO DO: display the most common start hour
    def popular_hour(self):
        print(self.df['start_time'].dt.hour.mode())
        most_pop_hour = int(self.df['start_time'].dt.hour.mode())
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
    def popular_stations(self):
        pop_start = self.df['start_station'].mode().to_string(index = False)
        print('The most popular start station is {}.'.format(pop_start))
        
    # TO DO: display most commonly used end station
    def popular_trip(self):
        most_pop_trip = self.df['end_station'].mode().to_string(index = False)
        print('The most popular trip is {}.'.format(most_pop_trip))


    # TO DO: display total travel time
    def total_trvel_time(self):
        total_travel_time = self.df['trip_duration'].sum()
        print('The trip total time is {}'.format(total_travel_time))
        
    # TO DO: display mean travel time
    def mean_trip_duration(self):
        mean_travel_time = self.df['trip_duration'].mean()
        print('The mean trip total time is {}'.format(mean_travel_time))

    def user_stats(self):
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

    # TO DO: Display counts of user types
    def users(self):
        subs = self.df.query('user_type == "Subscriber"').user_type.count()
        cust = self.df.query('user_type == "Customer"').user_type.count()
        print('There are {} Subscribers and {} Customers.'.format(subs, cust))

    # TO DO: Display counts of gender
    def gender(self):
        male_count = self.df.query('gender == "Male"').gender.count()
        female_count = self.df.query('gender == "Male"').gender.count()
        print('There are {} male users and {} female users.'.format(male_count, female_count))


    # TO DO: Display earliest, most recent, and most common year of birth
    def birth_years(self):
        earliest = int(self.df['birth_year'].min())
        latest = int(self.df['birth_year'].max())
        mode = int(self.df['birth_year'].mode())
        print('The oldest users are born in {}.\nThe youngest users are born in {}.'
            '\nThe most popular birth year is {}.'.format(earliest, latest, mode))

# Starting execution here
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!') 
    while True:
        city = input(str('\nWhich city would you like to see data on?New York City, Chicago, or Washington?\n ').lower())
        if city in ('washington', 'chicago', 'new york city'):
            break
        elif city == 'new york':
            city += ' city'
            break
        else:
            print('\n\nYour answer does not match any of the above options, please try again!\n')

        # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february','march', 'april','may', 'june', 'all']
    while True:
                month = input(str('\nWould you like to search by one of the following months?\nJanuary, February, March, April, May, June, or all?\n ').lower())
                if month in months:
                    break
                else:
                    print ('Your answer does not match any of the above options, please try again!\n')
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday','wednesday, thursday, friday','saturday', 'sunday']
    while True:
                day = input(str('\nWould you like to search by one of the following days?\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all of them?\n' ).lower())
                if day in days:
                    break
                else:
                    print ('Your answer does not match any of the above options, please try again!\n')
                    #return city, month, day      

    bikeShare = BikeShare(city, month, day)
    bikeShare.load_data()
    bikeShare.popular_hour()
    bikeShare.popular_stations()
    bikeShare.popular_trip()
    bikeShare.total_trvel_time()
    bikeShare.mean_trip_duration()
    bikeShare.users()
    bikeShare.gender()
    bikeShare.birth_years()

def main():
    get_filters()

if __name__== "__main__":
  main()