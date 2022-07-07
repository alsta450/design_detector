from extractor.nginx_extractor import NginxExtractor
from extractor.pem_extractor import PemExtractor
from extractor.properties_extractor import PropertiesExtractor
from extractor.script_extractor import ScriptExtractor
from extractor.yaml_extractor import YamlExtractor
from handler.data_handler import DataHandler
from logger import LoggerGenerator
from model.file_extraction import FileExtraction
from traverser.path_traverser import PathTraverser
from treelib import Tree
import uuid


from dockerfile_parse import DockerfileParser

from extractor.dockerfile_extractor import DockerfileExtractor
from model.component_info import ComponentInfo

from extractor.java_extractor import JavaExtractor
from extractor.pom_extractor import PomExtractor

class ExtractionHandler():
    def __init__(self, root) -> None:
        self._root = root
        self._path_traverser = PathTraverser()
        self._dockerfile_extractor = DockerfileExtractor()
        self._java_extractor = JavaExtractor()
        self._pom_extractor = PomExtractor()
        self._yaml_extractor = YamlExtractor()
        self._script_extractor = ScriptExtractor()
        self._properties_extractor = PropertiesExtractor()
        self._nginx_extractor = NginxExtractor()
        self._pem_extractor = PemExtractor()
        self.logger = LoggerGenerator(__class__.__name__).get_logger()

    def find_file(self,path,filename):
        '''Search for a specific file'''
        self.logger.debug("Searching for file...")
        return self._path_traverser.find_file(path,filename)

    def extract_pom(self,path=None):
        '''Extract pom file'''
        self.logger.debug("Extracting pom...")
        if path == None:
            path = self._root
        return self._pom_extractor.extract_pom(path)

    def find_all_docker_root(self):
        '''Search folder with docker-compose file'''
        self.logger.debug("Search for the folder with docker-compose file...")
        _list =[]
        self._path_traverser.find_all_docker_root(self._root,_list)
        return _list

    def extract_dockerfile(self,component: ComponentInfo) -> DockerfileParser:
        '''Extract docker file'''
        self.logger.debug("Extract dockerfile...")
        return self._dockerfile_extractor.extract_dockerfile(component._root)

    
    def create_diagram_dict(self,dockerfile):
        '''extract diagram dict'''
        self.logger.debug("Get diagram dict from docker-compose...")
        return self._dockerfile_extractor.get_connections_from_docker_compose(dockerfile)    



    def find_all_java_files(self, path):
        '''Search all java files'''
        self.logger.debug("Find all java_files...")
        _list = []
        self._path_traverser.get_all_java_files(path,_list)
        return _list

    def extract_java_file(self,path):
        '''Extract java file'''
        self.logger.debug("Extract java_file...")
        return self._java_extractor.extract_java_file(path)

    def build_tree(self,path):
        '''Build folder tree'''
        self.logger.debug("Build path tree...")
        tree = Tree()
        id = str(uuid.uuid4())
        print(path)
        tree.create_node(str(path.name),id)
        self._path_traverser.get_folder_tree(path,tree,id)
        return tree


    def extract_file(self,name="docker-compose.yml",path=None):
        '''Extract docker-compose file'''
        self.logger.debug("Extract file...")
        if path == None:
            path = self._root
        return self._dockerfile_extractor.extract_docker_compose(path,name)




    def handle_microservice_extraction(self,datahandler):
        '''
        Handle the extraction of all files in microservices
        Additional file extractions need to be added here
        '''
        self.logger.debug("Handle architecture extraction...")
        for element in datahandler._component_instances:
            #Docker files
            dockerfile =self.extract_dockerfile(element)
            #Pom files
            pom = self.extract_pom(element._root)
            # Java files
            java_file_list = {}
            java_files_path = self.find_all_java_files(element._root)
            for java_file in java_files_path:
                java_file_list[java_file.name] = FileExtraction(str(java_file),self.extract_java_file(java_file)) 
            # Yaml files
            yaml_file_list = {}
            yaml_files_path = self.find_all_yaml_files(element._root)
            for yaml_file in yaml_files_path:
                extraction = self._yaml_extractor.extract_yaml_file(yaml_file)
                if extraction != None:
                    yaml_file_list[yaml_file.name] =  extraction

            # sh files
            script_file_list = {}
            script_file_path = self.find_all_script_files(element._root)
            for script_file in script_file_path:
                script_file_list[script_file.name] = self._script_extractor.read_script(script_file)

            # .properties
            properties_file_dict = {}
            properties_files_path = self.find_all_properties_files(element._root)
            for properties_file in properties_files_path:
                properties_file_dict[properties_file.name] = self._properties_extractor.extract_properties_file(properties_file)


            # nginx
            nginx_file_dict = {}
            nginx_files_path = self.find_all_nginx_files(element._root)
            for nginx_file in nginx_files_path:
                nginx_file_dict[nginx_file.name] = self._nginx_extractor.extract_nginx_file(nginx_file)

            # Add files 
            datahandler.add_nginx_file(nginx_file_dict,element)
            datahandler.add_properties_file(properties_file_dict,element)
            datahandler.add_pom(pom,element)
            datahandler.add_dockerfile(element,dockerfile)
            datahandler.add_java_extraction(element, java_file_list)
            datahandler.add_yaml_files(element,yaml_file_list)
            datahandler.add_script_files(element,script_file_list)
        
    
    def find_all_properties_files(self,root):
        '''Find all properties files'''
        self.logger.debug("Find all .yaml files...")
        list_ = []
        self._path_traverser.get_all_java_files(root,list_,".properties")
        return list_

    def extract_pem_files(self):
        '''Extract all pem files'''
        self.logger.debug("Extract all .pem files...")
        list_ = self._path_traverser.get_all_pem_files_in_root(self._root)
        return_list = []
        for element in list_:
            el = self._pem_extractor.extract_pem_file(element)
            if(el != None):

                return_list.append(el)
        # print(return_dict)
        return return_list


    def find_all_nginx_files(self,root):
        '''Find all nginx files'''
        self.logger.debug("Find all .nginx files...")
        list_ = []
        self._path_traverser.get_all_java_files(root,list_,".conf")
        return list_

    def find_all_yaml_files(self,root):
        '''Find all yaml files'''
        self.logger.debug("Find all .yaml files...")
        list_ = []
        self._path_traverser.get_all_java_files(root,list_,".yml")
        return list_

    def find_all_script_files(self,root):
        '''Find all script files'''
        self.logger.debug("Find all .sh files...")
        list_ = []
        self._path_traverser.get_all_java_files(root,list_,".sh")
        return list_


    def extract_all_files_in_root(self, datahandler: DataHandler):
        '''Handle extraction in root folder'''
        datahandler.add_docker_compose(self.extract_file())
        self.logger.info("Adding all .env files from root...")
        datahandler.add_env_file(self.extract_file(".env"))
        self.logger.info("Adding all .travis files from root...")
        datahandler.add_travis_file(self.extract_file(".travis.yml"))
        self.logger.info("Adding all .pom files from root...")
        datahandler.add_pom(self.extract_pom())
        self.logger.info("Adding all .pem files from root...")
        datahandler.add_pem_file(self.extract_pem_files())