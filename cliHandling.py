import argparse
class CliHandling(object):
    __parser__ = None
    __arguments__ = None
    def __init__(self):
        self.__parser__ =argparse.ArgumentParser(description="""This app is used to analize Salesforce projetc content 
        and to compare it against target Org, in order to find custom objects and fields not existing in target Org, but
        referenced in project. It also can generate package.xml file, containing all differences found and compare classes
        and components content in order to determine, which of them needs to be deployed.""")
        self.__parser__.add_argument(['--projectPath', '--path', 'p'], action='store', help="""Path to \'main\' folder.""")
        self.__parser__.add_argument(['--makePackage', '--mkp', 'mp'], action='store', help="""Generate package.xml 
        with found differencies""", type=bool)
        self.__parser__.add_argument(['--packagePath', '--pkp', 'pp'], action='store', help="""Folder to create package.xml in""")
        self.__arguments__ = self.__parser__.parse_args()
    def getProjectPath(self):
        return self.__arguments__.projectPath
    def getIsNeedPackage(self):
        return self.__arguments__.makePackage
    def getPackagePath(self):
        return self.__arguments__.packagePath