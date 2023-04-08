from bs4 import BeautifulSoup
import requests

def FlightRestrictionParser(soup):#parse with beautiful soup library
    searchClassList = ['Fixed Wing', 'Helicopter', 'UAS', 'Manager on Duty:', 'Supervisor of Flight:']
    ClassListResults = ['','','','','']
    counter = 0
    while True:
        counter += 1
        result = soup.find_all('td', class_ = 'auto-style' + str(counter))
        if len(result) != 0:
            for i in range(len(searchClassList)):#code to specifically get restriction data
                if (result[0].text).find(searchClassList[i]) != -1:
                    ClassListResults[i] = soup.find_all('td', class_ = 'auto-style' + str(counter) + 'b')[0].text      
        else:
            break

    return ClassListResults

def GetFlightRestrictions():
    try:
        response = requests.get('https://aims-asp.aero.und.edu/sof2/sof2.aspx', timeout=8) #get website
    except:
        return False #if it can not get website
    #print(response.text)

    soup = BeautifulSoup(response.text, "html.parser") #parse with bs4
    return FlightRestrictionParser(soup=soup)
