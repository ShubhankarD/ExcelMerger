import pandas as pd

filepath = r"filepath\filename"
sheets_dict = pd.read_excel(filepath, sheet_name=None)

full_table = pd.DataFrame()

#loop through sheets
for name, sheet in sheets_dict.items():
    sheet['sheet'] = name

    #sheet = sheet.rename(columns=lambda x: x.split('\n')[-1])
    full_table = full_table.append(sheet)

full_table.reset_index (inplace=True, drop=True)

#dg.show(full_table)

#Write to Excel
writer = pd.ExcelWriter('consolidated_sdbcapm.xlsx', engine='xlsxwriter')
full_table.to_excel(writer,'Sheet1')
