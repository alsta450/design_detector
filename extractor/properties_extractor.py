from jproperties import Properties

from logger import LoggerGenerator
from model.file_extraction import FileExtraction

class PropertiesExtractor():
    def __init__(self) -> None:
        self.logger = LoggerGenerator(__class__.__name__).get_logger()

    def extract_properties_file(self,path):
        '''Extract properties file'''
        configs = Properties()
        with open(path, 'rb') as config_file:
            try:
                configs.load(config_file)
                return  FileExtraction(str(path),configs.properties)
            except:
                self.logger.error("No such file found %s", path)