# Practice Problem #3: Load and Filter the Dataset
# This is a bit of a bigger task, which involves choosing a dataset to load and filtering it based on a specified month and day. 
# In the quiz below, you'll implement the load_data() function, which you can use directly in your project. There are four steps:

# Load the dataset for the specified city. Index the global CITY_DATA dictionary object to get the corresponding filename for the given city name.
# Create month and day_of_week columns. Convert the "Start Time" column to datetime and extract the month number and weekday name into separate columns 
# using the datetime module.
# Filter by month. Since the month parameter is given as the name of the month, you'll need to first convert this to the corresponding month number. 
# Then, select rows of the dataframe that have the specified month and reassign this as the new dataframe.
# Filter by day of week. Select rows of the dataframe that have the specified day of week and reassign this as the new dataframe. 
# (Note: Capitalize the day parameter with the title() method to match the title case used in the day_of_week column!)

import pandas as pd

CITY_DATA = { 'chicago': 'Python\Explore US Bikeshare Data\chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
    df - pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # filter by month if applicable
    if not month.lower() == 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        df = df[df['Start Time'].dt.month == months.index(month) + 1]

    if not day.lower() == 'all':
        #df = df[df['Start Time'].dt.day == months.index(month) + 1]
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        df = df[df['Start Time'].dt.dayofweek == days.index(day) + 1]

    return df


df = load_data(CITY_DATA['chicago'], 'march', 'friday')
print(df)
