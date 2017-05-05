from pyteryt.importer.resourcedownloader import ResourceDownloader

class ResourceImporter(object):
    def __init__(self, latest_resource_finder, local_resource_finder):
        self.__latest_resource_finder = latest_resource_finder
        self.__local_resource_finder = local_resource_finder

    def run_import(self):
        print "Starting importer..."
        resources = self.__get_resources_to_download()
        for resource in resources:
            print "Found %s resource dated %s" % (resource.name, resource.date)
        for resource in resources:
            print "Downloading %s resource" % (resource.name)
            ResourceDownloader(resource).download_resource()
        if len(resources) == 0:
            print "All resources up-to-date, nothing to download"
        print "Finishing importer..."

    def __get_resources_to_download(self):
        latest_resources = self.__latest_resource_finder.find_resources()
        local_resources = self.__local_resource_finder.find_resources()
        resources = [r for r in latest_resources if not self.__contains_newer(local_resources, r)]
        return resources

    def __contains_newer(self, resources, resource):
        return any(r.name == resource.name and r.date >= resource.date for r in resources)
