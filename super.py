#Hello this is the main file which should be run for each cycle

import push_to_github
import sense
import upload
import chart_build
import daily_chart_build
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
chart_build
daily_chart_build

#time.sleep(5) #temporary sleep command waiting for image to be saved before doing stuff


#push updates to github
push_to_github