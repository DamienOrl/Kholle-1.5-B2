#!/usr/bin/python3
import csv
import argparse
import os


parser = argparse.ArgumentParser()
gList = parser.add_argument_group('Manipulate the list')
gList.add_argument("-l", help="Show the values of the list", action="store_true")
gList.add_argument("-a", help="Add your inputs to the list", action="append")
gList.add_argument("-c", help="Erase the list", action="store_true")
gMath = parser.add_argument_group('Mathematical operations')
# gMath.add_argument("-s", "--max", help="Show the biggest value of the list", action="store_true")
# gMath.add_argument("-s", "--min", help="Show the smallest value of the list", action="store_true")
# gMath.add_argument("-s", "--sum", help="Calculate the sum of the values", action="store_true")
# gMath.add_argument("-s", "--moy", help="Calculate the average of the values", action="store_true")
args = parser.parse_args()


if args.a:
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

# if args.s:
#     if args.max:
#         with open("list.csv", mode="r") as val_list:
#             list_reader = csv.reader(val_list)
#             maximum = 0
#             holder = 0
#
#             for line in val_list:
#                 holder = line
#                 if int(holder) > maximum:
#                     maximum = holder
#         print (maximum)
#
#     if args.min:
#         with open("list.csv", mode="r") as val_list:
#             list_reader = csv.reader(val_list)
#             minimum = 0
#             holder = 0
#
#             for line in val_list:
#                 holder = line
#                 if int(holder) > minimum:
#                     minimum = holder
#         print (minimum)
#
#     if args.sum:
#         with open("list.csv", mode="r") as val_list:
#             list_reader = csv.reader(val_list)
#             sum = 0
#
#             for line in val_list:
#                 sum += int(line)
#         print (sum)
#
#
#     if args.moy:
#         with open("list.csv", mode="r") as val_list:
#             list_reader = csv.reader(val_list)
#             sum = 0
#             nbValues = 0
#
#             for line in val_list:
#                 sum += int(line)
#                 nbValues += 1
#         print (sum/nbValues)
