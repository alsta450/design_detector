

from handler.data_handler import DataHandler


class ApiGatewayFinder():
    def __init__(self) -> None:
        self.gateway_annotations = ["EnableZuulProxy"]


    def find_api_gateway(self,datahandler):
        self.search_in_annotations(datahandler)
        self.search_for_nginx(datahandler)






    def search_in_annotations(self,datahandler: DataHandler):
        for microservice in datahandler._component_instances:
            for extracted_class in microservice._extracted_classes:
                for annotation in self.gateway_annotations:
                    if(annotation in microservice._extracted_classes[extracted_class].extraction["annotations"]):
                        datahandler._info_handler.add_used_services_info({extracted_class:annotation,"path":microservice._extracted_classes[extracted_class].path},microservice)


    def search_for_nginx(self,datahandler: DataHandler):
        for service_name in datahandler.root_instance._dockerfile.extraction["services"]:
            if "image" in datahandler.root_instance._dockerfile.extraction["services"][service_name]:
                if("nginx" in datahandler.root_instance._dockerfile.extraction["services"][service_name]["image"]):
                    if("consul" in datahandler.root_instance._dockerfile.extraction["services"][service_name]["image"]):
                        datahandler._info_handler.add_nginx_api_info({service_name:"Found nginx with consul","path":datahandler.root_instance._dockerfile.path})