# UND-Flight-Restriction-Scrape
This Python program uses the Python request library to get the data from the UND Aims flight restriction website. It also gets the current metar data for the KGFK metar. It then stores that data to a JSON file. 

The Python program called Spreadsheet.py can then take that data and put it into a spreadsheet. This can help you gain a better understanding of the data through the use of graphs. 

The file FlightRestrictionData.json is some sample data that the program that I have running on a Raspberry Pi 4 has generated. 

This program is meant to be used with another programming project of mine to display the status of the scraping program to an LED strip attached to the GPIO pins on the Pi. It is worth noting that this is not necessary for the code to work. 


Libraries used:
1. BeautifulSoup: For parsing HTML
2. requests: For getting website data
3. json: For interaction with JSON files
4. datetime: For Getting the current time
5. pytz: For getting the current time of timezone that KGFK is in
6. time: For adding delay
7. openpyxl: For adding data to an Excel spreadsheet


This code is open source and can be used by anyone.
