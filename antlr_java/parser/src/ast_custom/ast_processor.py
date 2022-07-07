from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr_java.grammar.JavaLexer import JavaLexer

from antlr_java.grammar.JavaParser import JavaParser
from antlr_java.parser.src.ast_custom.basic_info_listener import BasicInfoListener

#  Source of this file is https://linuxtut.com/en/6e717f5f7e14f09c4007/

class AstProcessor:

    def __init__(self, logging, listener):
        self.logging = logging
        self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener


    def execute(self, input_source):
        parser = JavaParser(CommonTokenStream(JavaLexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        info =  self.listener.ast_info
        self.clear()
        return info

    def clear(self):
        self.listener =  BasicInfoListener()