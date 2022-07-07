from xml.etree import ElementTree

from model.file_extraction import FileExtraction

# POM_FILE=r"C:\Users\Alex\Documents\Informatik\Bachelorarbeit\spring-netflix-oss-microservices-master/pom.xml" # replace your path
# namespaces = {'xmlns' : 'http://maven.apache.org/POM/4.0.0'}

# # tree = ElementTree.parse(POM_FILE)
# # root = tree.getroot()
# # print(root)
# # for profile in root.findall('//xlmns:project',namespaces):
# #     name  = profile.find('xmlns:artifactId', namespaces).text
# #     print(name)

# namespaces = {'xmlns' : 'http://maven.apache.org/POM/4.0.0'}
# tree = ElementTree.parse(r"C:\Users\Alex\Documents\Informatik\Bachelorarbeit\spring-netflix-oss-microservices-master\card-service/pom.xml")
# # map = {}
# # nsmap = {'m': 'http://maven.apache.org/POM/4.0.0'}
# root = tree.getroot()
# # dependencies = root.findall(".//xmlns:dependency", namespaces=namespaces )  #".//xmlns:dependency", namespaces=namespaces)
# # print(dependencies)

# for element in root.iter(tag="{http://maven.apache.org/POM/4.0.0}dependency"):
#     print(element.find("{http://maven.apache.org/POM/4.0.0}groupId").text)
#     print(element.find("{http://maven.apache.org/POM/4.0.0}artifactId").text)
#     # print(element.text)

# for element in pom.iter():
#     print(element)
# deps = root.findall(".//xmlns:dependency", namespaces=namespaces)
# for d in deps:
#     artifactId = d.find("xmlns:artifactId", namespaces=namespaces)
#     version    = d.find("xmlns:version", namespaces=namespaces)
#     print(artifactId.text + '\t' + version.text)


# from xml.etree import ElementTree

class PomExtractor():
    def __init__(self) -> None:
        pass

    def extract_pom(self, path):
        '''Extract pom file'''
        dict_ = {}
        try:
            tree = ElementTree.parse(path/"pom.xml")
            root = tree.getroot()

            for element in root.iter(tag="{http://maven.apache.org/POM/4.0.0}dependency"):
                groupId = element.find("{http://maven.apache.org/POM/4.0.0}groupId").text
                artifactId = element.find("{http://maven.apache.org/POM/4.0.0}artifactId").text
                dict_[groupId] = artifactId
            return FileExtraction(str(path/"pom.xml"),dict_) 
        except:
            return None