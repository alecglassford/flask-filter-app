from helpers import get_restaurants

restaurants = get_restaurants()

def print_record_count():
    print('There are', len(restaurants), 'food establishments.')

if __name__ == '__main__':
    print_record_count()
