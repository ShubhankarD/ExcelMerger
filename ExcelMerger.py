#Packages
import os
import pandas as pd
import xlsxwriter

src_path = r"C:\Users\sdash029\Desktop\Project DAWN\3212018\JAPAN"

number_files = 0

df = []
# Loop through files
for path, dirs, files in os.walk(src_path):
    for file in files:
        number_files = number_files + 1
        print (number_files)
        data = pd.read_excel(os.path.join(path, file)).iloc[:-1]
        data["filename"] = os.path.basename(file)
        df.append(data)

df = pd.concat(df)

writer = pd.ExcelWriter('pandas_mow_japan.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
