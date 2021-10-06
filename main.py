import os
import csv

with open("output.csv","w") as output:
    fieldnames=['first_name','last_name','birthts','image_path']
    # first save the data of the users
    csv_writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=",")
    csv_writer.writeheader()
    directory = os.fsencode("")
    for filename in os.listdir()