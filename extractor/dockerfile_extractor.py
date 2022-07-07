from dockerfile_parse import DockerfileParser
import yaml

from logger import LoggerGenerator
from model.file_extraction import FileExtraction
class DockerfileExtractor():
    def __init__(self) -> None:
        self.logger = LoggerGenerator(__class__.__name__).get_logger()

    def extract_dockerfile(self,path):
        '''Extract Dockerfile'''
        return FileExtraction(path/"Dockerfile", DockerfileParser(str(path/"Dockerfile")))

    def extract_docker_compose(self,path,name = "docker-compose.yml"):
        '''Extract docker-compose.yaml file'''
        try:
            with open(path / name, 'r') as file:
                yaml_file = yaml.safe_load(file)
                return FileExtraction( str(path/name), yaml_file)
        except:
            self.logger.error("No such file found: %s", name)
            if name == "docker-compose.yml":
                self.logger.error("Trying: %s", "docker-compose.yaml")
                try:
                    with open(path / "docker-compose.yaml", 'r') as file:
                        yaml_file = yaml.safe_load(file)
                        return FileExtraction( str(path/name), yaml_file)
                except:
                    self.logger.error("No such file found: %s", "docker-compose.yaml")
            return None



 