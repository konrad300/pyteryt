import os
import urllib2
import zipfile
import StringIO

class ResourceDownloader(object):
    def __init__(self, resource):
        self.__DATA_FOLDER = os.path.expanduser('~/.pyteryt/data')
        self.__resource = resource

    def download_resource(self):
        data = self.__fetch_resource()
        self.__extract_resource(data)

    def __fetch_resource(self):
        url_stream = urllib2.urlopen(self.__resource.url)
        return url_stream.read()

    def __extract_resource(self, data):
        stringio = StringIO.StringIO(data)
        with zipfile.ZipFile(stringio) as zip_stream:
            zip_stream.extractall(self.__DATA_FOLDER)
