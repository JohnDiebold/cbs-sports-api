from cbs_requests import CBSSportsRequests
from pool import Pool
from matchup import Matchup
from team import Team
from entry import Entry


class Bracket(object):
    def __init__(self, pool_id: str, fetch_all_entries: False):
        self.pool_id = pool_id
        self.cbs_request = CBSSportsRequests(pool_id=pool_id)
        self._fetch_pool()
        self._fetch_teams()
        self._fetch_matchups()
        if fetch_all_entries:
            self._fetch_all_entries()

    def _fetch_pool(self):
        details = self.cbs_request.pool_details()['data']['pool']
        standings = self.cbs_request.pool_standings()['data']['gameInstance']['pool']
        self.pool = Pool(details=details, standings=standings)

    def _fetch_teams(self):
        self.teams = []
        data = self.cbs_request.cbs_teams()
        for team in data['data']['teams']:
            self.teams.append(Team(data=team))

    def _fetch_matchups(self):
        self.matchups = []
        data = self.cbs_request.pool_period()
        for matchup in data['data']['gameInstance']['period']['matchups']:
            self.matchups.append(Matchup(data=matchup, teams=self.teams))

    def _fetch_all_entries(self):
        self.entries = []
        for entry_id in self.pool.entry_ids:
            entry = self.entry_details(entry_id=entry_id)
            self.entries.append(entry)

    def entry_details(self, entry_id: str):
        data = self.cbs_request.entry(entry_id=entry_id)['data']['entry']
        return Entry(data=data, teams=self.teams, matchups=self.matchups)
