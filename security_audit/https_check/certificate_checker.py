

class CertificateChecker():
    def __init__(self) -> None:
        pass


    def search_for_certificates(self, datahandler):
        alg_dict = {}
        for pem_file in datahandler.root_instance._pem:
            signature_algorithm = pem_file.extraction.get_signature_algorithm()
            alg_dict.update({str(pem_file.path.name):str(signature_algorithm),"path":str(pem_file.path)})
        datahandler._info_handler.add_certificate_info(alg_dict)


