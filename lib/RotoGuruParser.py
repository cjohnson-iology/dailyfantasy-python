import collections
import logging
import re

class RotoGuruParser:

    def __init__(self,**kwargs):
        if 'logger' in kwargs:
            self.logger = kwargs['logger']
        else:
            self.logger = logging.getLogger(__name__)

    def nba_players(self, content):    
        players = []

        # they have HIDEOUS html in these files
        # first have to find where the good stuff starts and ends
        match = re.search(r'(gid;.*?)<br>\n(.*?)<hr>', content, re.MULTILINE|re.DOTALL|re.IGNORECASE)

        if match:
            # group 1 is gid;xxx;final_header
            header_line = match.group(1)
            self.logger.debug(header_line)

            # group 2 is everything else; will have to split on <br> and newline
            player_lines = match.group(2).split("<br>\n")
            self.logger.debug(player_lines)

            # header_line should be semi-colon separated data
            if header_line:
                header_parts = header_line.split(';')
                self.logger.debug(header_parts)
                headers = [re.sub('\s+', '_', p).strip() for p in header_parts]
                self.logger.debug(headers)

            # each player_line is semi-colon separated, need to remove whitespace
            # use ordered collection for debugging ease (parameter order in GET)
            # but can also use an ordinary dictionary
            if player_lines:
                for pl in player_lines:
                    player_parts = [p.strip() for p in pl.split(';')]
                    self.logger.debug(player_parts)
                    player = dict(zip(headers, player_parts))
                    self.logger.debug(player)
                    players.append(player)

        return players


if __name__ == '__main__':
    pass