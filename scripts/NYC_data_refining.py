# Raymond Gerte, University of Connecticut, TURF Fellow Summer 2016
# An Analysis of NYC Trip Behavior Through Big Data Sources

# All datasets (Taxi, Uber, CitiBike, and Mass Tranist) are open source and
# readily accessible.

import pandas as pd
import numpy as np
import datetime as dt


# Import all datasets

greencab = pd.read_csv('green_tripdata_2014-09.csv', sep=',',
                       names=['vendorID', 'pickup_datetime',
                              'dropoff_datetime', 'store_and_fwd_flag',
                              'rate_code', 'pickup_longitude',
                              'pickup_latitude', 'dropoff_longitude',
                              'dropoff_latitude', 'passenger_count',
                              'trip_distance', 'fare_amount', 'extra',
                              'mta_tax', 'tip_amount', 'toll_amount',
                              'ehail_fee', 'total_amount', 'payment_type',
                              'trip_type'], header=None, index_col=False)
greencab = greencab.ix[1:]
yellowcab = pd.read_csv('yellow_tripdata_2014-09.csv',
                        names=['vendorID', 'pickup_datetime',
                               'dropoff_datetime', 'passenger_count',
                               'trip_distance', 'pickup_longitude',
                               'pickup_latitude', 'rate_code',
                               'store_and_fwd_flag', 'dropoff_longitude',
                               'dropoff_latitude', 'payment_type',
                               'fare_amount', 'surcharge', 'mta_tax',
                               'tip_amount', 'toll_amount', 'total_amount'],
                               parse_dates=[1, 2], header=0
                        )
citibike = pd.read_csv('2014-09-citibike-tripdata.csv',
                       names=['trip_duration', 'start_datetime',
                              'end_datetime', 'start_station_id',
                              'start_station_name',
                              'start_station_latitude',
                              'start_station_longitude', 'end_station_id',
                              'end_station_name', 'end_station_latitude',
                              'end_station_longitude', 'bike_id', 'usertype',
                              'birth_year', 'gender'], parse_dates=[1, 2],
                               header=0)
uber = pd.read_csv('uber-raw-data-sep2014.csv', sep=',',
                   names=['pickup_datetime', 'pickup_latitude',
                          'pickup_longitude', 'base_id'], parse_dates=[0],
                          header=0)

# Refine data into datetime csv's for quicker analysis
yellowcab_datetimes = yellowcab[['pickup_datetime', 'dropoff_datetime']]
greencab_datetimes = greencab[['pickup_datetime', 'dropoff_datetime']]
citibike_datetime = citibike[['start_datetime', 'end_datetime']]
uber_datetime = uber[['pickup_datetime']]

# Write DataFrames to CSV
yellowcab_datetimes.to_csv('yellowcab_datetime.csv')
greencab_datetimes.to_csv('greencab_datetime.csv')
citibike_datetime.to_csv('citibike_datetime.csv')
uber_datetime.to_csv('uber_datetime.csv')


# Refine Data into geospatial DataFrames
yellowcab_geodata = yellowcab[['pickup_longitude', 'pickup_latitude',
                               'dropoff_longitude', 'dropoff_latitude']]
greencab_geodata = greencab[['pickup_longitude', 'pickup_latitude',
                             'dropoff_longitude', 'dropoff_latitude']]
citibike_geodata = citibike[['start_station_longitude',
                             'start_station_latitude', 'end_station_longitude',
                             'end_station_latitude']]
uber_geodata = uber[['pickup_longitude', 'pickup_latitude']]

# Write DFs to csv's
yellowcab_geodata.to_csv('yellowcab_geodata.csv')
greencab_geodata.to_csv('greencab_geodata.csv')
citibike_geodata.to_csv('citibike_geodata.csv')
uber_geodata.to_csv('uber_geodata.csv')
