import pandas

csv_files = r"path"

number_files = 0

for csv_file in csv_files:
    Sheet_name = csv_file[:-4]
    pandas.read_csv(csv_file,low_memory=False).to_excel(csv_file+'.xlsx', sheet_name=Sheet_name,index=False)
