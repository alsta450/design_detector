import yaml

from logger import LoggerGenerator
from model.file_extraction import FileExtraction
class YamlExtractor():
    def __init__(self) -> None:
        self.logger = LoggerGenerator(__class__.__name__).get_logger()


    def extract_yaml_file(self,path):
        '''Extract yaml file'''
        return_list = []
        try:
            with open(path, 'r') as file:
                yaml_file = yaml.safe_load_all(file)
                for element in yaml_file:
                    return_list.append(element)
        except:
            self.logger.error("No such file found %s", path)
        if bool(return_list):
            return FileExtraction(str(path),return_list)
        else:
            return None