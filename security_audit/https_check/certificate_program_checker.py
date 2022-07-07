

from handler.data_handler import DataHandler


class CertificateProgramChecker():
    
    def search_cert_manager(self,datahandler: DataHandler):
        for service in datahandler.root_instance._dockerfile["service"]:
            if "image" in service:
                if "cert-manager" in service["image"]:
                    #TODO
                    datahandler._info_handler.add_certification_management_info({"Certification manager found: ":service["image"],"path":str(datahandler.root_instance.root)+"docker-compose.yml"})
