import os
import fnmatch
import xml.etree.ElementTree as ET

class StreetRepository(object):
    def __init__(self, data_source):
        self.__DATA_FOLDER = os.path.expanduser('~/.pyteryt/data')

    def find_streets(self, search_name):
        path = os.path.join(self.__DATA_FOLDER, 'ULIC.xml')
        root = ET.parse(path).getroot()
        return self.__get_streets(root, search_name)

    def __get_streets(self, root, search_name):
        streets = []
        for row in root.findall('./catalog/row'):
            street_name = row.find("./col[@name='NAZWA_1']").text
            if row.find("./col[@name='NAZWA_2']").text != None:
                street_name = row.find("./col[@name='NAZWA_2']").text + street_name
            if search_name and not fnmatch.fnmatch(street_name.lower(), search_name.lower()):
                continue
            street_feature = row.find("./col[@name='CECHA']").text
            province_id = row.find("./col[@name='WOJ']").text
            city_id = row.find("./col[@name='SYM']").text
            street = {'street_feature': street_feature, 'street_name': street_name,
                      'province_id': province_id, 'city_id': city_id}
            streets.append(street)
        return streets
