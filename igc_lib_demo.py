#!/usr/bin/env python
from __future__ import print_function

import os
import sys

### homebrew start ###

import pandas as pd
import openpyxl

### homebrew end ###

import igc_lib
import lib.dumpers as dumpers


def print_flight_details(flight):
    print("Flight:", flight)
    print("Takeoff:", flight.takeoff_fix)
    thermals = flight.thermals
    glides = flight.glides


### homebrew start ###

    # We need an empty list to get a proper output later on
    flightstats = []

    for i in range(max(len(thermals), len(glides))):
        if i < len(glides):
            # instead of printing, we want to append the elements
            flightstats.append(glides[i])
            # print("  glide[%d]:" % i, glides[i])
        if i < len(thermals):
            # instead of printing, we want to append the elements
            flightstats.append(thermals[i])
            # print("  thermal[%d]:" % i, thermals[i])
    print("Landing:", flight.landing_fix)

    # print(flightstats)
    # return the list
    return flightstats

# maybe we must integrate something like
# glidespeed = Glide()
# print(glidespeed.speed())
# inside the iteration

### homebrew end ###


# leave dumping out at the moment
'''
def dump_flight(flight, input_file):
    input_base_file = os.path.splitext(input_file)[0]
    wpt_file = "testfiles/%s-thermals.wpt" % input_base_file
    cup_file = "testfiles/%s-thermals.cup" % input_base_file
    thermals_csv_file = "testfiles/%s-thermals.csv" % input_base_file
    flight_csv_file = "testfiles/%s-flight.csv" % input_base_file
    python igc_lib_demo.py DS1.igckml_file = "testfiles/%s-flight.kml" % input_base_file

    print("Dumping thermals to %s, %s and %s" %
          (wpt_file, cup_file, thermals_csv_file))
    dumpers.dump_thermals_to_wpt_file(flight, wpt_file, True)
    dumpers.dump_thermals_to_cup_file(flight, cup_file)

    print("Dumping flight to %s and %s" % (kml_file, flight_csv_file))
    dumpers.dump_flight_to_csv(flight, flight_csv_file, thermals_csv_file)
    dumpers.dump_flight_to_kml(flight, kml_file)

'''

def main():
    if len(sys.argv) < 2:
        print("Usage: %s file.igc [file.lkt]" % sys.argv[0])
        sys.exit(1)

    input_file = sys.argv[1]
    task_file = None
    if len(sys.argv) > 2:
        task_file = sys.argv[2]

    flight = igc_lib.Flight.create_from_file(input_file)
    if not flight.valid:
        print("Provided flight is invalid:")
        print(flight.notes)
        sys.exit(1)

    print_flight_details(flight)

### homebrew start ###

    # put the returned list into a simple dataframe
    flightstats_df = pd.DataFrame(print_flight_details(flight), columns = ['dummy'])

    print(flightstats_df)

    with pd.ExcelWriter('analyzed.xls', engine = 'openpyxl') as writer:
        flightstats_df.to_excel(writer, sheet_name = 'analyzed')

    # return(flight)

# dynamically?
#with pd.ExcelWriter('%s.xls' % igc_lib_demo.print_flight_details([0]), engine = 'openpyxl') as writer:
#   flightstats_df.to_excel(writer, sheet_name = '%s' % igc_lib_demo.print_flight_details([0]))


### homebrew end ###

# leave dumping out at the moment
'''
    dump_flight(flight, input_file)

    if task_file:
        task = igc_lib.Task.create_from_lkt_file(task_file)
        reached_turnpoints = task.check_flight(flight)
        for t, fix in enumerate(reached_turnpoints):
            print("Turnpoint[%d] achieved at:" % t, fix.rawtime)
'''

if __name__ == "__main__":
    main()
