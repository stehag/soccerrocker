import requests

def getMatches():
    m = matchids()
    v = []
    for matchid in m:
        match = fetchMatchData(matchid)
        leauge = match['matchData']['competition']['displayName']
        # Add more leagues here if necessary :)
        if( leauge == 'European Qualifiers' or leauge == 'European Qualifiers'):
            v.append(match)
            print("Added: " + leauge + " : " + match['homeTeam'] + " vs " + match['awayTeam'] + " " + match['date'])
        else:
            print("Excluding: " + leauge +" : " + match['homeTeam'] +" vs "+ match['awayTeam'] + " " + match['date'])


    return v


def fetchMatchData(matchid):
    r = requests.get('https://digital-api.uefa.com/v1/matches/' + str(matchid) + '/statistics/team?language=EN')

    if r.ok:
        statsData = r.json()

    r = requests.get('https://digital-api.uefa.com/v1/matches/' + str(matchid) )
    if r.ok:
        matchData = r.json()

    competition = matchData['competition']['displayName']
    homeTeam = matchData['homeTeam']['displayTeamCode']
    awayTeam = matchData['awayTeam']['displayTeamCode']
    date = matchData['kickoffTime']['date']


    match = {'matchId':  matchid,
             'competition': competition,
             'date' : date,
             'homeTeam': homeTeam,
             'awayTeam': awayTeam ,
             'stats': statsData,
             'matchData': matchData }
    return match

def matchids():
      #  return  list(range(2025990, 2029994))
      return list(range(2025990, 2026994))

