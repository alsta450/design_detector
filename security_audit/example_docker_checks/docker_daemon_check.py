

class DockerDaemonCheck():

    def __init__(self) -> None:
        pass

    def check_if_docker_daemon_exposed(self, docker_compose):
        for element in docker_compose["services"]:
            if "volumes" in docker_compose["services"][element]:
                for ele in docker_compose["services"][element]["volumes"]:
                    if '/var/run/docker.sock' in ele:

                        print("Exposed docker daemon in service " +element +": "+str(docker_compose["services"][element]["volumes"]))
