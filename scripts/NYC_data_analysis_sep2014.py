# Raymond Gerte, University of Connecticut, TURF Fellow Summer 2016
# An Analysis of NYC Trip Behavior Through Big Data Sources

# All datasets (Taxi, Uber, CitiBike, and Mass Tranist) are open source and
# readily accessible.

import pandas as pd
import numpy as np
import datetime as dt
from bokeh.plotting import figure, output_file, show
import datashader as ds
from datashader.bokeh_ext import InteractiveImage
from functools import partial
from datashader.utils import export_image
from datashader.colors import colormap_select, Greys9, Hot, viridis, inferno
from IPython.core.display import HTML, display

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
                                header=0
                        )
citibike = pd.read_csv('2014-09-citibike-tripdata.csv',
                       names=['trip_duration', 'start_datetime', 'end_datetime',
                              'start_station_id', 'start_station_name',
                              'start_station_latitude',
                              'start_station_longitude', 'end_station_id',
                              'end_station_name', 'end_station_latitude',
                              'end_station_longitude', 'bike_id', 'usertype',
                              'birth_year', 'gender'], header=0)
uber = pd.read_csv('uber-raw-data-sep2014.csv', sep=',',
                   names=['pickup_datetime', 'pickup_latitude',
                          'pickup_longitude', 'base_id'], header=0)

# Refine data into datetime csvs for quicker analysis
yellowcab_datetimes = yellowcab['pickup_datetime', 'dropoff_datetime']
greencab_datetimes = greencab['pickup_datetime', 'dropoff_datetime']
citibike_datetime = citibike['start_datetime', 'end_datetime']
uber_datetime = uber['pickup_datetime']

# Write DataFrames to CSV
yellowcab_datetimes.to_csv('yellowcab_datetimes.csv')
greencab_datetimes.to_csv('greencab_datetimes.csv')
citibike_datetime.to_csv('citibike_datetime.csv')
uber_datetime.to_csv('uber_datetime.csv')
