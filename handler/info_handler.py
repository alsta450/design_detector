


from model.component_info import ComponentInfo


class InfoHandler():
    def __init__(self,component_instances, root_instance) -> None:
        self._component_instances: ComponentInfo = component_instances
        self._root_instance = root_instance


    # Https info
    def add_yaml_https_info(self, info,element):
        '''Add https info from extracted yaml files'''
        index = self._component_instances.index(element)
        self._component_instances[index]._output_info._https_info._yaml_info.update(info)

    def add_nginx_https_info(self, info,element):
        '''Add https info from extracted nginx files'''
        index = self._component_instances.index(element)
        self._component_instances[index]._output_info._https_info._nginx_info.update(info)




    # Database info
    def add_database_info(self, info,element):
        '''Add database info from microservices'''
        index = self._component_instances.index(element)
        self._component_instances[index]._output_info._database_info._database_connections.update(info)

    def add_database_info_docker_compose(self,info,element):
        '''Add database info from docker compose extraction'''
        for microservice in self._component_instances:
            print(microservice._name)
            if microservice._name in element:
                microservice._output_info._database_info._database_connections.update(info)



    def add_backup_info(self,info,element):
        '''Add backup info'''
        index = self._component_instances.index(element)
        self._component_instances[index]._output_info._database_info._backup_info.update(info)


    def add_encryption_info(self,info,element):
        '''Add encryption info'''
        index = self._component_instances.index(element)
        self._component_instances[index]._output_info._database_info._encryption_info.update(info)

    # API info
    def add_used_services_info(self, info,element):
        '''Add api info'''
        index = self._component_instances.index(element)
        self._component_instances[index]._output_info._api_info._used_services.update(info)


    def add_logger_info(self,info,element):
        '''Add logger info'''
        index = self._component_instances.index(element)
        self._component_instances[index]._output_info._api_info._logging_info.update(info)

    def add_port_info(self,info):
        '''Add port info'''
        self._root_instance._output_info._api_info.port_info.update(info)



    # Root info
    def add_nginx_api_info(self, info):
        '''Add nginx api info to root'''
        self._root_instance._output_info._api_info.nginx_proxy.update(info)


    def add_certificate_info(self,info):
        '''Add certificate info'''
        self._root_instance._output_info._https_info._cert_alg.update(info)

    def add_issuer_info(self,info):
        '''Add issuer info'''
        self._root_instance._output_info._https_info._issuer.update(info)

    def add_certification_management_info(self,info):
        '''Add certification management info'''
        self._root_instance._output_info._https_info._cert_manager.update(info)
