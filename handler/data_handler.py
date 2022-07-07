

from handler.info_handler import InfoHandler
from logger import LoggerGenerator
from model.component_info import ComponentInfo
from model.architecture_info import ArchitectureInfo
from model.file_extraction import FileExtraction


class DataHandler():
    def __init__(self) -> None:
        
        self._component_instances: ComponentInfo = []
        self.root_instance: ArchitectureInfo = ArchitectureInfo()
        self.logger = LoggerGenerator(__class__.__name__).get_logger()
        self._info_handler = InfoHandler(self._component_instances,self.root_instance)


    def add_pem_file(self,pem_files):
        '''Add pem extraction to microservice root'''
        self.logger.debug("Adding .pem file to root...")
        self.root_instance._pem = pem_files

    def add_env_file(self,env_file):
        '''Add env extraction to microservice root'''
        self.logger.debug("Adding .env file to root...")
        self.root_instance._env_file = env_file

    def add_properties_file(self,properties,element):
        '''Add properties extraction to microservice'''
        self.logger.debug("Adding properties files to microservice...")
        index = self._component_instances.index(element)
        self._component_instances[index]._properties_file = properties

    def add_nginx_file(self,nginx_file, element):
        '''Add nginx file extraction to Microservice'''
        self.logger.debug("Adding nginx file to microservice...")
        index = self._component_instances.index(element)
        self._component_instances[index]._nginx_file = nginx_file


    def add_travis_file(self,travis_file):
        '''Add travis extraction to microservice root'''
        self.logger.debug("Adding .travis file to root...")
        self.root_instance._travis_file = travis_file

    def add_componnents(self,_list):
        '''Add microservice instances'''
        self.logger.debug("Adding microservice instances...")
        for element in _list:
            self._component_instances.append(ComponentInfo(element,element.name))

    def add_script_files(self,element,script_files):
        '''Add Script file extraction to microservices'''
        self.logger.debug("Adding script files to microservice...")
        index = self._component_instances.index(element)
        self._component_instances[index]._script_files = script_files

    def add_architecture(self,root):
        '''Add root path'''
        self.logger.debug("Adding root...")
        self.root_instance.root = root

    def add_dockerfile(self,element,dockerfile):
        '''Add dockerfile extraction to microservice'''
        self.logger.debug("Adding dockerfile to microservice...")
        index = self._component_instances.index(element)
        self._component_instances[index]._dockerfile = dockerfile


    def add_docker_compose(self,dockerfile):
        '''Add docker-compose to root'''
        self.logger.debug("Adding docker compose to root...")
        self.root_instance._dockerfile = dockerfile

    def add_java_extraction(self,element,java_extraction):
        '''Add java extraction to microservices'''
        self.logger.debug("Adding extracted java files to microservice...")
        index = self._component_instances.index(element)
        self._component_instances[index]._extracted_classes = java_extraction

    def add_yaml_files(self, element, yaml_files):
        '''Add yaml extraction to microservices'''
        self.logger.debug("Adding extracted yaml files to microservice...")
        index = self._component_instances.index(element)
        self._component_instances[index].yaml_files = yaml_files

    def add_tree(self,tree):
        '''Add folder tree structure to root'''
        self.logger.debug("Adding tree to root...")
        self.root_instance._structure = tree

    def add_pom(self,pom,element=None):
        '''Add pom extraction to root/microservices'''
        self.logger.debug("Adding pom to root/microservice...")
        if element == None:
            self.root_instance._pom = pom
        else:
            index = self._component_instances.index(element)
            self._component_instances[index]._pom = pom

    def add_diagram_dict(self,dict_):
        '''Add a dict of the architecture to a create the architecture diagram'''
        self.logger.debug("Adding diagram dict to root...")
        self.root_instance._diagram_dict = dict_
