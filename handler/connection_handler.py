




from handler.data_handler import DataHandler
from logger import LoggerGenerator


class ConnectionHandler():
    def __init__(self,datahandler) -> None:
        self._datahandler: DataHandler = datahandler
        self.logger = LoggerGenerator(__class__.__name__).get_logger()
    
    def connect_microservices(self):
        '''Find connections between microservices and databases'''
        try:
            docker_compose = self._datahandler.root_instance._dockerfile.extraction
            return_dict = {}
            for element in docker_compose['services']:
                if(element not in return_dict):
                    return_dict[element] = {"type": "Docker('"+str(element)+"',id='" +str(element) +"')"   ,"connections":set()}
                if( "depends_on" in docker_compose["services"][element]):

                    for el in docker_compose["services"][element]['depends_on']:
                        return_dict[element]["connections"].add(el.replace("-","_"))
                if( "links" in docker_compose["services"][element]):

                    for el in docker_compose["services"][element]['links']:
                        return_dict[element]["connections"].add(el.replace("-","_"))
            

            for microservice in self._datahandler._component_instances:
                for connection in microservice._output_info._database_info._database_connections.keys():
                    return_dict[microservice._name]["connections"].add(connection.replace("-","_"))
            new_dict = { k.replace('-', '_'): v for k, v in return_dict.items() }

            return new_dict
        except:
            self.logger.error("Error Creating Architecture Overview dict")

            return None
