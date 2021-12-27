import os

directory = 'docs/assets/'

files = os.listdir(directory)

for i in files:
    os.remove(directory +i)