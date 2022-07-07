

import logging

from antlr_java.parser.src.ast_custom.ast_processor import AstProcessor
from antlr_java.parser.src.ast_custom.basic_info_listener import BasicInfoListener



class JavaExtractor():
    def __init__(self) -> None:
        self.ast_processor = AstProcessor(logging, BasicInfoListener())

    def extract_java_file(self,path):
        '''Extract java file'''
        return self.ast_processor.execute(path)

