
from lxml import etree
from handler.data_handler import DataHandler

from logger import LoggerGenerator

class SvgHandler():
    def __init__(self) -> None:

        self.logger = LoggerGenerator(__class__.__name__).get_logger()



    def load_svg(self,filepath):
        '''Load the architecture diagram'''
        try:
            svg = etree.parse(filepath)
            return svg
        except:
            self.logger.error("Failed to load svg")
    def add_paths_to_picture(self,datahandler: DataHandler,filepath):
        '''Add links to architecture diagrams'''
        try:
            svg = self.load_svg(filepath)

            for element in svg.iter():
                if "id" in element.attrib:
                    for microservice in datahandler._component_instances:
                        if element.attrib["id"] == microservice._name:
                                element_to_add = etree.Element('a',attrib={"href":str(microservice._root)})
                                element_to_add.extend(element)
                                element.append(element_to_add)

            svg.write('container_view.svg', pretty_print=True)

        except Exception as e:
            self.logger.error(e)




