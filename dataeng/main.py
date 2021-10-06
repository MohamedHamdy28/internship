import os
import csv

with open("output.csv","w") as output:
    fieldnames = ['first_name', ' last_name', ' birthts', 'image_path']
    # first save the data of the users
    output_writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=",")
    output_writer.writeheader()
    directory = r'D:\University\intenships\Data engineer internship tasks\internship\dataeng\02-src-data'
    for file in os.listdir(directory):
        filename = os.fsencode(file)
        if file.endswith(".csv"):
            filedir=directory+directory[2]+file;
            with open(filedir,"r") as data:
                data_reader=csv.DictReader(data)
                for line in data_reader:
                    output_writer.writerow(line)



