

from handler.data_handler import DataHandler


class BackUpCheck():
    def __init__(self) -> None:
        self._back_up_commands = ["mysqldump","backup"]

    def check_database_backup(self,datahandler: DataHandler):
        for microservice in datahandler._component_instances:
            for script_name, script_value in microservice._script_files.items():
                for command in self._back_up_commands:
                    if command in str(script_value).lower():
                        datahandler._info_handler.add_backup_info({script_name:command},microservice)