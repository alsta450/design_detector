
from OpenSSL import crypto
from logger import LoggerGenerator
from model.file_extraction import FileExtraction
class PemExtractor():
    def __init__(self) -> None:
        self.logger = LoggerGenerator(__class__.__name__).get_logger()


    def extract_pem_file(self,path):
        '''Extract pem file'''
        try:
            with open(path, "r") as pem_file:
                cert = crypto.load_certificate(crypto.FILETYPE_PEM, pem_file.read())
                return FileExtraction(path,cert)
        except:
            self.logger.error("No such file found %s", path)

