# King County Food Establishment Inspections

This project lets users explore [restaurant inspection data from King County](https://data.kingcounty.gov/Health/Food-Establishment-Inspection-Data/f29f-zza5) from January 1, 2015 to May 17, 2016. (I manually filtered it on the Socrata page. A future extension could be to dynamically fetch the last year of data when building the app.)

## Main listing page

This page shows a map with all the restaurants with inspections since January 1, 2015.

## Detail page

There will be a detail page for each restaurant, which will contain complete information about each inspection at that restaurant, including details about each violation if there are multiple from a single inspection.

## Filter options

Users will be able to filter the main listing page by

* doing a full text search of restaurant names
* choosing to show only the restaurants whose most recent inspection was unsatisfactory
* choosing to show only the restaurants over a certain inspection score

## Inspirations for this project

This project is inspired by the New York City restaurant inspection explorations presented by [the city itself](http://a816-restaurantinspection.nyc.gov/RestaurantInspection/SearchBrowse.do) and [the _New York Times_](http://www.nytimes.com/interactive/dining/new-york-health-department-restaurant-ratings-map.html). I'm just bringing the concept to my hometown. The usage of Leaflet for mapping is also inspired (/based on) the [IRE first news app tutorial](https://ireapps.github.io/first-news-app/build/index.html).
