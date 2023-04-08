# UND-Flight-Restriction-Scrape
This python program uses the python request library to get the data from the UND Aims flight restriction website. It also gets the current metar data for the KGFK metar. It then stres that data to a JSON file. 
The python program called Spreadsheet.py can then take that data and put it into a spreadsheet. This can help you gain a better understanding of the data through the use of graphs. 

The file FlightRestrictionData.json is some sample data that the program that I have running on a Raspberry Pi 4 has generated. 

This program is ment to be used with another programming project of mine to display the status of the scraping program to an LED strip attached to the GPIO pins on the Pi. It is worth noting that this is not nessary for the code to work. 
