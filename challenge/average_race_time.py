# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    jen = "Jennifer Rhines"
    jen_times = []
    races = get_data()
    header = races[0]
    race_time_i = header.find("TIME")
    athlete_i = header.find("Athlete")
    date_i = header.find("Race date")
    #date_of_birth_i = header.find("Date of birth")
    #location_i = header.find("Location")

    for race in races[1:]:
        
        race_time = race[race_time_i: athlete_i].strip()
        athlete = race[athlete_i: date_i].strip()
        #date = race[date_i: date_of_birth_i].strip()
        #date_of_birth = race[date_of_birth_i: location_i].strip()
        #location = race[location_i:].strip()
        
        if jen not in athlete:
            continue
        jen_times.append(race_time)


    return jen_times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    
    racetimes = get_rhines_times()

    total = datetime.timedelta()
    for race_t in racetimes:
        m_s_M = re.split(r":|\.", race_t)
        print(m_s_M)

        m = int(m_s_M[0])
        s = int(m_s_M[1])
        M = 0
        if len(m_s_M) == 3:
            M = int(m_s_M[2])
        
        total += datetime.timedelta(minutes= m, seconds= s, milliseconds= M)
    
    return f'{total/len(racetimes)}'[2:-5]
    