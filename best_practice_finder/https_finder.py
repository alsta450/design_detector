

from handler.data_handler import DataHandler


class HttpsFinder():
    def __init__(self) -> None:
        self.nginx_list = ["ssl","ssl_certificate","ssl_certificate_key","listen","ssl_protocols","ssl_ciphers","rewrite"]


    def find_https_setup(self,datahandler):
        self.find_https_in_yaml(datahandler)
        self.find_https_in_nginx(datahandler)

    # def find_https_in_docker_compose(self,datahandler:DataHandler):
    #     for service in datahandler.root_instance._dockerfile.extraction["services"]:
    #         if "environment" in datahandler.root_instance._dockerfile.extraction["services"][service]:
    #             for element in datahandler.root_instance._dockerfile.extraction["services"][service]["environment"]:
    #                 if "https" in element:
    #                     print("found https in " + service + " " + element)

    def find_https_in_yaml(self,datahandler:DataHandler):
        for microservice in datahandler._component_instances:
            for yaml_file in microservice.yaml_files:
                for dict_ in microservice.yaml_files[yaml_file].extraction:
                    path = self.__getpath(dict_,"https://")
                    if(path != None):
                        result = dict_
                        for element in path:
                            result = result[element]
                        datahandler._info_handler.add_yaml_https_info({yaml_file:result,"path":microservice.yaml_files[yaml_file].path},microservice)

    # def find_https_in_properties(self,datahandler:DataHandler):
    #     for microservice in datahandler._component_instances:
    #         for properties_file in microservice._properties_file:
    #             print(properties_file)

    def find_https_in_nginx(self,datahandler: DataHandler):
        for microservice in datahandler._component_instances:
            for key in microservice._nginx_file:
                result = []
                if microservice._nginx_file[key] != None:
                    for nested_list in microservice._nginx_file[key].extraction:
                        
                        self.__iterate_nested_list(nested_list,self.nginx_list,result)

                    datahandler._info_handler.add_nginx_https_info({key:result,"path":microservice._nginx_file[key].path},microservice)



    # Credit for this function goes to https://stackoverflow.com/questions/22162321/search-for-a-value-in-a-nested-dictionary-python
    def __getpath(self, nested_dict, value, prepath=()):
        try:
            for k, v in nested_dict.items():
                path = prepath + (k,)
                if type(v) == str:
                    if value in v:
                        return path
                elif type(v) == dict:
                    p = self.__getpath(v, value, path)
                    if p is not None:
                        return p
        except:
            return None

    
    def __iterate_nested_list(self,nested_list,value,return_list):
        for element in nested_list:
            if type(element) != str:
                if element[0] != "#":
                    self.__iterate_nested_list(element,value,return_list)
                if any(x in element[0] for x in value):
                    if(type(element[0]) == str):
                        return_list.append(element)