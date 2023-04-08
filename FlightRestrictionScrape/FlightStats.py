import json
import FlightRestrictionParser
import MetarWeatherData
import datetime
import pytz
import time

LEDStatus = 0 #0 means all good
#0: all good, 1: restrictions not getable, 2: metar not getable, 3: both restrictions and metar not getable 

pathToLEDStatusJson = '/home/pi/Documents/PythonCode/PiStatusLEDStrip/ledStatusFile.json'

FlightScrapeDays = 365 #in days
SecondsBetweenScrape = 300

def GetAndStoreFlightData():
    file = open('FlightRestrictions.json') #get data from json file
    FlightData = json.load(file)
    file.close()

    restrictions = FlightRestrictionParser.GetFlightRestrictions() #web scrape the UND aviation flight restrictions
    metar = MetarWeatherData.GetMetarData()#web scrape the metar info from the aims website
    if metar == False or restrictions == False:#update led status
        if metar == False:
            LEDStatus = 1
            restrictions = ['','','','','']
        if restrictions == False:
            LEDStatus = 2
            metar = ''
        if metar == False and restrictions == False:
            LEDStatus = 3

    current_time = datetime.datetime.now(pytz.timezone('US/Central')) #get time for timestamp
    Year = current_time.year
    Month = current_time.month
    Day = current_time.day
    Hour = current_time.hour
    Minute = current_time.minute

    FlightData.append([[Year, Month, Day, Hour, Minute], restrictions, [metar]]) #add scraped data and time to the data to be added to the json file

    with open('FlightRestrictions.json','w') as outfile: #add data to json file
        json.dump(FlightData, outfile, indent=4)

def UpdateLEDStatusJson(LEDStatus):#Function to write data to the json file that displays lights
    color = (0,0,0)
    if LEDStatus == 0:#all good
        color = (0,1,0)
    elif LEDStatus == 1:#restriction issues
        color = (1,0,0)
    elif LEDStatus == 2:#Metar issues
        color = (0,0,1)
    elif LEDStatus == 3:#Both Metar and Restriction issues
        color = (1,0,1)
    with open(pathToLEDStatusJson,'r') as infile:#open
        LED = json.load(infile)

    LED[0][0] = color #Modify data

    with open(pathToLEDStatusJson,'w') as outfile: #write data
        json.dump(LED, outfile, indent=4)
    return color

startTime = time.time()
endTime = round(time.time()) + FlightScrapeDays*24*60*60

if FlightScrapeDays >=0:#Decide if infinite scraping or not
    while True:
        if time.time() < endTime:#while current unix time is less than time to stop scraping
            GetAndStoreFlightData()
            output = UpdateLEDStatusJson(LEDStatus)
            timeLeft = (((endTime - time.time())/60)/60)/24
            print('Data Stored: ', output, 'Days Left: ', timeLeft)
            time.sleep(SecondsBetweenScrape)#wait for next scrape
        else:
            break
else:
    while True:#never stops
        GetAndStoreFlightData()
        output = UpdateLEDStatusJson(LEDStatus)
        print('Data Stored: ', output, 'Days Left: Infinite')
        time.sleep(SecondsBetweenScrape)
print('DONE!!!')