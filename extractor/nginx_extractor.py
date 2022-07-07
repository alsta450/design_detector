from nginxparser_eb import load
from logger import LoggerGenerator
from model.file_extraction import FileExtraction


class NginxExtractor():
    def __init__(self) -> None:
        self.logger = LoggerGenerator(__class__.__name__).get_logger()

    def extract_nginx_file(self,path):
        '''Extract nginx file'''
        try:
            file = load(open(path))
            return FileExtraction(str(path), list(file))
        except:
            self.logger.error("No such file found %s", path)
