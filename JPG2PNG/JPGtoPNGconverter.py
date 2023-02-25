import sys
import os

from PIL import Image

# grab first and second argument

src_dir = sys.argv[1]
dest_dir = sys.argv[2]

# check /new exists, if not create
if(not os.path.exists(f'./{dest_dir}')):
    os.mkdir(f'./{dest_dir}')
# loop through Pokedox,
directory = os.fsencode(f'./{src_dir}')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if(filename.endswith('.jpg')):
        img = Image.open(f'./{src_dir}/{filename}')
        stem = filename.split('.')[0]
        img.save(f'./{dest_dir}/{stem}.png', 'png')

    else:
        continue

    # convert images to png
    # save to the new folder
