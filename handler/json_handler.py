import json

from handler.data_handler import DataHandler


class JsonHandler():
    def __init__(self,datahandler) -> None:
        self.output_dict: dict = dict()
        self.datahandler: DataHandler = datahandler

    
    def create_json(self,datahandler: DataHandler):
        '''
        Create the final output json
        Additional info can be added here
        '''
        self.add_api_info(datahandler)
        self.create_database_info(datahandler)
        self.create_https_info(datahandler)
        self.save_as_json()


    # API Info
    def add_api_info(self,datahandler: DataHandler):
        '''Add the information for api gateway and related security decisions'''
        # Add info if there is an API Gateway
        api_info ={"API":"No API Gateway found"}
        nginx_root = self.create_nginx_info_architecture_string(datahandler)
        nginx_ms = self.create_api_info_microservice_string(datahandler)
        has_entry = False
        if (bool(nginx_root)):
            api_info["API"] = nginx_root
            has_entry = True
        
        if(has_entry and bool(nginx_ms)):
            api_info["API"].update(nginx_ms)
            has_entry = True
        elif bool(nginx_ms):
            api_info["API"]=nginx_ms
            has_entry = True

        if has_entry:
            api_info["API"].update(self.create_logging_info_string(datahandler))
            api_info["API"].update(self.create_port_info(datahandler))
        self.output_dict.update(api_info)


    def create_port_info(self,datahandler:DataHandler):
        '''Create port info'''
        port_info = {}
        if bool(datahandler.root_instance._output_info._api_info.port_info):
            port_info["Exposed Ports"]=datahandler.root_instance._output_info._api_info.port_info
        else:
            port_info["Exposed Ports"] = "No exposed ports found"

        return port_info

    def create_logging_info_string(self,datahandler: DataHandler):
        '''Create logging info'''
        logging_info = {}
        for microservice in datahandler._component_instances:
            if bool(microservice._output_info._api_info._logging_info):
                logging_info["Logging"] = {microservice._name: microservice._output_info._api_info._logging_info}
        if not bool(logging_info):
            logging_info["Logging"] = "There was no logging info found, but logger should at least report failed login attempts"
        return logging_info


    def create_nginx_info_architecture_string(self,datahandler:DataHandler):
        '''Create nginx info'''
        nginx_root = {}
        if (bool(datahandler.root_instance._output_info._api_info.nginx_proxy)):
            nginx_root["API_Gateway"] = {"Setup": datahandler.root_instance._output_info._api_info.nginx_proxy}

        return nginx_root


    def create_api_info_microservice_string(self,datahandler:DataHandler):
        '''Create api info'''
        nginx_ms = {}
        for microservice in datahandler._component_instances:
            if bool(microservice._output_info._api_info._used_services):
                if "API_Gateway" in nginx_ms.keys():
                    nginx_ms["API_Gateway"].update({"Setup in " + microservice._name + ": ":microservice._output_info._api_info._used_services})
                else:
                    nginx_ms["API_Gateway"] = {"Setup in " + microservice._name + ": ":microservice._output_info._api_info._used_services}

        return nginx_ms



    # Database
    def create_database_info(self,datahandler: DataHandler):
        '''Add the information for the database best practice and connected security decisions'''
        json = {"Database": "No database found"}
        
        databases = self.get_db_connection_string(datahandler)
        if (bool(databases)):
            json["Database"] = databases
            backup = self.get_db_backup_string(datahandler)
            json.update(backup)
        
            encryption = self.get_db_encryption_string(datahandler)
            json.update(encryption)

        self.output_dict.update(json)
        
    def get_db_connection_string(self, datahandler: DataHandler):
        '''add connection between microservice and databases'''
        json = {}
        for microservice in datahandler._component_instances:
            if bool(microservice._output_info._database_info._database_connections):
                if "Connections" in json.keys():
                    json["Connections"].update({"Database connected to " + microservice._name : microservice._output_info._database_info._database_connections} )
                else:
                    json["Connections"] = {"Database connected to " + microservice._name : microservice._output_info._database_info._database_connections} 
                # string += "Found connected dbs in " +microservice._name + " " + str(microservice._output_info._database_info._database_connections) + "\n"
        return json

    def get_db_backup_string(self, datahandler: DataHandler):
        '''Add database backup info'''
        json = {}
        for microservice in datahandler._component_instances:
            if bool(microservice._output_info._database_info._backup_info):
                if "Backup" in json.keys():
                    json["Backup"].update({"Found possible backup instruction in " +microservice._name:microservice._output_info._database_info._backup_info})
                else:
                    json["Backup"] = {"Found possible backup instruction in " +microservice._name:microservice._output_info._database_info._backup_info}

        if not bool(json):
            json["Backup"] = "There was no backup information found"

        return json


    def get_db_encryption_string(self, datahandler: DataHandler):
        '''Add database encryption info'''
        json = {}
        for microservice in datahandler._component_instances:
            if bool(microservice._output_info._database_info._encryption_info):
                if bool(json):
                    json["Encryption"].update({"Found encryption instruction or libraries in " +microservice._name: microservice._output_info._database_info._encryption_info})
                else:
                    json["Encryption"] = {"Found encryption instruction or libraries in " +microservice._name: microservice._output_info._database_info._encryption_info}

        if not bool(json):
            json["Encryption"] = "There was no encryption information found"
        return json



    # HTTPS
    def create_https_info(self,datahandler: DataHandler):
        '''Add https info and connected security decisions'''
        json = {"HTTPS":"No https setup found"}

        https = self.get_https_setup_string(datahandler)
        if bool(https):
            json["HTTPS"] = https
            json["HTTPS"].update(self.get_https_cert(datahandler))
            json["HTTPS"].update(self.get_cert_manager(datahandler))


        self.output_dict.update(json)


    def get_cert_manager(self,datahandler:DataHandler):
        '''Add certificate manager info'''
        json = {}
        if bool(datahandler.root_instance._output_info._https_info._cert_manager):
            json["Cert_manager"] = datahandler.root_instance._output_info._https_info._cert_manager
        else:
            json["Cert_manager"] = "There was no certification manager found"
        return json


    def get_https_setup_string(self,datahandler: DataHandler):
        '''Add https info'''
        json = {}
        for microservice in datahandler._component_instances:
            if bool(microservice._output_info._https_info._yaml_info):
                if bool(json):
                    json["Setup"].update({"Found https setup for server: " + microservice._name: microservice._output_info._https_info._yaml_info})
                else:
                    json["Setup"] = {"Found https setup for server: " + microservice._name: microservice._output_info._https_info._yaml_info}
            if bool(microservice._output_info._https_info._nginx_info):

                if bool(json):
                    json["Setup"].update({"Found https setup in " + microservice._name:microservice._output_info._https_info._nginx_info})
                else:
                    json["Setup"] = {"Found https setup in " + microservice._name:microservice._output_info._https_info._nginx_info}
        return json


    def get_https_cert(self,datahandler:DataHandler):
        '''Add certificate info'''
        json = {}
        if bool(datahandler.root_instance._output_info._https_info._cert_alg):
            json["Certificate"] = datahandler.root_instance._output_info._https_info._cert_alg
        else:
            json["Certificate"] = "There was no certificate found"
        return json
        

    # Save json
    def save_as_json(self):
        '''Write the json to microservice'''
        with open(self.datahandler.root_instance.root/'output.json', 'w') as fp:
            json.dump(self.output_dict, fp)