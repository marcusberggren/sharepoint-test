from sharepoint import Sharepoint

# set file name
file_name = 'SB0Y1LHC.pdf'

# set the folder name
folder_name = 'EGL'

# get file
file = Sharepoint().download_file(file_name, folder_name)

# save file
with open(file_name, 'wb') as f:
    f.write(file)