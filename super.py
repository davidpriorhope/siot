#Hello this is the main file which should be run for each cycle

import push_to_github
import sense
import upload
import chart_build

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


#push updates to github
push_to_github