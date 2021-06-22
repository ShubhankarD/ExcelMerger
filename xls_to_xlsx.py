import os
from xls2xlsx import XLS2XLSX

input_path = r""
Destination_Path = r""

#empty list for filepaths
paths = [] 

#empty list for filenames
fns = []

for root, dirs, files in os.walk(input_path):
    for name in files:
        paths.append(os.path.join(root, name))
        fns.append(name)
        
for file in paths:
    basename = os.path.basename(file)
    new_file_name = os.path.splitext(basename)[0]+".xlsx"
    x2x = XLS2XLSX(file)
    wb = x2x.to_xlsx(Destination_Path+"\\"+new_file_name)
