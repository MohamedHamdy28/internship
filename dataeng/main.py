import os
import csv

with open("output.csv","w") as output:
    fieldnames = ['first_name', ' last_name', ' birthts', 'image_path']
    # first save the data of the users
    output_writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=",")
    output_writer.writeheader()
    directory ="02-src-data"
    file_data_dir = directory
    file_image_dir = directory
    ready=0
    for file in os.listdir(directory):
        filename = os.fsencode(file)
        if file.endswith(".csv"):
            file_Data_dir=directory+'/'+file
            ready += 1
        if file.endswith(".png"):
            file_image_dir = directory+'/'+file
            ready += 1
        if ready == 2:
            ready=0
            with open(file_Data_dir,"r") as data:
                data_reader=csv.DictReader(data)
                for line in data_reader:
                    output_writer.writerow({"first_name":line.get("first_name")," last_name":line.get(" last_name")," birthts":line.get(" birthts"),"image_path":file_image_dir})




