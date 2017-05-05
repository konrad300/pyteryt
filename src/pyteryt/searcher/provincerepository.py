import os
import fnmatch
import xml.etree.ElementTree as ET

class ProvinceRepository(object):
    def __init__(self, data_source):
        self.__DATA_FOLDER = os.path.expanduser('~/.pyteryt/data')

    def find_provinces(self, search_name):
        path = os.path.join(self.__DATA_FOLDER, 'TERC.xml')
        root = ET.parse(path).getroot()
        provinces = self.__get_provinces(root, search_name)
        return provinces

    def __get_provinces(self, root, search_name):
        provinces = []
        for row in root.findall('./catalog/row'):
            for col in row:
                if col.get('name') == 'POW' and col.text is None:
                    province_name = row.find("./col[@name='NAZWA']").text.lower()
                    if search_name and not fnmatch.fnmatch(province_name, search_name.lower()):
                        continue
                    province_id = row.find("./col[@name='WOJ']").text
                    province = {'province_id': province_id, 'province_name': province_name}
                    provinces.append(province)
        return provinces
