import datetime
import re
import os
import string

from pyteryt.importer.resource import Resource

class LocalResourceFinder(object):
    def __init__(self):
        self.__DATA_FOLDER = os.path.expanduser('~/.pyteryt/data')
        self.__RESOURCE_RE = (
            r'date=\"(?P<date>\d{4}-\d{2}-\d{2})\">' # date
        )

    def find_resources(self):
        if not os.path.exists(self.__DATA_FOLDER):
            return []
        resources = []
        for file_name in os.listdir(self.__DATA_FOLDER):
            resource = self.__read_resource(file_name)
            resources.append(resource)
        return resources

    def __read_resource(self, file_name):
        file_path = os.path.join(self.__DATA_FOLDER, file_name)
        with open(file_path) as file_stream:
            name = self.__get_resource_name(file_name)
            data = file_stream.read()
            date = self.__scan_date(data)
            resource = Resource(name, file_path, date)
            return resource

    def __scan_date(self, data):
        match = re.search(self.__RESOURCE_RE, data)
        date = datetime.datetime.strptime(match.group('date'), '%Y-%m-%d').date()
        return date

    def __get_resource_name(self, file_name):
        name = string.rsplit(file_name, '.', 1)[-2]
        return name
