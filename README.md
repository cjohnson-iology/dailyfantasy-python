# dailyfantasy-python
collection of python libraries for gathering data about daily fantasy games.
also has some database scripts (table creation & stored procedures)

## file list

### rotoguru-nba.py

This is the bootstrap script for getting all of the 2014-15 (and future season when applicable)
salary and player data from rotoguru.net. Uses the RotoGuruParser and RotoGuruScraper classes. Right now, saves results to a pickle file. Need to add mysql and mongodb support.

### /data

#### rg.html

This is a response for a query of a single day of statistics

#### rotoguru_alternate_html_files.tar.gz

Before I realized there was a query page that returned semi-colon separated values, I downloaded these webpages which are more difficult to scrape because they contain numerous nested tables with no class/id and unstructured data. I am saving these in case something goes wrong with querying for the semi-colon separated values data.

### /lib

#### RotoGuruParser.py

Used to parse HTML from rotoguru.net (most likely by way of RotoGuruScraper class). The HTML on this site is horrible, so it has to use regular expressions rather than a parsing library such as BeautifulSoup.

Methods: <pre>nba_players</pre>

#### RotoGuruScraper.py

Used to scrape HTML from rotoguru.net. The CGI application on this site forces you to specify every parameter in the request or it throws an error, so the query string is quite long and convoluted.

Methods: <pre>nba_players, _get_from_file, _get_from_web</pre>

### /sql

#### sp_draftkings_nba_fantasypoints.sql

This stored procedure takes a table name and a minutes floor and calculates draftkings fantasy points for those players. Right now, assumes certain field names. Does not calculate bonuses for double-double and triple-double

### /test


