from dockerfile_parse import DockerfileParser
from model.output_info import OutputInfo

class ComponentInfo():
    def __init__(self,root,name) -> None:
        self._structure = None
        self._dockerfile: DockerfileParser= None
        self._extracted_classes= {}
        self._root = root
        self._pom = None
        self._name = name
        self.yaml_files = {}
        self._script_files = {}
        self._properties_file= {}
        self._nginx_file = {}
        self._output_info: OutputInfo= OutputInfo(name) 