import time
import pandas as pd
import numpy as np
from tabulate import tabulate

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

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City, or Washington? \n')
    while True:
        if city.lower() in ['chicago', 'new york city', 'washington']:
            city = city.lower()
            break
        else:
            city = input('Please choose from these options Chicago, New York City, or Washington. \n')

    # get the time frame that's user need to filter
    time_frame = input('Would you like to filter the data by month, day, both or not at all? \n')
    while True:
        if time_frame.lower() in ['month', 'day', 'both', 'not at all']:
            time_frame = time_frame.lower()
            break
        else:
            time_frame = input('Please choose from these options month, day, both or not at all.\n')
    
    # get user input for month (all, january, february, ... , june)
    def get_month():
        month = input('Which month - January, February, March, April, May, or June? \n')
        while True:
            if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june']:
                months = ['January', 'February', 'March', 'April', 'May', 'June']
                month = months.index(month.title()) + 1
                break
            else:
                month = input('Please choose from these options January, February, March, April May or June.\n')
        return month
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    def get_day():
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? \n')
        while True:
            if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                day = day.title()
                break
            else:
                day = input('Please choose from these options Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. \n')
        return day
    
    if time_frame.lower() == 'both':
        month = get_month()
        day = get_day()
        
    elif time_frame.lower() == 'month':
        month = get_month()
        day = 'all'
        
    elif time_frame.lower() == 'day':
        day = get_day()
        month = 'all'
    else:
        month = 'all'
        day = 'all'
        

    print('-'*40)
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
    # Read CSV File into DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Add Month and Day columns from Start Time column into DataFrame
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name

    # Filter DataFrame by Month
    if month != 'all':
        df = df[df['Month'] == month]

    # Filter DataFrame by Day
    if day != 'all':
        df = df[df['Day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month = months[most_common_month - 1]
    print('The Most Common Month:       ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['Day'].mode()[0]
    print('The Most Common Day of week: ', most_common_day)

    # TO DO: display the most common start hour
    # Create hour column from Start Time
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour:  ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The Most Common Start Station: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The Most Common End Station: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' To ' + df['End Station']
    most_freq_start_end_station = df['trip'].mode()[0]
    print('The Most Frequent Combination of Start and End Station Trip: ', most_freq_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time: ', total_travel_time, 'sec | ', total_travel_time/(60*60), 'hr')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Average Travel Time: ', mean_travel_time, 'sec | ', mean_travel_time/(60*60), 'hr')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_subscriber_users = df['User Type'].value_counts()[0]
    counts_of_customer_users = df['User Type'].value_counts()[1]
    print('The Count of Subscriber User: ' + str(counts_of_subscriber_users))
    print('The Count of Customer User:   ' + str(counts_of_customer_users))

    # TO DO: Display counts of gender
    # Check if Gender column exists in DataFrame
    if 'Gender' in df:
        counts_of_male_gender = df['Gender'].value_counts()[0]
        counts_of_female_gender = df['Gender'].value_counts()[1]
        print('The Count Gender of Male Users:   ' + str(counts_of_male_gender))
        print('The Count Gender of Female Users: ' + str(counts_of_female_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    # Check if Birth Year column exists in DataFrame
    if 'Birth Year' in df:
        # Calclate The Oldest 
        oldest = df['Birth Year'].min()
        print('The Oldest:  ', oldest)

        # Calclate The Youngest 
        youngest = df['Birth Year'].max()
        print('The Youngest:', youngest)

        # Calclate The Most Year Of Birth
        most_year_of_birth = df['Birth Year'].mode()[0]
        print('The Most Year Of Birth:', most_year_of_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):
    """
    Asks user if would like to see the raw data. If the user answers yes, 
    then print 5 rows of the data at a time, 
    then ask the user if they would like to see 5 more rows of the data..

    Returns:
        print rows of data if the user asked.
    """

    print('\nCalculating Display Raw data...\n')
    start_time = time.time()

    # Read CSV File into DataFrame
    df = pd.read_csv(CITY_DATA[city])
    row_num = 0
    while True:
        flag = input('\nWould you like to see raw data? Enter yes or no.\n')
        # Check If The User Enter Yes Or No Correct
        while True:
            if flag.lower() in ['yes', 'no']:
                flag = flag.lower()
                break
            else:
                flag = input('Please choose from these options yes, no. \n')
        # Check If The User Want To Display 5 New Rows Or Not
        if flag == 'no':
            break
        else:
            # use try and except : if the user arrive to the end of the data and df.loc[[i]] become out of range
            # tell the user that's a whole date and exit the loop
            try:
                for i in range(row_num, row_num + 5):
                    # tabulate fun for just make the data display friendly. resource https://pypi.org/project/tabulate/
                    print(tabulate(df.loc[[i]], headers='keys', tablefmt='plain'))
                    print('*'*124)
                row_num += 5
            except:
                print("This is the whole data. \n")
                break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        # Check If The User Enter Yes Or No Correct
        while True:
            if restart.lower() in ['yes', 'no']:
                restart = restart.lower()
                break
            else:
                restart = input('Please choose from these options yes, no. \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
