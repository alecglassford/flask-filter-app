from html import unescape

from load_data import get_restaurants

restaurants = get_restaurants()

def mm_dd_yyyy_key(date):
    mm, dd, yyyy = date.split('/')
    return yyyy, mm, dd

def sorted_dates(restaurant):
    return sorted(restaurant.keys(), key=mm_dd_yyyy_key, reverse=True)

def most_recent_violation(restaurant):
    dates = sorted_dates(restaurant)
    last_date = dates[0]
    return restaurant[last_date][0] # All violations in a single inspection have mostly same data

def recent_inspection_geq_min_score(r_name, min_score):
    restaurant = restaurants[r_name]
    violation = most_recent_violation(restaurant)
    score = int(violation['Inspection Score'])
    return score >= min_score

def recent_inspection_unsatisfactory(r_name):
    restaurant = restaurants[r_name]
    violation = most_recent_violation(restaurant)
    return violation['Inspection Result'] == 'Unsatisfactory'

def filtered_restaurants(name='', min_score=0, only_unsatisfactory=False):
    name = name.upper()
    filtered_restaurants = {}
    for r_name in restaurants:
        if name in r_name and recent_inspection_geq_min_score(r_name, min_score) \
                          and (not only_unsatisfactory or recent_inspection_unsatisfactory(r_name)):
            filtered_restaurants[r_name] = restaurants[r_name]
    return filtered_restaurants

#### functions below here are 'public'

def map_display(filtered_restaurants):
    results = []
    for r_name in filtered_restaurants:
        restaurant = filtered_restaurants[r_name]
        violation = most_recent_violation(restaurant)
        lon, lat = violation['Longitude'], violation['Latitude']
        if not lon or not lat:
            continue # Some restaurants are missing lat/long .. we'll just skip
        row = (r_name,
              violation['Inspection Result'],
              violation['Inspection Score'],
              lon,
              lat)
        results.append(row)
    return results

def fetch_detail(r_name):
    r_name = unescape(r_name)
    result = {}
    restaurant = restaurants[r_name]
    recent = most_recent_violation(restaurant)
    result['r_name'] = r_name
    result['lat'] = recent['Latitude']
    result['lon'] = recent['Longitude']
    result['info'] = '{}<br>{}, WA {}<br>{}'.format(recent['Address'],
                                                    recent['City'],
                                                    recent['Zip Code'],
                                                    recent['Phone'])
    result['inspections'] = []
    dates = sorted_dates(restaurant)
    for date in dates:
        inspection = restaurant[date]
        violations = []
        for violation in inspection:
            if violation['Violation Description']:
                violations.append((violation['Violation Description'], violation['Violation Points']))
        result['inspections'].append({
            'date': inspection[0]['Inspection Date'],
            'type': inspection[0]['Inspection Type'],
            'violations': violations,
            'score': inspection[0]['Inspection Score'],
            'result': inspection[0]['Inspection Result']
        })
    return result

def print_record_count():
    print('There are', len(restaurants), 'food establishments.')

if __name__ == '__main__':
    print_record_count()
