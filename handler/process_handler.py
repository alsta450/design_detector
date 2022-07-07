

from handler.best_practice_handler import BestPracticeHandler
from handler.connection_handler import ConnectionHandler
from handler.data_handler import DataHandler
from handler.diagram_handler import DiagramHandler
from handler.extraction_handler import ExtractionHandler
from handler.json_handler import JsonHandler

from handler.security_handler import SecurityHandler
from logger import LoggerGenerator

class ProcessHandler():
    
    def __init__(self,root) -> None:
        self._extraction_handler = ExtractionHandler(root)
        self._data_handler = DataHandler()
        self._security_handler = SecurityHandler()
        self._diagram_handler = DiagramHandler(self._data_handler)
        self._best_practice_handler = BestPracticeHandler()
        self._connection_handler = ConnectionHandler(self._data_handler)
        self.json_handler = JsonHandler(self._data_handler)
        self.logger = LoggerGenerator(__class__.__name__).get_logger()



    def run(self):
        '''Call each step of the design detection process'''
        self.logger.info("Gathering information from file system...")
        self.gather_information()
        self.logger.info("Identifying best practices...")
        self.find_best_practices()
        self.logger.info("Starting security audit...")
        self.security_audit()
        self.logger.info("Creating output json...")
        self.json_handler.create_json(self._data_handler)
        self.logger.info("Creating architecture diagram...")
        self.create_diagram()
        return self.json_handler.output_dict


    def gather_information(self):
        '''Extract path, build a path tree and extract all files'''
        self.logger.info("Extracting path...")
        self.extract_path()
        self.logger.info("Building path tree...")
        self.build_tree()
        self.logger.info("Extracting all files in root...")
        self.extract_all_files_in_root()
        self.logger.info("Extracting all files in microservices...")
        self.extract_all_files_in_microservices()


    def find_best_practices(self):
        '''Detect best practices'''
        self._best_practice_handler.find_best_practices(self._data_handler)

    def extract_all_files_in_root(self):    
        '''Extract all files in root folder''' 
        self._extraction_handler.extract_all_files_in_root(self._data_handler)   


    def create_diagram(self):
        '''Create the diagram overview'''
        self.logger.info("Adding diagram dict...")
        self._data_handler.add_diagram_dict(self._connection_handler.connect_microservices())
        
        self.logger.info("Creating diagram...")
        self._diagram_handler.create_object(self._data_handler.root_instance._diagram_dict)

    def security_audit(self):
        '''Detect security design decisions'''
        self._security_handler.do_audit(self._data_handler)

    def build_tree(self):
        '''Build a tree of the folder structure'''
        result = self._extraction_handler.build_tree(self._data_handler.root_instance.root)
        self._data_handler.add_tree(result)

    def extract_path(self):
        '''Add Component instances per microservice and the Architecture instance'''
        self._data_handler.add_componnents(self._extraction_handler.find_all_docker_root())
        self._data_handler.add_architecture(self._extraction_handler.find_file(self._extraction_handler._root,"docker-compose.yml"))

    def extract_all_files_in_microservices(self):
        '''Extract all files in the microservices'''
        self._extraction_handler.handle_microservice_extraction(self._data_handler)
