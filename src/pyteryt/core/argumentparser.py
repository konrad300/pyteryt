# -*- coding: utf-8 -*-

import argparse

PROGRAM_DESCRIPTION = '''
This script allows searching Polish TERYT database
(Krajowy Rejestr Urzędowego Podziału Terytorialnego Kraju)

The database files are downloaded automatically from
the official TERYT website. Future updates are downloaded
only if the file version on the website in newer than
the one stored locally. The local storage is located at:
~/.pyteryt/data/

User can supply none, some or all of the supported
search arguments, which are: province, city, street.
Combining more search arguments narrows down the result
set (AND condition between arguments). Search arguments
are case-insensitive.

Unix shell-style wildcards are fully supported, for more
details check http://www.linfo.org/wildcard.html
'''

PROGRAM_EPILOG = '''
examples:

$ pyteryt
[Will return all results; Because of slowness, do not execute]

$ pyteryt -p małopolskie -s Grodzka
Province: małopolskie, City: Mogilany, Street: ul. Grodzka
Province: małopolskie, City: Jadowniki, Street: ul. Grodzka
Province: małopolskie, City: Brodła, Street: ul. Grodzka
Province: małopolskie, City: Kraków-Śródmieście, Street: ul. Grodzka
Province: małopolskie, City: Wojnicz, Street: ul. Grodzka
Province: małopolskie, City: Wielmoża, Street: ul. Grodzka
Province: małopolskie, City: Nowy Sącz, Street: ul. Grodzka
Province: małopolskie, City: Biecz, Street: ul. Grodzka

$ pyteryt -c Kraków* -s "Stefana [CS]*"
Province: małopolskie, City: Kraków-Podgórze, Street: ul. Stefana Czarnieckiego
Province: małopolskie, City: Kraków-Podgórze, Street: ul. Stefana Stolarza
Province: małopolskie, City: Kraków-Podgórze, Street: ul. Stefana Starzyńskiego
'''

class ArgumentParser(object):
    def parse(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=PROGRAM_DESCRIPTION, epilog=PROGRAM_EPILOG)
        parser.add_argument('-p', '--province', help='search streets by province name')
        parser.add_argument('-c', '--city', help='search streets by city name')
        parser.add_argument('-s', '--street', help='search streets by street name')
        arguments = parser.parse_args()
        dictionary = self.__to_dictionary(arguments.province, arguments.city, arguments.street)
        return dictionary

    def __to_dictionary(self, province, city, street):
        encoded = {'province': self.__string_to_unicode(province),
                   'city': self.__string_to_unicode(city),
                   'street': self.__string_to_unicode(street),
                  }
        return encoded

    def __string_to_unicode(self, input_string):
        if input_string is None:
            return None
        return input_string.decode('utf-8')
