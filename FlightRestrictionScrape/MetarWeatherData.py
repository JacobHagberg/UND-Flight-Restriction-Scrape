import requests

def GetMetarData():
    try: #scrapes weather data
        metar = requests.get('https://aviationweather.gov/adds/metars/?chk_metars=on&hoursStr=most+recent+only&std_trans=standard&station_ids=KGFK', timeout=8)
    except:
        return False  #if it cant get data
    
    location1 = metar.text.find('KGFK')
    if location1 != -1:
        location2 = metar.text.find('RMK',  location1)
    else:
        return False #issue with metar
    text = metar.text
    
    text = text[location1:location2]#clip out metar
    text = text.replace('\n', '')
    while True: #clean up metar
        if text.find('  ') == -1:
            break
        text = text.replace('  ', ' ')
    return text