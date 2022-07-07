from dockerfile_parse import DockerfileParser
class UnprivilegedUserCheck():
    def __init__(self) -> None:
        pass


    def check_unprivileged_user(self, docker: DockerfileParser):
        user_found = False
        for element in docker.structure:
            if element['instruction'] == "USER":
                print("A user profile is used")
                user_found = True
                break
        if(user_found != True):
            print("No custom user profile was found")

