import json
import os
import sys
import time
import threading

class crd:

    def __init__(self):
    #preparation of file and its access

        #initiating file access variables
        file_path = os.getcwd()
        self.filepath = file_path + '/crd.json'
        self.filelock = threading.Lock()
        self.datalock = threading.Lock()


        #acessing file data if file already created
        try:
            file = open(self.filepath, 'r')
            filedata = json.load(file)
            self.data = filedata
            file.close()

            if not self.check_file_size():
                raise Exception('Size of the file storing data exceeded permitted 1GB')


        #creating new file if file is not created previously
        except:

            file = open(self.filepath, 'w')
            self.data = {}
            self.ttldict = {}
            file.close()
