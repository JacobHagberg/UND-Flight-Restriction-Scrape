import json
import matplotlib.pyplot as plt

#uniqueRestrictions = ['Closed', 'No Dispatch', 'No Fly', 'Dual Local Only', 'Turbine Only', 'No Dispatch - Due to Ramp Conditions', 'Dual Only - Stage checks and Semi only', 'Dual Only', 'Dual Local Only - Stage Check Only', 'Solos Per METAR/TAF/NOTAM', '', 'No Spins/Aerobatics', 'Solos Traffic Pattern Only', 'No Student Pilot Solos', 'No Cessna / No Tailwheel', 'Garfield', 'Dual Pattern Only', 'No Restrictions', 'No Fly / No Dispatch due to ramp conditions', 'Dual Local Only - Family Weekend Flights', 'No Fly - Family Weekend Flights', 'No Student Pilot Solo XC', 'No Restrictions Family Weekend Flights', , 'IFR Dual Only', 'No Solo XC', 'Student Pilot Solo Traffic Pattern Only', 'IFR Dual Only  | VFR Dual Pattern Only', 'Dual Only - SEMI/Stage Check/ XC Only', 'Summer Camp Only', 'No Private Pilot Local Solo', 'No Student Pilot Solos | Private Local', 'No Student Pilot Solos / Private Local', 'No Student Pilot Solos or Private Local', 'No Night Solo XC', 'No XC', 'Dual Local Only | PIREPs Appreciated!', 'Dual Only | PIREPs Appreciated!', 'Pattern Only', 'No Student Pilot Solos | PIREPs Appreciated!', 'No Student Pilot Solos | Private Pilot Local Only', 'Dual Pattern Only | No Cessna | No Tailwheel', 'Solos Per METAR/TAF/NOTAM | No Cessna | No Tailwheel', 'Dual Local Only | No Cessna | No Tailwheel', 'Semi/Stage/Dual only', 'Semi/Stage/Dual/Spins Only', 'No Cessna /No Tailwheel Dual Only', 'Family Weekend No Fly', 'VFR Dual Pattern Only | IFR Dual Only', 'No Green Solos', 'SEMI, Stage, Dual XC Only', 'No Fly :(', 'Dual Pattern Only - No Cessna / No Tailwheel', 'Dual Only - No Cessna / No Tailwheel', 'SEMI/Stage/Dual Only', 'No Spins / Aerobatics', 'Family Weekend - Solos Per METAR/TAF/NOTAM', 'Family Weekend - Solos/Dual Allowed', 'No Solo Private Local', 'Semi, Stage, Solo, XC, and Perm Only', 'Student Pilot Solo Traffic Pattern Only / No Solo XC', 'Student Pilot Solo Traffic Pattern Only , No XC S', 'Dual Only - No Acro/Spins', 'Dual Only -- No Dispatch N', 'Semi/Stage/Solo/XC', 'Semi/Stage/XC Only', 'Semi/Stage/XC/PERM Only', 'No Dual VFR XC', 'No DECA Spins / Aerobatics', 'Dual Only - No DECA Acro/Spins', 'No Aerobatics', 'Solos Per METAR/TAF/NOTAM | No DECA', 'Dual Only | No DECA', 'Solos Traffic Pattern Only | No DECA', 'No Solo XC | No DECA', 'Solos Per METAR/TAF/NOTAM - No DECA Acro/Spins']


jsonPaths = ['RestrictionsData/FlightRestrictionData1.json', 'RestrictionsData/FlightRestrictionData2.json']

goodWeather = ['Dual Only', 'Solos Per METAR/TAF/NOTAM', 'No Spins/Aerobatics', 'No Restrictions', 'No Restrictions Family Weekend Flights', 'Summer Camp Only', 'Dual Only | PIREPs Appreciated!', 'No Night Solo XC', 'SEMI/Stage/Dual Only', 'Semi/Stage/Solo/XC', 'No DECA Spins / Aerobatics', 'Solos Per METAR/TAF/NOTAM - No DECA Acro/Spins', 'Dual Only | No DECA', 'No XC', 'Dual Only - No DECA Acro/Spins', 'No Solo XC | No DECA', 'Family Weekend - Solos/Dual Allowed', 'Semi/Stage/Dual only', 'No Spins / Aerobatics', 'Family Weekend - Solos Per METAR/TAF/NOTAM', 'No Aerobatics', 'Dual Only - No Acro/Spins', 'Semi/Stage/XC/PERM Only', 'Semi/Stage/XC Only', 'Dual Only - Stage checks and Semi only', 'Semi/Stage/Dual/Spins Only', 'Semi, Stage, Solo, XC, and Perm Only', 'Dual Only - SEMI/Stage Check/ XC Only', 'Solos Per METAR/TAF/NOTAM | No DECA', 'No Student Pilot Solos | Private Local', 'Garfield']
fairWeather = ['Dual Local Only', 'Solos Traffic Pattern Only', 'No Student Pilot Solos', 'No Cessna / No Tailwheel', 'Dual Local Only - Family Weekend Flights', 'No Student Pilot Solo XC', 'Student Pilot Solo Traffic Pattern Only', 'No Private Pilot Local Solo', 'Dual Local Only - Stage Check Only', 'No Student Pilot Solos / Private Local', 'Dual Local Only | PIREPs Appreciated!', 'No Student Pilot Solos | PIREPs Appreciated!', 'Solos Per METAR/TAF/NOTAM | No Cessna | No Tailwheel', 'Dual Local Only | No Cessna | No Tailwheel', 'No Solo XC', 'No Cessna /No Tailwheel Dual Only', 'Dual Only - No Cessna / No Tailwheel', 'No Green Solos', 'No Solo Private Local', 'Solos Traffic Pattern Only | No DECA', 'No Dual VFR XC', 'Student Pilot Solo Traffic Pattern Only , No XC S', 'Dual Only -- No Dispatch N',  'SEMI, Stage, Dual XC Only', 'Student Pilot Solo Traffic Pattern Only / No Solo XC', 'No Student Pilot Solos | Private Pilot Local Only', 'No Student Pilot Solos or Private Local']
ifr = ['Turbine Only', 'Dual Pattern Only', 'IFR Dual Only', 'IFR Dual Only  | VFR Dual Pattern Only', 'Pattern Only', 'Dual Pattern Only | No Cessna | No Tailwheel', 'VFR Dual Pattern Only | IFR Dual Only', 'Dual Pattern Only - No Cessna / No Tailwheel']
notFlyable = ['No Dispatch', 'No Fly', 'No Dispatch - Due to Ramp Conditions', 'No Fly / No Dispatch due to ramp conditions', 'No Fly - Family Weekend Flights', 'No Dispatch - Due to Convective Activity', 'Family Weekend No Fly', 'No Fly :(', 'No Dispatch - Due to Convective Activity']
#notFLyable does not contain 'Closed'

hourlyWeather = {}

for i in range(0, 24):
    hourlyWeather[i] = [0, 0, 0, 0] #good, fair, ifr, not flyable


for path in jsonPaths:
    with open(path, 'r') as f:
        data = json.load(f)
    for point in data:
        try:
            month = point[0][1]
            hour = point[0][3]
            restriction = point[1][0]
            if hour == 5 and restriction in goodWeather:
                print(restriction)
            if restriction in goodWeather:  hourlyWeather[hour][0] += 1
            elif restriction in fairWeather:  hourlyWeather[hour][1] += 1
            elif restriction in ifr:  hourlyWeather[hour][2] += 1
            elif restriction in notFlyable:  hourlyWeather[hour][3] += 1
        except:
            pass

finalWeather = {}
for key in hourlyWeather.keys():
    total = sum(hourlyWeather[key])
    finalWeather[key] = [round(hourlyWeather[key][0] / total, 3), round(hourlyWeather[key][1] / total, 3), round(hourlyWeather[key][2] / total, 3), round(hourlyWeather[key][3] / total, 3)]
    

print(finalWeather)
for i in range(2, 6):finalWeather.pop(i)


hours = list(finalWeather.keys())
x = list(range(len(hours)))
values = list(finalWeather.values())

v1 = [v[0] for v in values]
v2 = [v[1] for v in values]
v3 = [v[2] for v in values]
v4 = [v[3] for v in values]

plt.figure()

plt.bar(x, v1, color='green', label='Good Weather')
plt.bar(x, v2, bottom=v1, color='yellow', label='Fair Weather')

bottom_v3 = [v1[i] + v2[i] for i in range(len(x))]
plt.bar(x, v3, bottom=bottom_v3, color='purple', label='Barely Flyable/ IFR')

bottom_v4 = [bottom_v3[i] + v3[i] for i in range(len(x))]
plt.bar(x, v4, bottom=bottom_v4, color='red', label='Not Flyable')

plt.xlabel('Hour')
plt.ylabel('Value')
plt.title('Weather Categories By Hour')
plt.xticks(x, hours)  
plt.legend()

plt.tight_layout()
plt.savefig('Graphs/FlightWeatherByHour')
plt.show()
