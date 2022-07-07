
import yaml
from traverser.path_traverser import PathTraverser
from security_audit.database_check.backup_check import BackUpCheck
from security_audit.database_check.password_encrypted_check import PasswordEncryptedCheck


class DatabaseAudit():
    def __init__(self) -> None:
        self._backup_check = BackUpCheck()
        self._password_encryption_check = PasswordEncryptedCheck()


    def run_database_security_check(self,datahandler):
        self._backup_check.check_database_backup(datahandler)
        self._password_encryption_check.find_encryption_library(datahandler)



    # def find_database_connections(self,datahandler):
    #     for microservice in datahandler._component_instances:
    #         for ms in datahandler._component_instances:
    #             for key in ms.yaml_files.keys():
    #                 if microservice._name in key:
                        
    #                     db = self.find_key_in_nested_dict(ms.yaml_files[key],"host")
    #                     if db != None:
    #                         microservice._security_info._database_connections.append(db)


    # def find_key_in_nested_dict(self,dict_,key_to_find):
    #     if(type(dict_) == dict):
    #         if key_to_find in dict_.keys():
    #             return dict_[key_to_find]
    #         else: 
    #             for key in dict_:
    #                 x = self.find_key_in_nested_dict(dict_[key],key_to_find)
    #                 if x != None and type(x) == str:
    #                     return x

        
        
        



