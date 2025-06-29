class Entry(object):
    def __init__(self, data, teams, matchups):
        self.entry_id = data['id']
        self.entry_name = data['name']
        self.entry_url = data['url']
        self.avatar_url = data['avatarUrl']
        self.roles = data['roles']
        self.member_id = data['memberId']
        self.total_picks_count = data['totalPicksCount']
        self.max_picks_count = data['maxPicksCount']
        self.pool_rank = data['poolRank']
        self.correct_picks = data['correctPicks']
        self.points = data['fantasyPoints']
        self.max_points = data['maxPoints']
        self.user_info = data['userInfo']
        self.champion_team = data['championTeam']
        self.pool = data['pool']
        self.tiebreaker = data['tiebreakerAnswers']
        self._format_picks(data, teams, matchups)

    def __repr__(self):
        return f'Entry({self.entry_name})'

    def _format_picks(self, data, teams, matchups):
        self.picks = {}
        picks_data = data['picks']
        for pick in picks_data:
            picked_team = None
            picked_matchup = None
            pick_team_id = pick['itemId']
            pick_slot_id = pick['slotId']
            for team in teams:
                if pick_team_id == team.team_id:
                    picked_team = team
                    break
            for matchup in matchups:
                if pick_slot_id == matchup.matchup_id:
                    picked_matchup = matchup
                    break
            if picked_team and picked_matchup:
                self.picks[picked_matchup] = picked_team

