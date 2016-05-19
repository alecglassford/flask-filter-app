import csv
from collections import defaultdict
from os import path

# Data is from https://data.kingcounty.gov/Health/Food-Establishment-Inspection-Data/f29f-zza5
# filtered to only collect inspections from after 2015 onward
csv_path = path.join('static', 'data', 'inspections.csv')

def get_restaurants():
    """
    Structure of the returned restaurants dictionary:

    restaurant name maps to a dictionary whose keys are inspection ids
    each inspection id maps to a list of violations form that inspection

    restaurant name --> inspection(sorted by date) --> list of of violations
    """
    restaurants = defaultdict(lambda: defaultdict(list))
    with open(csv_path, newline='') as csv_file:
        inspections_reader = csv.DictReader(csv_file)
        for violation in inspections_reader:
            name = violation['Name'].upper()
            date = violation['Inspection Date']
            restaurants[name][date].append(violation)
    return restaurants
