

from model.file_extraction import FileExtraction


class ScriptExtractor():

    def read_script(self,path):
        '''Extract script file'''
        try:
            with open(path) as f:
                x = f.read()
                return FileExtraction(str(path),x)
        except:
            return None
