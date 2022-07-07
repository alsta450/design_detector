import glob
from pathlib import Path
import logging.config
from dockerfile_parse import DockerfileParser
from treelib import Node, Tree
import uuid
class PathTraverser():
    def __init__(self) -> None:
        pass

    def find_file(self,path: Path,file: str):

        for element in path.iterdir():

            if file == "docker-compose.yml":
                if element.name == file or element.name == "docker-compose.yaml":
                    return path
                if(element.is_dir()):
                    x= self.find_file(path/element.name,file) 
                    if x != None: return x 
            else:
                if element.name == file:
                    return path
                if(element.is_dir()):
                    x= self.find_file(path/element.name,file) 
                    if x != None: return x 


    def find_all_docker_root(self,path: Path, dockerfile_list: list):
        _list = []
        for element in path.iterdir():
            if element.name == "Dockerfile" or element.name == "DockerFile":   
                dockerfile_list.append(path)
            if(element.is_dir()):
                _list.append(element)
        for element in _list:
            self.find_all_docker_root(path/element.name,dockerfile_list)



    def get_all_directories_in_path(self,path: Path):
        _list = []
        for element in path.iterdir():
            if(element.is_dir()):
                _list.append(element)
        return _list



    def get_folder_tree(self,path: Path,tree: Tree,id):
        temp_list = []
        for element in path.iterdir():
            if(element.is_dir()):
                temp_list.append(element)
            else:
                id_ = str(uuid.uuid4())
                tree.create_node(str(element.name),id_, parent=id)
        for element in temp_list:
            id_ = str(uuid.uuid4())
            tree.create_node(str(element.name),id_, parent=id)
            self.get_folder_tree(path /element, tree,id_)

    def get_all_java_files(self,path,_list,file_type=".java"):
        for element in path.iterdir():
            if(element.suffix == file_type):
                _list.append(element)
            elif(element.is_dir() and element.name != "test" ):
                self.get_all_java_files(path/element,_list,file_type)


    def get_all_pem_files_in_root(self, path):
        return_list = []
        for element in path.iterdir():
            if(element.suffix == ".pem"):
                return_list.append(element)

        return return_list 