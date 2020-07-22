#This is the file for the class rideshare_city

import pandas as pd

class rideshare_city:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.df['Start Time'] = pd.to_datetime(self.df['Start Time'])
        self.df['End Time'] = pd.to_datetime(self.df['End Time'])
        self.df['Month'] = self.df['Start Time'].dt.month
        self.df['Day'] = self.df['Start Time'].dt.dayofweek
        self.df['Hour'] = self.df['Start Time'].dt.hour
        self.df['Duration'] = self.df['End Time'] - self.df['Start Time']

    def common_month(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        return months[self.df['Month'].mode()[0]-1]
 
    def common_day(self):
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        return days[self.df['Day'].mode()[0]-1]
    
    def common_hour(self):
        '''Returns the most common hour of day for 'Start Time''''
        return self.df['Hour'].mode()[0]-1

    def common_start_station(self):
        return self.df['Start Station'].mode()[0]

    def common_end_station(self):
        return self.df['End Station'].mode()[0]

    def common_itinerary(self):
        '''returns most common trip from start to end (i.e., most frequent combination of start station and end station)'''
        return self.df[['Start Station', 'End Station']].mode()

    def total_travel_time(self):
        return self.df['Duration'].sum()
            
    def average_travel_time(self):
        return self.df['Duration'].mode()[0]

    def user_count_type(self):        
        '''counts of each user type'''
        return dict((self.df.groupby('User Type')['User Type'].count()))

    def gender_count(self):
        '''counts of each gender (only available for NYC and Chicago)'''     
        try: return dict((self.df.groupby('Gender')['Gender'].count()))
        except KeyError: return 'Sorry, that data may not be available for this city.'

    def earliest_birth_year(self):
        '''earliest year of birth (only available for NYC and Chicago)'''        
        try: return self.df['Birth Year'].min()
        except KeyError: return 'Sorry, that data may not be available for this city.'

    def most_recent_birth_year(self):
        try: return self.df['Birth Year'].max()
        except KeyError: return 'Sorry, that data may not be available for this city.'

    def most_common_yob(self):
         '''most common year of birth (only available for NYC and Chicago)'''
         try: return self.df['Birth Year'].mode()[0]
         except KeyError: return 'Sorry, that data may not be available for this city.'

    def raw_data_chunks(self):
        '''Yields chunks of 5 rows'''
        for i in range(0, len(self.df), 5):
            yield self.df[i: i+5]
    
        
# if __name__ == "__main__":
#     city = rideshare_city('Python\Explore US Bikeshare Data\chicago.csv')
    
#     # print(f'The most common month: {city.common_month()}')
#     # print(f'The most common city: {city.common_day()}')
#     # print(f'The most common hour: {city.common_hour()}')
#     # print(f'The most common start station: {city.common_start_station()}')
#     # print(f'The most common end station: {city.common_end_station()}')
#     # print(f'The most common itinerary: {city.common_itinerary()}')
#     # print(f'Total travel time: {city.total_travel_time()}')
#     # print(f'Average travel time: {city.average_travel_time()}')
#     # print(f'Counts of each user type: \n{city.user_count_type()}')
#     # print(f'The gender breakdown is as follows: {city.gender_count()} \n')
#     # print(f'Earliest Year of Birth: {city.earliest_birth_year()}')
#     # print(f'The most recent year of birth is : {city.most_recent_birth_year()} \n')
#     # print(f'The most common year of birth is : {city.most_common_yob()} \n')
