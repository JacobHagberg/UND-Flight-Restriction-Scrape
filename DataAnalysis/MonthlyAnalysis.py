import json
import matplotlib.pyplot as plt

#uniqueRestrictions = ['Closed', 'No Dispatch', 'No Fly', 'Dual Local Only', 'Turbine Only', 'No Dispatch - Due to Ramp Conditions', 'Dual Only - Stage checks and Semi only', 'Dual Only', 'Dual Local Only - Stage Check Only', 'Solos Per METAR/TAF/NOTAM', '', 'No Spins/Aerobatics', 'Solos Traffic Pattern Only', 'No Student Pilot Solos', 'No Cessna / No Tailwheel', 'Garfield', 'Dual Pattern Only', 'No Restrictions', 'No Fly / No Dispatch due to ramp conditions', 'Dual Local Only - Family Weekend Flights', 'No Fly - Family Weekend Flights', 'No Student Pilot Solo XC', 'No Restrictions Family Weekend Flights', , 'IFR Dual Only', 'No Solo XC', 'Student Pilot Solo Traffic Pattern Only', 'IFR Dual Only  | VFR Dual Pattern Only', 'Dual Only - SEMI/Stage Check/ XC Only', 'Summer Camp Only', 'No Private Pilot Local Solo', 'No Student Pilot Solos | Private Local', 'No Student Pilot Solos / Private Local', 'No Student Pilot Solos or Private Local', 'No Night Solo XC', 'No XC', 'Dual Local Only | PIREPs Appreciated!', 'Dual Only | PIREPs Appreciated!', 'Pattern Only', 'No Student Pilot Solos | PIREPs Appreciated!', 'No Student Pilot Solos | Private Pilot Local Only', 'Dual Pattern Only | No Cessna | No Tailwheel', 'Solos Per METAR/TAF/NOTAM | No Cessna | No Tailwheel', 'Dual Local Only | No Cessna | No Tailwheel', 'Semi/Stage/Dual only', 'Semi/Stage/Dual/Spins Only', 'No Cessna /No Tailwheel Dual Only', 'Family Weekend No Fly', 'VFR Dual Pattern Only | IFR Dual Only', 'No Green Solos', 'SEMI, Stage, Dual XC Only', 'No Fly :(', 'Dual Pattern Only - No Cessna / No Tailwheel', 'Dual Only - No Cessna / No Tailwheel', 'SEMI/Stage/Dual Only', 'No Spins / Aerobatics', 'Family Weekend - Solos Per METAR/TAF/NOTAM', 'Family Weekend - Solos/Dual Allowed', 'No Solo Private Local', 'Semi, Stage, Solo, XC, and Perm Only', 'Student Pilot Solo Traffic Pattern Only / No Solo XC', 'Student Pilot Solo Traffic Pattern Only , No XC S', 'Dual Only - No Acro/Spins', 'Dual Only -- No Dispatch N', 'Semi/Stage/Solo/XC', 'Semi/Stage/XC Only', 'Semi/Stage/XC/PERM Only', 'No Dual VFR XC', 'No DECA Spins / Aerobatics', 'Dual Only - No DECA Acro/Spins', 'No Aerobatics', 'Solos Per METAR/TAF/NOTAM | No DECA', 'Dual Only | No DECA', 'Solos Traffic Pattern Only | No DECA', 'No Solo XC | No DECA', 'Solos Per METAR/TAF/NOTAM - No DECA Acro/Spins']

jsonPaths = ['RestrictionsData/FlightRestrictionData1.json', 'RestrictionsData/FlightRestrictionData2.json']

goodWeather = ['Dual Only', 'Solos Per METAR/TAF/NOTAM', 'No Spins/Aerobatics', 'No Restrictions', 'No Restrictions Family Weekend Flights', 'Summer Camp Only', 'Dual Only | PIREPs Appreciated!', 'No Night Solo XC', 'SEMI/Stage/Dual Only', 'Semi/Stage/Solo/XC', 'No DECA Spins / Aerobatics', 'Solos Per METAR/TAF/NOTAM - No DECA Acro/Spins', 'Dual Only | No DECA', 'No XC', 'Dual Only - No DECA Acro/Spins', 'No Solo XC | No DECA', 'Family Weekend - Solos/Dual Allowed', 'Semi/Stage/Dual only', 'No Spins / Aerobatics', 'Family Weekend - Solos Per METAR/TAF/NOTAM', 'No Aerobatics', 'Dual Only - No Acro/Spins', 'Semi/Stage/XC/PERM Only', 'Semi/Stage/XC Only', 'Dual Only - Stage checks and Semi only', 'Semi/Stage/Dual/Spins Only', 'Semi, Stage, Solo, XC, and Perm Only', 'Dual Only - SEMI/Stage Check/ XC Only', 'Solos Per METAR/TAF/NOTAM | No DECA', 'No Student Pilot Solos | Private Local', 'Garfield']
fairWeather = ['Dual Local Only', 'Solos Traffic Pattern Only', 'No Student Pilot Solos', 'No Cessna / No Tailwheel', 'Dual Local Only - Family Weekend Flights', 'No Student Pilot Solo XC', 'Student Pilot Solo Traffic Pattern Only', 'No Private Pilot Local Solo', 'Dual Local Only - Stage Check Only', 'No Student Pilot Solos / Private Local', 'Dual Local Only | PIREPs Appreciated!', 'No Student Pilot Solos | PIREPs Appreciated!', 'Solos Per METAR/TAF/NOTAM | No Cessna | No Tailwheel', 'Dual Local Only | No Cessna | No Tailwheel', 'No Solo XC', 'No Cessna /No Tailwheel Dual Only', 'Dual Only - No Cessna / No Tailwheel', 'No Green Solos', 'No Solo Private Local', 'Solos Traffic Pattern Only | No DECA', 'No Dual VFR XC', 'Student Pilot Solo Traffic Pattern Only , No XC S', 'Dual Only -- No Dispatch N',  'SEMI, Stage, Dual XC Only', 'Student Pilot Solo Traffic Pattern Only / No Solo XC', 'No Student Pilot Solos | Private Pilot Local Only', 'No Student Pilot Solos or Private Local']
ifr = ['Turbine Only', 'Dual Pattern Only', 'IFR Dual Only', 'IFR Dual Only  | VFR Dual Pattern Only', 'Pattern Only', 'Dual Pattern Only | No Cessna | No Tailwheel', 'VFR Dual Pattern Only | IFR Dual Only', 'Dual Pattern Only - No Cessna / No Tailwheel']
notFlyable = ['No Dispatch', 'No Fly', 'No Dispatch - Due to Ramp Conditions', 'No Fly / No Dispatch due to ramp conditions', 'No Fly - Family Weekend Flights', 'No Dispatch - Due to Convective Activity', 'Family Weekend No Fly', 'No Fly :(', 'No Dispatch - Due to Convective Activity']
#notFLyable does not contain 'Closed'

monthlyWeather = {}

for i in range(1, 13):
    monthlyWeather[i] = [0, 0, 0, 0] #good, fair, ifr, not flyable


for path in jsonPaths:
    with open(path, 'r') as f:
        data = json.load(f)
    for point in data:
        try:
            month = point[0][1]
            restriction = point[1][0]
            if restriction in goodWeather:  monthlyWeather[month][0] += 1
            elif restriction in fairWeather:  monthlyWeather[month][1] += 1
            elif restriction in ifr:  monthlyWeather[month][2] += 1
            elif restriction in notFlyable:  monthlyWeather[month][3] += 1
        except:
            pass

finalWeather = {}
for key in monthlyWeather.keys():
    total = sum(monthlyWeather[key])
    finalWeather[key] = [round(monthlyWeather[key][0] / total, 3), round(monthlyWeather[key][1] / total, 3), round(monthlyWeather[key][2] / total, 3), round(monthlyWeather[key][3] / total, 3)]
    

print(finalWeather)

months = list(finalWeather.keys())
values = list(finalWeather.values())

v1 = [v[0] for v in values]
v2 = [v[1] for v in values]
v3 = [v[2] for v in values]
v4 = [v[3] for v in values]

plt.figure()

plt.bar(months, v1, color='green', label='Good Weather')
plt.bar(months, v2, bottom=v1, color='yellow', label='Fair Weather')

bottom_v3 = [v1[i] + v2[i] for i in range(len(months))]
plt.bar(months, v3, bottom=bottom_v3, color='purple', label='Barely Flyable/ IFR')

bottom_v4 = [bottom_v3[i] + v3[i] for i in range(len(months))]
plt.bar(months, v4, bottom=bottom_v4, color='red', label='Not Flyable')

plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Weather Categories By Month')
plt.xticks(months) 
plt.legend()

plt.tight_layout()
plt.savefig('Graphs/FlightWeatherByMonth')
plt.show()