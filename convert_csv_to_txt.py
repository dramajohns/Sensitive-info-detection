# -*- coding: utf-8 -*-

# simple function for converting csv into txt
def convert_csv_to_txt(filepath,path): 
    import csv
    with open(path, "w") as my_output_file:
        with open(filepath, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
    return(my_output_file)