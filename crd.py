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

        # Creating and storing given Key, Value & optional Time-To-Live into file

    def create(self, key='', value='', ttl=None):

        # Checking if key is bounding to constraints
        self.verify_key(key)

        # Trigger for submission without entering key
        if key == '':
            raise Exception('No key was entered. Please enter the key.')

        # Assigning value as none if no value is provided
        if value == '':
            value = None

        # Checking if value size is less than 15kb
        if sys.getsizeof(value) > 15000:
            raise Exception("Size of the entered value exceeds capped 15KB size limit.")

        if not self.check_file_size():
            raise Exception('Size of the file exceeds 1 GB.')

        self.datalock.acquire()
        if key in self.data.keys():
            self.datalock.release()

            raise Exception('Key is already present.')

        # ttl is Time-To-Live.
        # It is the time upto which a key can be read or deleted
        # The key expires after the set ttl
        # ttl is given in form of seconds
        # ttl is optional. In case of no input of ttl, the key value is considered to have no expiry
        if ttl is not None:

            ttl = int(time.time()) + abs(int(ttl))
            tempdict = {'value': value, 'ttl': ttl}

            self.data[key] = tempdict
            self.filelock.acquire()
            json.dump(self.data, fp=open(self.filepath, 'w'), indent=3)

            self.filelock.release()
            self.datalock.release()

            return True


        else:
            ttl = None
            tempdict = {'value': value, 'ttl': ttl}
            self.data[key] = tempdict
            self.filelock.acquire()
            json.dump(self.data, fp=open(self.filepath, 'w'), indent=2)

            self.filelock.release()
            self.datalock.release()

            return True


