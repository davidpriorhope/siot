#Hello this is the main file which should be run for each cycle

import push_to_github
import sense
import upload
import chart_build
import daily_chart_build
import clean_assets
import os
import time

#Collect data
sense

#Upload data
upload

#Create website assets:
    #Read data 
    #Do processing (multi-dimensional linear regression)
        #this includes calculating the number of layers to cycle right now
    #build chart
#clean_assets
chart_build
daily_chart_build
print('Successfully generated charts')


#push updates to github

directory = 'docs/assets/'

files = os.listdir(directory)

while len(files)<3:                 #this while loop is to stall out until all 3 graphs have been uploaded to the folder
    files =os.listdir(directory)
    time.sleep(1)
    print('1 loop')

push_to_github