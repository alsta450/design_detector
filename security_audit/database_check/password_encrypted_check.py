

from handler.data_handler import DataHandler


class PasswordEncryptedCheck():
    def __init__(self) -> None:
        self._password_list = ["password", "pwd", "pass"]
        self._library_list = ["BCryptPasswordEncoder", "MessageDigest",
                              "Hashing", "DigestUtils", "BouncyCastleProvider", "Keccak"]

    # def check_password_encryption(self, component_set):
    #     for component in component_set:
    #         for element in component._extracted_classes:

    #             if any(pwd in str(element).lower() for pwd in self._password_list):
    #                 # print(element)
    #                 for el in element["imports"]:
    #                     for lib in self._library_list:
    #                         if lib in el:
    #                             print(
    #                                 "The following Encryption library was found: " + el)

    def find_encryption_library(self,datahandler: DataHandler):

            for microservice in datahandler._component_instances:
                for key in microservice._extracted_classes:
                        for import_ in microservice._extracted_classes[key].extraction["imports"]:
                            for library in self._library_list:
                                if library in import_:
                                    calls =  []
                                    variable = ""
                                    if "fields" in microservice._extracted_classes[key].extraction:
                                        for fieldType in microservice._extracted_classes[key].extraction["fields"]:
                                            if(fieldType['fieldType'] == library):
                                                variable = fieldType['fieldDefinition'].partition("=")[0]
                                                calls.append(variable)
                                                if "callMethods" in microservice._extracted_classes[key].extraction["methods"][0]:
                                                    for methodCalls in microservice._extracted_classes[key].extraction["methods"][0]["callMethods"]:
                                                        if variable in methodCalls:
                                                            calls.append(methodCalls)
                                    datahandler._info_handler.add_encryption_info({"file":key,library:calls,"path":microservice._extracted_classes[key].path},microservice)



    

