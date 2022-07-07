import logging.config
from ast_custom.ast_processor import AstProcessor
from ast_custom.basic_info_listener import BasicInfoListener


if __name__ == '__main__':


    target_file_path = r'C:\Users\Alex\Documents\Informatik\Bachelorarbeit\parser_test\parser\src/test.c'

    ast_info = AstProcessor(logging, BasicInfoListener()).execute(target_file_path)
    