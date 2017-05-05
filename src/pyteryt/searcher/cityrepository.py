import os
import fnmatch
import xml.etree.ElementTree as ET

class CityRepository(object):
    def __init__(self, data_source):
        self.__DATA_FOLDER = os.path.expanduser('~/.pyteryt/data')

    def find_cities(self, search_name):
        path = os.path.join(self.__DATA_FOLDER, 'SIMC.xml')
        root = ET.parse(path).getroot()
        return self.__get_cities(root, search_name)

    def __get_cities(self, root, search_name):
        cities = []
        for row in root.findall('./catalog/row'):
            city_name = row.find("./col[@name='NAZWA']").text
            if search_name and not fnmatch.fnmatch(city_name.lower(), search_name.lower()):
                continue
            city_id = row.find("./col[@name='SYM']").text
            province_id = row.find("./col[@name='WOJ']").text
            city = {'city_id': city_id, 'city_name': city_name, 'province_id': province_id}
            cities.append(city)
        return cities
