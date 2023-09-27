import os
class FileListBuilder(object):
    dirList = []
    def __init__(self, projectPath):
        self.__path__=projectPath
        self.__makeFileList()
        
    def __makeFileList(self):
        obj = os.scandir(self.__path__)
        for entry in obj:
            if (entry.is_dir):
                self.dirList.append(entry.path)
        # for (root, dirs, file) in os.walk(self.__path__):
        #     for dir in dirs:
        #         self.dirList.append(dir)
    def printList(self):
        print (self.dirList)
