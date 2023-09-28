import os
class FileListBuilder(object):
    __dirList__ = None
    __apexClassesFolderPath__ = None
    __lwcComponentsFolderPath__ = None
    __auraComponentsFolderPath__ = None
    __lwcComponentsList__= []
    __lwcCompnentsPathsMap__ = {}
    __auraComponentsList__= []
    __auraComponentsPathsMap__ = {}
    __apexClassesList__= []
    APEX_REGEX_PATTERN = "\\.+\.cls$"
    MESSAGE_FORCEAPP_FOLDER_NOT_FOUND = "force-app folder not found in a given folder"
    def __init__(self, projectPath):
        self.__path__=projectPath
        self.__makeFileList()
        
    def __makeFileList(self):        
        for entry in os.scandir(self.__path__):
            if entry.is_dir and entry.path.endswith("force-app"):
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
        # for (root, dirs, file) in os.walk(self.__path__)
        #     for dir in dirs:
        #         self.dirList.append(dir)
    def __getLWCComponentsList(self):
        for entry in os.scandir(self.__lwcComponentsFolderPath__):
            if entry.is_dir:
                self.__lwcComponentsList__.append(entry.path)
                for componentElement in os.scandir(entry.path):
                    if not componentElement.path.endswith("xml") and not componentElement.is_dir:
                        self.__lwcCompnentsPathsMap__[componentElement.path.s]
    def __getApexClassesList(self):
        for entry in os.scandir(self.__apexClassesFolderPath__):
            if entry.is_dir and not entry.path.endswith("xml"):
                self.__apexClassesList__.append(entry.path)
    def __getAuraComponentsList(self):
        for entry in os.scandir(self.__auraComponentsFolderPath__):
            if entry.is_dir:
                self.__auraComponentsList__.append(entry.path)
    def printList(self):
        # print (self.__apexClassesFolderPath__)
        # print (self.__lwcComponentsFolderPath__)
        # print (self.__auraComponentsFolderPath__)
        # print (self.__lwcComponentsList__)
        # print (self.__auraComponentsList__)
        print (self.__apexClassesList__)
