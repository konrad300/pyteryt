import urllib2
import re
import datetime

from pyteryt.importer.resource import Resource

class LatestResourceFinder(object):
    def __init__(self):
        self.__TERYT_WEBPAGE_URL = 'http://www.stat.gov.pl/broker/access/prefile/listPreFiles.jspa'
        self.__TERYT_WEBPAGE_PREFIX = 'http://www.stat.gov.pl/broker/access/prefile'
        self.__RESOURCE_RE = (
            r'(?P<name>SIMC|ULIC|TERC|WMRODZ).*?' # name
            r'(?P<date>\d{4}-\d{2}-\d{2}).*?'     # date
            r'<a href=\"(?P<url>[^\"]*)\">'       # url
        )

    def find_resources(self):
        webpage = self.__fetch_webpage()
        resources = self.__scrape_resources(webpage)
        return resources

    def __fetch_webpage(self):
        response = urllib2.urlopen(self.__TERYT_WEBPAGE_URL)
        return response.read()

    def __scrape_resources(self, webpage):
        iterator = re.compile(self.__RESOURCE_RE, re.DOTALL).finditer(webpage)
        resources = []
        for match in iterator:
            name = match.group('name')
            date = datetime.datetime.strptime(match.group('date'), '%Y-%m-%d').date()
            url = "%s/%s" % (self.__TERYT_WEBPAGE_PREFIX, match.group('url'))
            resource = Resource(name, url, date)
            resources.append(resource)
        return resources
