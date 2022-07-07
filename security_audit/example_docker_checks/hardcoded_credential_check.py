from dockerfile_parse import DockerfileParser
class HardCodedCrendentialCheck():
    def __init__(self) -> None:
        pass

    def check_docker_compose_for_credentials(self,dockerfile):
        # for element in dockerfile:
        #     print(element)
        # print(dockerfile["services"])
        # pass
        print(self.extract_all_values(dockerfile), "hardcoded password(s) found")


    def extract_all_values(self,dict_:dict):
        counter = 0
        if(type(dict_) == dict):
            for element in dict_.keys():
                if("PASSWORD" in str(element).upper()):
                    if("$" not in dict_[element]): 
                        counter = counter+ 1
                else:
                    counter += self.extract_all_values(dict_[element])
        return counter
