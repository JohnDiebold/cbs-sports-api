class Matchup(object):
    def __init__(self, data, teams):
        self.matchup_id = data['id']
        self.tournament_id = data['tournamentId']
        self.tournament_description = data['tournamentDescription']
        self.tournament_round = data['tournamentRound']
        self.round_ordinal = data['roundOrdinal']
        self.top_seed = data['topItemSeed']
        self.bottom_seed = data['bottomItemSeed']
        self.top_id = data['topItemId']
        self.bottom_id = data['bottomItemId']
        self.winner_plays_into_ordinal = data['winnerPlaysIntoOrdinal']
        self.winner_plays_into_position = data['winnerPlaysIntoPosition']
        self.winner_id = data['winnerId']
        self.group_position = data['groupPosition']
        self.group_name = data['groupName']
        self.tournament_round_name = data['tournamentRoundName']
        self.is_play_in = data['isPlayin']
        self.slot_ids = data['slotIds']
        self.advancement_id = data['advancementId']
        self.event_id = data['event']['id']
        self.event_starts_at = data['event']['startsAt']
        self.winning_team_id = data['event']['winningTeamId']
        self.home_team_score = data['event']['homeTeamScore']
        self.away_team_score = data['event']['awayTeamScore']
        self.game_status = data['event']['gameStatusDesc']
        self.time_remaining = data['event']['timeRemaining']
        self.game_period = data['event']['gamePeriod']
        self.tv_name = data['event']['tvInfoName']
        self.possession = data['event']['possession']
        self.home_team_id = data['event']['homeTeamId']
        self.away_team_id = data['event']['awayTeamId']
        self.top_name = ''
        self.bottom_name = ''
        for team in teams:
            if self.top_id == team.team_id:
                self.top_name = team.location
            elif self.bottom_id == team.team_id:
                self.bottom_name = team.location
            if self.top_name and self.bottom_name:
                break

    def __repr__(self):
        if self.top_name and self.bottom_name:
            if self.tournament_round_name == 'First Four' or self.tournament_round_name == 'Final Four':
                return f'Matchup({self.tournament_round_name} {self.top_name} vs. {self.bottom_name})'
            else:
                return f'Matchup({self.group_name} {self.tournament_round_name} {self.top_name} vs. {self.bottom_name})'
        return f'Matchup({self.group_name} {self.tournament_round_name} Game {self.round_ordinal})'
