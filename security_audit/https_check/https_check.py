

from security_audit.https_check.certificate_checker import CertificateChecker
from security_audit.https_check.certificate_program_checker import CertificateProgramChecker


class HttpsCheck():
    def __init__(self) -> None:
        self.certificate_checker = CertificateChecker()
        self.certificate_program_checker = CertificateProgramChecker()


    def run_https_check(self,datahandler):
        self.certificate_checker.search_for_certificates(datahandler)
