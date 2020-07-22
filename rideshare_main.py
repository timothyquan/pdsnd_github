#This is the main file to run

from rideshare_city import rideshare_city
from time import sleep

class rideshare_interface:
    def __init__(self, cities):
        running = True     
        print('Hello, and welcome and welcome to the bikeshare data exploration app! \n')    
        while running:
            print(f'Data is available for the following cities: \n')
            for key,city in enumerate(tuple(cities.items())):
                print(f'{key+1} for {city[0]}')
            city_idx = input(f'\nEnter  {list(range(1, len(cities)+1))} for one of the above cities, or x to exit: ')
            
            if city_idx.lower() == 'x': break
            
            filename = ''
            try: filename = tuple(cities.items())[int(city_idx) - 1][1]
            except: 
                print('You have made an invalid selection.\n\n')
                sleep(1)
            if filename != '':
                print('Loading...\n')
                city = rideshare_city(filename)
                self.__category_questions(city)

    def __category_questions(self, city):

        running = True
        while running == True:
            print('We can can look at the following types of data:\n\n')
            print('1 Popular times of travel. ie, occurs most often in the start time')
            print('2 Popular stations and trip')
            print('3 Trip duration')
            print('4 User infomation')
            print('5 Print raw data')
            selection = input('Enter 1-4 for any of the above or 0 to return to the previous menu: ')
            
            try: int(selection)
            except: selection = 6
            if int(selection) == 1:
                self.__time_questions(city)
            elif int(selection) == 2:
                self.__station_questions(city)
            elif int(selection) == 3:
                self.__duration_questions(city)
            elif int(selection) == 4:
                self.__user_questions(city)
            elif int(selection) == 5:
                for items in city.raw_data_chunks():
                    print(items)
                    if '0' == input('Press enter to see more or 0 to return to the previous menu:'):
                        break
            elif int(selection) == 0:
                running = False
            else:
                print('You have made an invalid selection.\n\n')
                sleep(1)
            
    def __time_questions(self, city):
        running = True
        while running == True :   
            print('\n1 Most Common Month')
            print('2 Most common day of week')
            print('3 most common hour of the day\n')
            
            selection = input('Enter 1-3 to view any of the above data, press 0 to return to the previous menu: ')
            
            
            try: int(selection)
            except: selection = 4
            if int(selection) == 1:
                print(f'\nThe busiest month was {city.common_month()}.')
            elif int(selection) == 2:
                print(f'\n{city.common_day()} was the most common day.')
            elif int(selection) == 3:
                print(f'\nOverall, rides started most frequently during this hour: {city.common_hour()}')
            elif int(selection) == 0:
                running = False
            sleep(1)

    def __station_questions(self, city):
        running = True
        while running == True :   
            print('\n1 Most common start station')
            print('2 Most common end station')
            print('3 Most common itinerary \n')
            
            selection = input('Enter 1-3 to view any of the above data, press 0 to return to the previous menu: ')
            
            
            try: int(selection)
            except: selection = 4
            if int(selection) == 1:
                print(f'\nThe most common start station {city.common_start_station()}.')
            elif int(selection) == 2:
                print(f'\n{city.common_end_station()} was the most common end station.')
            elif int(selection) == 3:
                print(f'The following was the most common itinerary: \n{city.common_itinerary()}')
            elif int(selection) == 0:
                running = False
            sleep(1)

    def __duration_questions(self, city):
        running = True
        while running == True :   
            print('\n1 Total time overall travelled')
            print('2 Average travel time per trip')
           
            selection = input('Enter 1-2 to view any of the above data, press 0 to return to the previous menu: ')
            
            
            try: int(selection)
            except: selection = 3
            if int(selection) == 1:
                print(f'\nThe overall time travelled was {city.total_travel_time()}.')
            elif int(selection) == 2:
                print(f'\n{city.average_travel_time()} was average trip duration.')
            elif int(selection) == 0:
                running = False
            sleep(1)

    def __user_questions(self, city):
        running = True
        while running == True :   
            print('\n1 Count of each user type')
            print('2 Count of each gender (only available for NYC and Chicago)')
            print('3 Earliest birth year (only available for NYC and Chicago)')
            print('4 Most recent birth year (only available for NYC and Chicago)')
            print('5 Most common birth year (only available for NYC and Chicago)')

           
            selection = input('Enter 1-5 to view any of the above data, press 0 to return to the previous menu: ')
            
            try: int(selection)
            except: selection = 7
            if int(selection) == 1:
                print(f'The user type breakdown is as follows: \n {city.user_count_type()}.')
            elif int(selection) == 2:
                print(f'The following is a breakdown of the user genders: \n{city.gender_count()}')
            elif int(selection) == 3:
                print(f'The following is the earliest birth year: \n{city.earliest_birth_year()} .')
            elif int(selection) == 4:
                print(f'The following is the recent birth year: \n{city.most_recent_birth_year()}')
            elif int(selection) == 5:
                print(f'The following is the most common birth year:\n{city.most_common_yob()} was average trip duration.')
            elif int(selection) == 0:
                running = False
            sleep(1)


if __name__ == "__main__":
    cities =  {'Chicago': 'Python\Explore US Bikeshare Data\chicago.csv',
              'New York City': 'Python\Explore US Bikeshare Data\\new_york_city.csv',
              'Washington': 'Python\Explore US Bikeshare Data\washington.csv' }

    rideshare_interface(cities)
