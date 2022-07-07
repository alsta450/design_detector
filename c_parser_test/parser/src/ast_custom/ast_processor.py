from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from pprint import pformat
from ast_custom.CLexer import CLexer

from ast_custom.CParser import CParser
from ast_custom.basic_info_listener import BasicInfoListener



class AstProcessor:

    def __init__(self, logging, listener):
        self.logging = logging
        self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    #★ Point 2
    def execute(self, input_source):
        parser = CParser(CommonTokenStream(CLexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        info =  self.listener.ast_info
        self.clear()
        return info

    def clear(self):
        self.listener =  BasicInfoListener()