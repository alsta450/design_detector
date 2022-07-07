

from best_practice_finder.api_gateway_finder import ApiGatewayFinder
from best_practice_finder.database_connector import DatabaseConnector
from best_practice_finder.https_finder import HttpsFinder

from logger import LoggerGenerator


class BestPracticeHandler():
    '''Best practices can be added to this class'''
    def __init__(self) -> None:
        self._database_connector = DatabaseConnector()
        self._api_gateway_finder = ApiGatewayFinder()
        self._https_finder = HttpsFinder()
        self.logger = LoggerGenerator(__class__.__name__).get_logger()


    def find_best_practices(self,datahandler):
        '''Find best practices, new best practices can be added here'''
        self._database_connector.connect_database_to_microservices(datahandler)
        self._api_gateway_finder.find_api_gateway(datahandler)
        self._https_finder.find_https_setup(datahandler)


