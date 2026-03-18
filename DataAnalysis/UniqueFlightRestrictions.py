import json


jsonPaths = ['RestrictionsData/FlightRestrictionData1.json', 'RestrictionsData/FlightRestrictionData2.json']


uniqueRestrictions = []

for path in jsonPaths:
    with open(path, 'r') as f:
        data = json.load(f)
    for record in data:
        try:
            restriction = record[1][0]
        except:
            pass
          #  print(record)
        if restriction not in uniqueRestrictions: uniqueRestrictions.append(restriction)

print(uniqueRestrictions)





#output: ['Closed', 'No Dispatch', 'No Fly', 'Dual Local Only', 'Turbine Only', 'No Dispatch - Due to Ramp Conditions', 'Dual Only - Stage checks and Semi only', 'Dual Only', 'Dual Local Only - Stage Check Only', 'Solos Per METAR/TAF/NOTAM', '', 'No Spins/Aerobatics', 'Solos Traffic Pattern Only', 'No Student Pilot Solos', 'No Cessna / No Tailwheel', 'Garfield', 'Dual Pattern Only', 'No Restrictions', 'No Fly / No Dispatch due to ramp conditions', 'Dual Local Only - Family Weekend Flights', 'No Fly - Family Weekend Flights', 'No Student Pilot Solo XC', 'No Restrictions Family Weekend Flights', 'No Dispatch - Due to Convective Activity', 'IFR Dual Only', 'No Solo XC', 'Student Pilot Solo Traffic Pattern Only', 'IFR Dual Only  | VFR Dual Pattern Only', 'Dual Only - SEMI/Stage Check/ XC Only', 'Summer Camp Only', 'No Private Pilot Local Solo', 'No Student Pilot Solos | Private Local', 'No Student Pilot Solos / Private Local', 'No Student Pilot Solos or Private Local', 'No Night Solo XC', 'No XC', 'Dual Local Only | PIREPs Appreciated!', 'Dual Only | PIREPs Appreciated!', 'Pattern Only', 'No Student Pilot Solos | PIREPs Appreciated!', 'No Student Pilot Solos | Private Pilot Local Only', 'Dual Pattern Only | No Cessna | No Tailwheel', 'Solos Per METAR/TAF/NOTAM | No Cessna | No Tailwheel', 'Dual Local Only | No Cessna | No Tailwheel', 'Semi/Stage/Dual only', 'Semi/Stage/Dual/Spins Only', 'No Cessna /No Tailwheel Dual Only', 'Family Weekend No Fly', 'VFR Dual Pattern Only | IFR Dual Only', 'No Green Solos', 'SEMI, Stage, Dual XC Only', 'No Fly :(', 'Dual Pattern Only - No Cessna / No Tailwheel', 'Dual Only - No Cessna / No Tailwheel', 'SEMI/Stage/Dual Only', 'No Spins / Aerobatics', 'Family Weekend - Solos Per METAR/TAF/NOTAM', 'Family Weekend - Solos/Dual Allowed', 'No Solo Private Local', 'Semi, Stage, Solo, XC, and Perm Only', 'Student Pilot Solo Traffic Pattern Only / No Solo XC', 'Student Pilot Solo Traffic Pattern Only , No XC S', 'Dual Only - No Acro/Spins', 'Dual Only -- No Dispatch N', 'Semi/Stage/Solo/XC', 'Semi/Stage/XC Only', 'Semi/Stage/XC/PERM Only', 'No Dual VFR XC', 'No DECA Spins / Aerobatics', 'Dual Only - No DECA Acro/Spins', 'No Aerobatics', 'Solos Per METAR/TAF/NOTAM | No DECA', 'Dual Only | No DECA', 'Solos Traffic Pattern Only | No DECA', 'No Solo XC | No DECA', 'Solos Per METAR/TAF/NOTAM - No DECA Acro/Spins']