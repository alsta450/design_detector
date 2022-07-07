import logging

class LoggerGenerator():
    def __init__(self,name,level=logging.INFO) -> None:
        self.logger=logging.getLogger(name)
        self.logger.setLevel(level)

        # logging_level_list = [logging.INFO, logging.DEBUG,logging.WARNING,logging.CRITICAL,logging.ERROR]

        # for element in logging_level_list:
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

        


    def get_logger(self):
        return self.logger