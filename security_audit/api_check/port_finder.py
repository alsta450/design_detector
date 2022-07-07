

from dockerfile_parse import DockerfileParser
import json

from handler.data_handler import DataHandler
class PortFinder():
    def __init__(self) -> None:
        self.port_dict = {}

    def find_exposed_ports(self,datahandler: DataHandler):
        
        self.find_docker_compose_ports(datahandler)
        self.find_docker_ports(datahandler)
        datahandler._info_handler.add_port_info(self.port_dict)

    def find_docker_compose_ports(self,datahandler: DataHandler):
        for service in datahandler.root_instance._dockerfile.extraction["services"]:
            if("EXPOSE" in datahandler.root_instance._dockerfile.extraction["services"][service]):
                for expose in datahandler.root_instance._dockerfile.extraction["services"][service]["EXPOSE"]:
                    self.port_dict.update({service:{"port":expose,"path":str(datahandler.root_instance.root)+"/docker-compose.yml"}})

            if("ports" in datahandler.root_instance._dockerfile.extraction["services"][service]):
                for expose in datahandler.root_instance._dockerfile.extraction["services"][service]["ports"]:
                    self.port_dict.update({service:{"port":expose,"path":str(datahandler.root_instance.root)+"/docker-compose.yml"}})



    def find_docker_ports(self,datahandler):
        for microservice in datahandler._component_instances:
            dockerfile: DockerfileParser = microservice._dockerfile.extraction
            for element in json.loads(dockerfile.json):
                for key in element.keys():
                    if "EXPOSE" in key:
                        self.port_dict.update({microservice._name:{"port":element[key],"path":str(microservice._root)+"/dockerfile"}})