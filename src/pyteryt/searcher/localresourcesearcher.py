from __future__ import print_function

from pyteryt.searcher.nestedloopsjoin import NestedLoopsJoin
from pyteryt.searcher.provincerepository import ProvinceRepository
from pyteryt.searcher.cityrepository import CityRepository
from pyteryt.searcher.streetrepository import StreetRepository

class LocalResourceSearcher(object):
    def __init__(self):
        data_source = None
        self.__join_algorithm = NestedLoopsJoin()
        self.__province_repository = ProvinceRepository(data_source)
        self.__city_repository = CityRepository(data_source)
        self.__street_repository = StreetRepository(data_source)

    def search(self, province_name, city_name, street_name):
        print ('Searching for province: %s, city: %s, street: %s' %
               (province_name if province_name else '(all)',
                city_name if city_name else '(all)',
                street_name if street_name else '(all)'))
        provinces = self.__get_provinces(province_name)
        cities = self.__get_cities(city_name)
        streets = self.__get_streets(street_name)
        combined = self.__get_combined_results(provinces, cities, streets)
        return combined

    def __get_provinces(self, province_name):
        print ('Looking for provinces... ', end='')
        provinces = self.__province_repository.find_provinces(province_name)
        print ('found %s results' % (len(provinces)))
        return provinces

    def __get_cities(self, city_name):
        print ('Looking for cities... ', end='')
        cities = self.__city_repository.find_cities(city_name)
        print ('found %s results' % (len(cities)))
        return cities

    def __get_streets(self, street_name):
        print ("Looking for streets... ", end='')
        streets = self.__street_repository.find_streets(street_name)
        print ('found %s results' % (len(streets)))
        return streets

    def __get_combined_results(self, provinces, cities, streets):
        print ("Combining results... ", end='')
        combined = self.__join_algorithm.join(provinces, cities,
            lambda x, y: x['province_id'] == y['province_id'])
        combined = self.__join_algorithm.join(combined, streets,
            lambda x, y: x['province_id'] == y['province_id'] and x['city_id'] == y['city_id'])
        print ('found %s results' % (len(combined)))
        return combined
