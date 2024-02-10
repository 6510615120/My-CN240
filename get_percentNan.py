import pandas as pd
import csv
import os

'''
get List of file_names
'''
# Get the current directory
current_directory = os.getcwd()
# List all files in the current directory
files = os.listdir(current_directory)
# Filter out directories, keep only files
keyword = 'test' #Please in put keyword
file_names_list = [file for file in files if os.path.isfile(os.path.join(current_directory, file)) and keyword in file]


'''
get Row from feature file
'''
# Specify the CSV file path
csv_file_path = 'row.csv'
# Initialize an empty list to store the data
variable_list = []
# Read the CSV file and append each row to the list
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        variable_list.append(row[0])


'''
make output data as DataFrame.to_csv
'''
#create emtpy dataframe with specific rows and columns 
output_data = pd.DataFrame(columns=file_names_list,index=variable_list)


'''
get %Nan from each file from each column
'''
#loop through all files
for file_name in file_names_list:


    data = pd.read_csv(file_name)                               
    data_row = data.shape[0]                                        #get amount of row in data
    list_of_columns = data.columns.to_list()                        #get all columns name into list
    
    #loop through all columns
    for columns in list_of_columns:

        percentNan = data[columns].isnull().sum()/data_row          #simple %Nan
        if columns in variable_list:                                #in case that column not in feature file
            output_data.at[columns, file_name] = percentNan         #put %Nan in right place

#output file
output_data.to_csv('output.csv', index=True)