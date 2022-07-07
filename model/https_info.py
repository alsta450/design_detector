

class HttpsInfo():
    '''Information about https'''
    def __init__(self) -> None:
        self._nginx_info = {}
        self._cert_alg = {}
        self._issuer = {}
        self._yaml_info = {}
        self._cert_manager = {}
