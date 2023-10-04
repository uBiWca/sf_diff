import fileReader
import re
class ApexParser(object):
    CUSTOM_OBJECT_NAME_REGEX = "\w*__c|__C"
    CUSTOM_FIELD_NAME_REGEX = ".\w*__c|__C"
    __apexClasses__ = []
    __apexClassesPaths__ = {}
    __fieldsNames__ = []
    def __init__(self, fileReader):
        self.__apexClasses__ = fileReader.getApexClasses()
        self.__apexClassesPaths = fileReader.getApexClassPath()
    #Parses class content and extracts all custom fields names
    #
    def __searchClassForFields__(self, classContent):
        regex = re.compile(self.CUSTOM_OBJECT_NAME_REGEX)
        result = regex.findall(classContent) 
        if result:
            for fieldNamde in result:
                strippedName = fieldNamde[1:]
                if strippedName not in self.__fieldsNames__:
                    self.__fieldsNames__.append(strippedName)
    
