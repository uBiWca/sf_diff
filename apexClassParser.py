import fileReader

class ApexParser(object):
    __apexClasses__ = []
    __apexClassesPaths = {}
    def __init__(self, fileReader):
        self.__apexClasses__ = fileReader.getApexClasses()
        self.__apexClassesPaths = fileReader.getApexClassPath()
        