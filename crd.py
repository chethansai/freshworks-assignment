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
            file.close()\


    #verification of entered key to fit to constraints
    def verify_key(self, key):

        # Checking if key is a string and length of it is below 32
        if type(key) == type(""):
            if len(key) > 32:
                raise Exception('Size of key is capped at 32. Entered key length is ' + str(len(key)))
            else:
                return True
        else:
            raise Exception('Entered Key value is not a string. Entered key is of type: ' + str(type(key)))
            return False



    #Checking if the file size is below 1 GB
    def check_file_size(self):

        self.filelock.acquire()

        if os.path.getsize(self.filepath) <= 1e+9:
            self.filelock.release()
            return True
        else:
            self.filelock.release()
            return False

