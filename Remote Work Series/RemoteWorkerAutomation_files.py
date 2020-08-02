import os
from datetime import date
import pandas as pd

data_location = 'Docs/Employee Receipts/'
file_list = []
for file in os.listdir(data_location):
    file_list.append(file)

data = {'file_names' : file_list }
file_df = pd.DataFrame(data)
new_file_directory = 'Docs/Processed Receipts/'
today = date.today()
#file_df.to_excel(new_file_directory + 'receipts_sum -' + str(today) + '.xlsx' )

for file in os.listdir(data_location):
    os.rename(data_location + file, new_file_directory + file )


string_to_find = 'Derrick'
directory_to_search = 'Docs/Processed Receipts/'
derrick_docs = []
for file in os.listdir(directory_to_search):
    with open(directory_to_search + file) as f:
        if string_to_find in f.read():
            derrick_docs.append(file)

print(derrick_docs)
