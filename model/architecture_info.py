from model.output_info import OutputInfo


class ArchitectureInfo():
    '''Information in root folder'''
    def __init__(self) -> None:
        #Tree structure of folders
        self._structure = None
        #Docker compose file
        self._dockerfile = None
        #Path to the root 
        self.root = None
        #Dict for plotting the structure
        self._diagram_dict: dict = None
        #.env file
        self._env_file = None
        #travis.yaml file
        self._travis_file = None
        #Pom
        self._pom = None 

        self._pem = None
        
        self._output_info: OutputInfo = OutputInfo("root")

