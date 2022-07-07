



from handler.data_handler import DataHandler


class SecurityLoggerChecker():
    def __init__(self) -> None:
        self._logging_spring = "org.springframework.security"


    def search_for_logging_enabled(self,datahandler: DataHandler):
        for microservice in datahandler._component_instances:
            for yaml_file in microservice.yaml_files:
                for yaml in microservice.yaml_files[yaml_file].extraction:
                    key = self.__find_key_in_nested_dict(yaml,self._logging_spring)
                    if key != None:
                        datahandler._info_handler.add_logger_info({yaml_file: {self._logging_spring: key,"path":microservice.yaml_files[yaml_file].path}},microservice)

    

    def __find_key_in_nested_dict(self,dict_,key_to_find):
        if(type(dict_) == dict):
            if key_to_find in dict_.keys():
                return dict_[key_to_find]
            else: 
                for key in dict_:
                    x = self.__find_key_in_nested_dict(dict_[key],key_to_find)
                    if x != None and type(x) == str:
                        return x