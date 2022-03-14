import os
import collections

# Find download folder
Download_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# File type to folder
mappings_file = collections.defaultdict()
for filename in os.listdir(Download_path):
    file_type = filename.split('.')[-1]
    mappings_file.setdefault(file_type,[]).append(filename)

# pprint(mappings_file)
# Move all files into their folder/directory
for name_dir, Item_dir in mappings_file.items():
    folder_path = os.path.join(Download_path, name_dir)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for item in Item_dir:
        source = os.path.join(Download_path, item)
        destination_dir = os.path.join(folder_path,item)
        print(f'Memindahkan {source} ke {destination_dir}')
        os.rename(source,destination_dir)
