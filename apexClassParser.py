import fileReader
import re


class ApexParser(object):
    CUSTOM_OBJECT_NAME_REGEX = "(\(|\(\s*|[new\s*])(\w*__c|__C)(?=\s)"
    CUSTOM_FIELD_NAME_REGEX = ".\w*__c|__C"
    __apexClasses__ = []
    __apexClassesPaths__ = {}
    __fieldsNames__ = []

    def __init__(self, fileReader):
        self.__apexClasses__ = fileReader.getApexClasses()
        self.__apexClassesPaths = fileReader.getApexClassPath()
        self.__parseFiles__()
    # Iterates over classes list and extracts all custom fields names and custom objects names

    def __parseFiles__(self):
        if self.__apexClassesPaths__:
            for apexClass in self.__apexClassesPaths__.values():
                file = open(apexClass, 'r')
                self.__searchClassForFields__(file)
    # Parses class content and extracts all custom objects names

    def __searchClassForObjects__(self, classContent):
        regex = re.compile(self.CUSTOM_OBJECT_NAME_REGEX)
        result = regex.findall(classContent)
        if result:
            for objectName in result:
                strippedName = fieldNamde[1:]
                if strippedName not in self.__fieldsNames__:
                    self.__fieldsNames__.append(strippedName)
    # Parses class content and extracts all custom fields names
    #

    def __searchClassForFields__(self, classContent):
        regex = re.compile(self.CUSTOM_OBJECT_NAME_REGEX)
        result = regex.findall(classContent)
        if result:
            for fieldNamde in result:
                strippedName = fieldNamde[1:]
                if strippedName not in self.__fieldsNames__:
                    self.__fieldsNames__.append(strippedName)
