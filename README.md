# 2016_turf_NYC_shared_ride_analysis
An analysis of shared modes in NYC using Python programming

This analysis was completed with funding provided through a Transportation Undergraduate Research Fellowship (TURF) offered through the Center for Transportation and Livable Systems (CTLS) at the University of Connecticut.

Within this repository, there are three main components:
1) A complete Jupyter Notebook containing a first pass analysis of various shared modes for September 2014.
2) A portion of the data used to complete the analysis,
And 3) The scripts used to refine the original datasets into those found in the data file.

# Quick Use Instructions

For users interested in just the analysis that has already been completed, the Jupyter Notebook file provides static visualizations and  commentary to garner quick insight into the presence of shared modes in NYC. This can be accessed directly through the repository by opening the file and does not require a download.

# Further Exploration

For users interested in further exploration, the simplest way to first access the project would be to clone this repository using git and the command line:

$ git clone https://github.com/foss-transportationmodeling/2016_turf_NYC_shared_ride_analysis

The scripts themselves can also be downloaded individually from the scripts file.

All existing scripts were written in Python 2.7.11 using pandas 0.18.1, bokeh 0.12.1, and datashader 0.4.0 along with their associated dependencies. It is recommended that interested users have these libraries installed and up to date.

The data presented in this repository has been refined from larger open source files which each of the modes, excluding Uber, publish publicly. Due to the nature of the size of these files, only a portion of the full data is presented and because of this, users will need the geographic data in order to experience the full functionality of the notebook. By downloading the entire data sets and making use of the aforementioned scripts, the geodata can be pulled and refined to a higher level of workability and interactivity 

# The Data

All the data used to complete this analysis is publically available and can be used in further explorations. Due to time constraints, only September 2014 was investigated, but a more comprehensive timespan can be explored using the completed work as a backbone. Links to the data are presented below:

Taxi - http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml

Citi Bike - https://www.citibikenyc.com/system-data

Uber (through FOIL Request by FiveThirtyEight) - https://github.com/fivethirtyeight/uber-tlc-foil-response/tree/master/uber-trip-data

