class Team(object):
    def __init__(self, data):
        self.team_id = data['id']
        self.abbreviation = data['abbrev']
        self.location = data['location']
        self.nickname = data['nickName']
        self.short_name = data['shortName']
        self.sport = data['sportType']
        self.hexadecimal_color = data['colorHexDex']
        self.primary_color = data['colorPrimaryHex']
        self.secondary_color = data['colorSecondaryHex']
        self.conference_abbreviation = data['conferenceAbbrev']
        self.cbs_team_id = data['cbsTeamId']
        self.wins = data['wins']
        self.losses = data['losses']
        self.ties = data['ties']
        self.image_url = data['imageUrl']
        self.medium_name = data['mediumName']

    def __repr__(self):
        return f'Team({self.location})'
