# Raymond Gerte
# Mode Share analysis NYC September 2014
import pandas as pd
import numpy as np
import datetime as dt
from bokeh.charts import Line, output_file, show, Bar
from bokeh.models import (FactorRange, CategoricalAxis, VBox, Range1d,
                          LinearAxis, DatetimeTickFormatter)
from bokeh.plotting import figure
from bokeh.layouts import gridplot

# Import datetime data
yellowcab = pd.read_csv('yellowcab_datetime.csv', index_col=0,
                        parse_dates=[1, 2])
greencab = pd.read_csv('greencab_datetime.csv', index_col=0,
                       parse_dates=[1, 2])
citibike = pd.read_csv('citibike_datetime.csv', index_col=0,
                       parse_dates=[1, 2])
uber = pd.read_csv('uber_datetime.csv', index_col=0,
                   parse_dates=[1])
weather = pd.read_csv('Sep2014Weather.csv', parse_dates=[0], index_col='Date',
                      usecols=['Date', 'mean_temp', 'percipitation'])

# count the trips made by each mode by day
yellowcab_daily_trips = yellowcab['pickup_datetime'].dt.day.value_counts().sort_index()
greencab_daily_trips = greencab['pickup_datetime'].dt.day.value_counts().sort_index()
citibike_daily_trips = citibike['start_datetime'].dt.day.value_counts().sort_index()
uber_daily_trips = uber['pickup_datetime'].dt.day.value_counts().sort_index()

rng = pd.date_range('9/1/2014', periods=30, freq='D')

trips = pd.DataFrame(zip(yellowcab_daily_trips, greencab_daily_trips,
                         citibike_daily_trips, uber_daily_trips),
                     columns=['yellow_trips', 'green_trips',
                              'citibike_trips', 'uber_trips'],
                     index=rng)
trips.loc[:, 'weekday'] = trips.index.weekday
trips['weekday'].replace(to_replace=[0, 1, 2, 3, 4, 5, 6],
                         value=['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                                'Friday', 'Saturday', 'Sunday'], inplace=True)


graph = Line(trips, title='NYC September 2014 Trip Distribution',
             legend='top_left', ylabel='Trips',
             color=['blue', 'green', 'black', 'yellow'], plot_width=800,
             plot_height=500)

graph.xaxis.formatter = DatetimeTickFormatter(
    formats=dict(
        days=["%a %m/%d"]
    )
)

#trips.to_csv('Sep2014_DayTripCount.csv')
output_file('trips.html')
show(graph)

# Here I am creating a second line graph of typical morning 'commuter' trips
# by investigating the trips, by mode, made between 7-10am across every day of
# the month.

yellow_am_commute = yellowcab.set_index('pickup_datetime').between_time('7:00', '10:00')
green_am_commute = greencab.set_index('pickup_datetime').between_time('7:00', '10:00')
citibike_am_commute = citibike.set_index('start_datetime').between_time('7:00', '10:00')
uber_am_commute = uber.set_index('pickup_datetime').between_time('7:00', '10:00')

yellow_am_commuters = pd.value_counts(yellow_am_commute.index.normalize(), sort=False)
green_am_commuters = pd.value_counts(green_am_commute.index.normalize(), sort=False)
citibike_am_commuters = pd.value_counts(citibike_am_commute.index.normalize(), sort=False)
uber_am_commuters = pd.value_counts(uber_am_commute.index.normalize(), sort=False)

# concatinate df's into one AM Trip set
am_commuters = pd.concat([yellow_am_commuters, green_am_commuters,
                          citibike_am_commuters, uber_am_commuters], axis=1,
                         keys=['yellow cab', 'green cab',
                               'citibike', 'uber'])
am_commuters.loc[:, 'weekday'] = trips.index.weekday
am_commuters['weekday'].replace(to_replace=[0, 1, 2, 3, 4, 5, 6],
                         value=['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                                'Friday', 'Saturday', 'Sunday'], inplace=True)

am_commuters.to_csv('Sep2014_AMCommuteTripCount.csv')
graph2 = Line(am_commuters,
              title='NYC September 2014 Morning Commute (7-10am): Trips by Mode',
              legend='top_left', ylabel='Trips', xlabel='Date', plot_width=800,
              plot_height=400, color=['blue', 'green', 'black', 'yellow'])
graph2.xaxis.formatter = DatetimeTickFormatter(
    formats=dict(
        days=["%a %m/%d"]
    )
)
# Create second graph with relevant weather data & linked axies
graph3 = figure(title='September 2014 Weather', plot_width=800,
                plot_height=400, tools='pan, wheel_zoom',
                x_axis_type='datetime', y_range=Range1d(0, 90))

graph3.line(weather.index, weather['mean_temp'], line_color='orange',
            line_width=2, legend='temperature')
graph3.yaxis.axis_label = 'Temperature (F)'
graph3.extra_y_ranges = {'Percipitation': Range1d(0, .75)}
graph3.add_layout(LinearAxis(y_range_name='Percipitation',
                             axis_label='Percipitation (in)'), 'right')
graph3.line(weather.index, weather['percipitation'],
            y_range_name='Percipitation', line_color='blue', line_width=2,
            legend='percipitation')
graph3.x_range = graph2.x_range
graph3.toolbar_location = 'above'
graph3.xaxis.axis_label = 'Date'
graph3.legend.location = 'top_left'
graph3.xaxis.formatter = DatetimeTickFormatter(
    formats=dict(
        days=["%a %m/%d"]
    )
)

# Here I am creating a fourth line graph of typical evening 'commuter' trips
# by investigating the trips, by mode, made between 4-7pm across every day of
# the month.

yellow_pm_commute = yellowcab.set_index('pickup_datetime').between_time('16:00', '19:00')
green_pm_commute = greencab.set_index('pickup_datetime').between_time('16:00', '19:00')
citibike_pm_commute = citibike.set_index('start_datetime').between_time('16:00', '19:00')
uber_pm_commute = uber.set_index('pickup_datetime').between_time('16:00', '19:00')

yellow_pm_commuters = pd.value_counts(yellow_pm_commute.index.normalize(), sort=False)
green_pm_commuters = pd.value_counts(green_pm_commute.index.normalize(), sort=False)
citibike_pm_commuters = pd.value_counts(citibike_pm_commute.index.normalize(), sort=False)
uber_pm_commuters = pd.value_counts(uber_pm_commute.index.normalize(), sort=False)

# concatinate df's into one PM Trip set
pm_commuters = pd.concat([yellow_pm_commuters, green_pm_commuters,
                          citibike_pm_commuters, uber_pm_commuters], axis=1,
                         keys=['yellow cab', 'green cab',
                               'citibike', 'uber'])
pm_commuters.loc[:, 'weekday'] = trips.index.weekday
pm_commuters['weekday'].replace(to_replace=[0, 1, 2, 3, 4, 5, 6],
                         value=['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                                'Friday', 'Saturday', 'Sunday'], inplace=True)

pm_commuters.to_csv('Sep2014_PMCommuteTripCount.csv')

graph4 = Line(pm_commuters,
              title='NYC September 2014 Evening Commute (4-7pm): Trips by Mode',
              legend='top_left', ylabel='Trips', xlabel='Date', plot_width=800,
              plot_height=400, color=['blue', 'green', 'black', 'yellow'])
graph4.x_range = graph2.x_range
graph4.xaxis.formatter = DatetimeTickFormatter(
    formats=dict(
        days=["%a %m/%d"]
    )
)

# Here I am creating a fifth line graph of late night trips
# by investigating the trips, by mode, made between 10pm-12am across every day
# of the month.

yellow_late = yellowcab.set_index('pickup_datetime').between_time('22:00', '23:59')
green_late = greencab.set_index('pickup_datetime').between_time('22:00', '23:59')
citibike_late = citibike.set_index('start_datetime').between_time('22:00', '23:59')
uber_late = uber.set_index('pickup_datetime').between_time('22:00', '23:59')

yellow_late_count = pd.value_counts(yellow_late.index.normalize(), sort=False)
green_late_count = pd.value_counts(green_late.index.normalize(), sort=False)
citibike_late_count = pd.value_counts(citibike_late.index.normalize(), sort=False)
uber_late_count = pd.value_counts(uber_late.index.normalize(), sort=False)

# concatinate df's into one Late Trip set
late_trips = pd.concat([yellow_late_count, green_late_count,
                          citibike_late_count, uber_late_count], axis=1,
                         keys=['yellow cab', 'green cab',
                               'citibike', 'uber'])
late_trips.loc[:, 'weekday'] = trips.index.weekday
late_trips['weekday'].replace(to_replace=[0, 1, 2, 3, 4, 5, 6],
                         value=['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                                'Friday', 'Saturday', 'Sunday'], inplace=True)
late_trips.to_csv('Sep2014_LateTripCount.csv')
graph5 = Line(late_trips,
              title='NYC September 2014 Late Night Trips (10pm-12am): Trips by Mode',
              legend='top_left', ylabel='Trips', xlabel='Date', plot_width=800,
              plot_height=400, color=['blue', 'green', 'black', 'yellow'])
graph5.x_range = graph2.x_range
graph5.xaxis.formatter = DatetimeTickFormatter(
    formats=dict(
        days=["%a %m/%d"]
    )
)

output_file('commute_trips.html')
show(gridplot([[graph2, graph4], [graph5, graph3]]))
