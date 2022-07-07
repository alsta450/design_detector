

from handler.data_handler import DataHandler


class DatabaseConnector():
    def __init__(self) -> None:
        self.database_strings = ["mysql","mongodb"]


    def connect_database_to_microservices(self,datahandler):
        self.search_yaml_files(datahandler)
        self.search_for_docker_compose_file(datahandler)


    def search_for_docker_compose_file(self,datahandler:DataHandler):
        dockerfile = datahandler.root_instance._dockerfile.extraction
        set_ = set()
        try:
            for element in dockerfile["services"]:
                if("image" in dockerfile["services"][element].keys()):
                    if("mongodb" in dockerfile["services"][element]["image"] or "sql" in dockerfile["services"][element]["image"]):
                        set_.add(element)
            for element in dockerfile["services"]:
                if("depends_on" in dockerfile["services"][element].keys()):
                    for service in dockerfile["services"][element]["depends_on"]:
                        if service in set_:
                            datahandler._info_handler.add_database_info_docker_compose({service:str(datahandler.root_instance.root)+"/docker-compose.yml"},element)
        except:
            for element in dockerfile:
                if("image" in dockerfile[element].keys()):
                    if("mongodb" in dockerfile[element]["image"] or "sql" in dockerfile[element]["image"]):
                        set_.add(element)
            for element in dockerfile:
                if("depends_on" in dockerfile[element].keys()):
                    for service in dockerfile[element]["depends_on"]:
                        if service in set_:
                            datahandler._info_handler.add_database_info_docker_compose({service:str(datahandler.root_instance.root)+"/docker-compose.yml"},element)


    def search_yaml_files(self,datahandler):
        for microservice in datahandler._component_instances:
            for ms in datahandler._component_instances:
                for key in ms.yaml_files.keys():
                    if microservice._name in key:
                        for element in ms.yaml_files[key].extraction:
                            db = self.find_key_in_nested_dict(element,"host")
                            if db != None:
                                datahandler._info_handler.add_database_info({db:ms.yaml_files[key].path},microservice)


    def find_key_in_nested_dict(self,dict_,key_to_find):
        if(type(dict_) == dict):
            if key_to_find in dict_.keys():
                return dict_[key_to_find]
            else: 
                for key in dict_:
                    x = self.find_key_in_nested_dict(dict_[key],key_to_find)
                    if x != None and type(x) == str:
                        return x

