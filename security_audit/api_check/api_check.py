



from security_audit.api_check.port_finder import PortFinder
from security_audit.api_check.security_logger_checker import SecurityLoggerChecker

class ApiSecurityCheck():
    def __init__(self) -> None:
        self._security_logger_checker = SecurityLoggerChecker()
        self._port_finder = PortFinder()

    def run_api_security_check(self,datahandler):
        self._security_logger_checker.search_for_logging_enabled(datahandler)
        self._port_finder.find_exposed_ports(datahandler)
    