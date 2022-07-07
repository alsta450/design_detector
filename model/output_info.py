

from model.api_info import ApiInfo
from model.database_info import DatabaseInfo
from model.https_info import HttpsInfo


class OutputInfo():
    '''Collected information for output'''
    def __init__(self,name) -> None:
        self._name = name
        self._api_info: ApiInfo= ApiInfo()
        self._database_info: DatabaseInfo = DatabaseInfo()
        self._https_info: HttpsInfo = HttpsInfo()

