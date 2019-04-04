# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:33:42 2018

@author: ACANTAMA
"""

cities = {
        'philadelphia': {
                'country': 'united states',
                'population': 1568000,
                'fact': 'It is the home of the Super Bowl 52 Champion Philadelphia Eagles.',
                },
        'auckland': {
                'country': 'new zealand',
                'population': 1377000,
                'fact': 'There are over 50 volcanoes in the city of Auckland.',
                },
        'seattle': {
                'country': 'united states',
                'population': 704532,
                'fact': 'It is the home of the Seattle Seahawks',
                },
            }
for city, facts in cities.items():
    print(city.title() + ':')
    country = facts ['country']
    population = facts['population']
    fact = facts['fact']
    
    print('\tCountry where this city is located: ' + country.title())
    print('\tPopulation: ' + str(population))
    print('\tInteresting fact: ' + fact)
