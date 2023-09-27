import os
class FileListBuilder(object):
    __dirList__ = None
    apexClassesFolderPath = None
    lwcComponentsFolderPath = None
    auraComponentsFolderPath = None
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
                print(entry.path)
        # for (root, dirs, file) in os.walk(self.__path__):
        #     for dir in dirs:
        #         self.dirList.append(dir)
    def printList(self):
        print (self.__dirList__)
