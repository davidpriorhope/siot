#Hello this is the main file which should be run for each cycle

'''import push_to_github
import sense
import upload
import chart_build
import daily_chart_build
import clean_assets'''
import os
import time


#sense
exec(open("./sense.py").read())

#upload data
exec(open("./upload.py").read())
#exec(open("./clean_assets.py").read())

#Create website assets:
    #Read data 
    #Do processing (multi-dimensional linear regression)
        #this includes calculating the number of layers to cycle right now
    #build chart

exec(open("./chart_build.py").read())
exec(open("./daily_chart_build.py").read())
print('Successfully generated charts')

directory = 'docs/assets/'
files = os.listdir(directory)

#this while loop is to stall out until all 3 graphs have been uploaded to the folder
while len(files)<3:
    files =os.listdir(directory)

#pushing updated files to github
exec(open("./push_to_github.py").read())