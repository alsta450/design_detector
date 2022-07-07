from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from handler.svg_handler import SvgHandler
import os
from diagrams.onprem.container import Docker
from diagrams.programming.flowchart import Database
from logger import LoggerGenerator

class DiagramHandler():
    def __init__(self,datahandler) -> None:
        self.logger = LoggerGenerator(__class__.__name__).get_logger()
        self.svg_handler = SvgHandler()
        self._datahandler = datahandler

    def create_object(self, dict_):
        self.logger.debug("Creating diagram from diagram dict...")
        s = ""

        for element in dict_.keys():
            s +="   "+ element + "=" + dict_[element]["type"] + "\n"

        for element in dict_.keys():
            s +="   "+ element
            s += " >> [" 
            first = True
            for el in dict_[element]["connections"]:
                if(first):
                    first = False
                    s += str(el)
                else:
                    s += "," + str(el)
            
            s+= "]\n"
        exec('''with Diagram("./static/container_view", show=False, direction="TB",outformat="png"):\n''' + s)
        exec('''with Diagram("container_view_pre_rework", show=False, direction="TB",outformat="svg"):\n''' + s)
        self.svg_handler.add_paths_to_picture(self._datahandler,os.curdir + "/container_view_pre_rework.svg")

