class Pool(object):
    def __init__(self, details, standings):
        self.pool_id = details['id']
        self.pool_name = details['name']
        self.pool_slogan = details['slogan']
        self.pool_url = details['url']
        self.pool_settings = details['poolSettings']
        self.entries_count = details['entriesCount']
        self.members_count = details['membersCount']
        self.season = details['season']['season']
        self.year = details['season']['year']
        self.periods = details['season']['whenToWatch']
        self.entries_with_picks_count = standings['entriesWithPicksCount']
        self.entries = standings['entries']['edges']
        self.entry_ids = []
        for entry in self.entries:
            self.entry_ids.append(entry['node']['id'])

    def __repr__(self):
        return f'Pool({self.pool_name})'


