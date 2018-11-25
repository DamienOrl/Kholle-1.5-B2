#!/usr/bin/python3
import csv
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("-l", help="Show the values of the list", action="store_true")
parser.add_argument("-a", help="Add your inputs to the list")
parser.add_argument("-c", help="Erase the list", action="store_true")
#parser.add_argument("-s --max", help="Show the biggest value of the list")
#parser.add_argument("-s --min", help="Show the smallest value of the list")
#parser.add_argument("-s --sum", help="Calculate the sum of the values")
#parser.add_argument("-s --moy", help="Calculate the average of the values")
#parser.add_argument("-t", help="Sort out the values in the ascending order")
#parser.add_argument("-t --desc", help="Sort out the values in the descending order")
args = parser.parse_args()


if args.a:
    #for i in range(values.length):
    value = args.a
    with open("list.csv", mode="w", newline="") as val_list:
        list_writer = csv.writer(val_list)
        list_writer.writerow(value)

if args.l:
    with open("list.csv", mode="r") as val_list:
        list_reader = csv.reader(val_list)

        for line in val_list:
            print (line)

if args.c:
    if os.path.exists("list.csv"):
        os.remove("list.csv")
    else:
        print("Nothing to remove!")
