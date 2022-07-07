
from logger import LoggerGenerator
from security_audit.api_check.api_check import ApiSecurityCheck
from security_audit.database_check.database_audit import DatabaseAudit
import logging

from security_audit.https_check.https_check import HttpsCheck


class SecurityHandler():
    def __init__(self) -> None:
        self._database_security = DatabaseAudit()
        self._api_checker = ApiSecurityCheck()
        self._https_checker = HttpsCheck()
        self.logger = LoggerGenerator(__class__.__name__).get_logger()



    def do_audit(self,datahandler):
        '''
        Conduct the security audit
        Additional audits can be added here
        '''
        self._api_checker.run_api_security_check(datahandler)
        self._database_security.run_database_security_check(datahandler)##
        self._https_checker.run_https_check(datahandler)

    


        
    
