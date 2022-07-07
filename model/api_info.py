

class ApiInfo():
    '''Information about api gateway'''
    def __init__(self) -> None:
        self.nginx_proxy = {}
        self._used_services = {}
        self._logging_info = {}
        self.port_info = {}

    