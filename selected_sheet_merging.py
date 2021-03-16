#Packages
import os
import pandas as pd
import dfgui


src_path = "provide dir path"
extensions = ('.XLS', '.xlsx', '.xls')
number_files = 0
full_table = pd.DataFrame()


df = []
# Loop through files
for path, dirs, files in os.walk(src_path):
    for file in files:
        if file.endswith(extensions):
            number_files = number_files + 1
            print (number_files)
            fullfilename = os.path.join (path, file)
            full_table = pd.read_excel(fullfilename, sheet_name=None)
            full_table["FILENAME"] = os.path.basename(file)
            df.append(full_table)

#full_table.reset_index (inplace=True, drop=True)
df = pd.concat(df.values())

writer = pd.ExcelWriter('USAID merging.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
