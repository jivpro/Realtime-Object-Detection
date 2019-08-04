import os

imdir = 'id card'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

fidget_folders = [folder for folder in os.listdir('.') if 'images' in folder]

n = 0
for folder in fidget_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, 'aot-{:04}.jpg'.format(n)))
        n+=1