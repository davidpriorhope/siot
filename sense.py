import datetime, time
import requests
import read_temp


#setting up sampling frequency
samp_freq = 1.1 #this is actually time between samples, not frequency - 
                #the selected value has been selected after timing the loop and seeing that the average run time is 1s

#creating an avergae function which we will call later!
def average(input_list):
    avg = sum(input_list)/len(input_list)
    return avg

#In order to get an accurate sampling frequency we are going to make a function which takes the start time and calculates how long the actual sampling frequency should be
def actual_sleep(sampling_freq,start_time):
    duration = time.time() - start_time

    if sampling_freq - duration>0:
        return sampling_freq - duration
    else:
        return 0

#temperature calibration
def body_temp_cal():
    cal_start = input('Press enter to begin calibration')
    cal_time_start = time.time()
    cal_duration = 5
    cal_list = []
    while cal_time_start+cal_duration>time.time():
        #finding start at beginning of loop
        cal_loop_start = time.time()
        #read temperature
        temp_now = read_temp.read_temp()
        cal_list.append(temp_now)  #change this to the temperature reading

        time.sleep(actual_sleep(samp_freq, cal_loop_start))
    
    cal = average(cal_list)

    print('Calibrated body temperature of: ' +str(cal))

    return cal


cal_temp = body_temp_cal()


#commence timer
workout_duration = 0.1                             #make this 20 for the actual runs lol
actual_workout_duration = 3+ workout_duration*60    #converting to seconds and accounting for countdown
cycle = input("Ready to pedal? (y) ")
time_start = time.time()

#Preparing to save data locally
save_name_list = ['time','temp_raw','temp_per','weather']
def write_temp(my_list, save_name):
    textfile = open('temp_data/' +save_name+".txt", "w")
    for i in my_list:
        textfile.write(str(i) + "\n")
    textfile.close()


#reading data from sensors and API and then writing to Sheets
def read():

    #initially locally storing data rather than constantly uploading to make sampling frequency more accurate
    time_list = []
    temp_list_raw = []
    temp_list_perc = []
    weather_list = []
    
    #loop searching for new data
    while (time_start+actual_workout_duration)>time.time():
        #getting local start time of loop to adjust sampling frequency
        loop_start_time = time.time()
        
        
        #getting time
        time_now = datetime.datetime.now().strftime('%H:%M:%S') #getting the time
        time_list.append(time_now)
        
        #getting temperature
        temp_now = read_temp.read_temp()
        temp_list_raw.append(temp_now)
        temp_perc = temp_now/cal_temp
        temp_list_perc.append(temp_perc)

        #getting london temperature
        weather_now = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=ada8d9cc126cf4404e8e2bae94450f3e&units=metric").json()['main']['temp']
        weather_list.append(weather_now)

        time.sleep(actual_sleep(samp_freq,loop_start_time))



    #telling user to stop pedalling
    print('Workout complete! You have cycled for '+ str(workout_duration) + ' minutes! Good job!' + ' Your body reached a maximum temperature of: ' + str(max(temp_list_raw)))
    
    print('Temporarily storing data locally')
    master_list = [time_list, temp_list_raw, temp_list_perc, weather_list]
    #writing temporary files
    for i in range(len(master_list)):
        write_temp(master_list[i],save_name_list[i])

 

#exciting countdown!
if cycle =='y':
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("PEDAL!!!!")
    read()