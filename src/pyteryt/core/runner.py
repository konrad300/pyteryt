import sys

from pyteryt.core.argumentparser import ArgumentParser
from pyteryt.importer.latestresourcefinder import LatestResourceFinder
from pyteryt.importer.localresourcefinder import LocalResourceFinder
from pyteryt.importer.resourceimporter import ResourceImporter
from pyteryt.searcher.localresourcesearcher import LocalResourceSearcher

def main():
    argument_parser = __get_argument_parser()
    arguments = argument_parser.parse()
    importer = __get_resource_importer()
    importer.run_import()
    searcher = LocalResourceSearcher()
    results = searcher.search(arguments['province'], arguments['city'], arguments['street'])
    __display_results(results)

def __get_argument_parser():
    parser = ArgumentParser()
    return parser

def __get_resource_importer():
    latest_resource_finder = LatestResourceFinder()
    local_resource_finder = LocalResourceFinder()
    return ResourceImporter(latest_resource_finder, local_resource_finder)

def __display_results(results):
    print "Printing results..."
    for item in results:
        print "Province: %s, City: %s, Street: %s %s" % \
            (item['province_name'], item['city_name'], item['street_feature'],
             item['street_name'])
