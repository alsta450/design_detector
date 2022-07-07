# Bachelor Alexander Stadler
### Secure Microservice Deployment Design Extractor and Detector

## Overview
This is my bachelor thesis project. The goal is to support practitioners with design and security, when planning a microservice architecture. To do so, a detector is implemented, which can provide a rough architectural overview of a microservice architecture and detect design and security decisions made. For now, three design decisions and six security decisions can be detected. In the folder filewatcher, a VSCode extension can be found, that displays changes in the information provided by the tool. On how to run or extend the tool, see the next sections.

## How To install and run locally

- To install the tool clone this project
- Install pip and npm, if not already installed
- run pip install yaml nginxparser_eb OpenSSL jproperties diagrams treelib lxml dockerfile_parse
- Eventually the graphviz module which comes with the diagrams package, must be added to the environment variables
- Start the extension by navigating in VSCode to the extension.ts file and press F5
- Run the main.py file either in VSCode or from command line by navigating to the folder containing the main.py file and either run "py main.py" or "python3 main.py" (depends on operating system).
- 
## How to extend the tool

To extend the tool to detect further design and security decisions, first analyse microservice architectures and figure out where and how the information is present. Next write an extractor (if not already present) to extract the file(s) where the information is. This can be easily done by adding an extractor class. Next, in the class ExtractionHandler add a method to call the extractor and add a method call to the method handle_microservice_extraction. Now that the information is extracted, a class to find certain information or pattern needs to be added. For example the detection of a new best practice is implemented in a new class. Next, add a method call for this class to the BestPracticeHandler. Finally add a method to the JsonHandler, to extend the output information.
