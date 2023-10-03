import os
import re
class FileListBuilder(object):
    __dirList__ = None
    __apexClassesFolderPath__ = None
    __lwcComponentsFolderPath__ = None
    __auraComponentsFolderPath__ = None    
    __apexClasses__ = []
    __auraComponents__ = []
    __lwcComponents__ = []
    APEX_REGEX_PATTERN = "[\w\d\s]*\.cls$"
    COMPONENTS_REGEX_PATTERN ="[\w\d\s]*$"
    MESSAGE_FORCEAPP_FOLDER_NOT_FOUND = "force-app folder not found in a given folder"
    def __init__(self, projectPath):
        self.__path__=projectPath
        self.__makeFileList()
        
    def __makeFileList(self):        
        for entry in os.scandir(self.__path__):
            if entry.is_dir() and entry.path.endswith("force-app"):
                self.__dirList__ = entry.path
        if self.__dirList__ == None:
            self.__dirList__ = self.MESSAGE_FORCEAPP_FOLDER_NOT_FOUND
        else:
            os.chdir(self.__dirList__+"\\main\\default")
            for entry in os.scandir(self.__dirList__+"\\main\\default"):
                if entry.path.endswith("classes"):
                    self.__apexClassesFolderPath__ = entry.path
                elif entry.path.endswith("lwc"):
                    self.__lwcComponentsFolderPath__ = entry.path
                elif entry.path.endswith("aura"):
                    self.__auraComponentsFolderPath__ = entry.path
        if self.__lwcComponentsFolderPath__:
            self.__getLWCComponentsList()   
        if self.__auraComponentsFolderPath__:
            self.__getAuraComponentsList()
        if self.__apexClassesFolderPath__:
            self.__getApexClassesList()            
        
    def __getLWCComponentsList(self):
        for entry in os.scandir(self.__lwcComponentsFolderPath__):
            if entry.is_dir():                
                self.__getClassOrComponentName(entry.path, False, False)
               
    def __getApexClassesList(self):
        for entry in os.scandir(self.__apexClassesFolderPath__):            
            if entry.is_file() and not entry.path.endswith("xml"):
                self.__getClassOrComponentName(entry.path, True, False)
                
    def __getAuraComponentsList(self):
        for entry in os.scandir(self.__auraComponentsFolderPath__):
            if entry.is_file():
                self.__getClassOrComponentName(entry.path, False, True)

    # Checks end of the path line to determine is this path of apex class or a component, 
    # extracts it name and adds it to one of lists
    def __getClassOrComponentName(self, path, isClass, isAura):        
        regex = (re.compile(self.COMPONENTS_REGEX_PATTERN),re.compile(self.APEX_REGEX_PATTERN))[isClass]
        match = regex.search(path)        
        if match:            
            if isClass:
                 self.__apexClasses__.append(match.group(0)[:-4])
            elif not isClass and isAura:
                self.__auraComponents__.append(match.group(0))
            elif not isClass and not isAura:
                self.__lwcComponents__.append(match.group(0))

    def getAuraComponents(self):
        return self.__auraComponents__

    def getLWCComponents(self):
        return self.__lwcComponents__

    def getApexClasses(self):
        return self.__apexClasses__

    def printList(self):
        
        print (self.__apexClasses__)
        print (self.__lwcComponents__)
