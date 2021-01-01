import unittest
import crd

class TestCrd(unittest.TestCase):
    def test_create(self):

        #Checking for proper insertion of data when key, value as well as Time-To-Live is provided
        a=crd.crd().create("A","65",12)
        self.assertEqual(a,True)

        #Checking for proper insertion of data when key, value is provided but Time-To-Live is not provided
        b=crd.crd().create("B","66")
        self.assertEqual(a,True)\

        #Checking for exception when same key is provided
        self.assertRaises(Exception,crd.crd().create,"B","2")

        #Checking for exception when key value is not provided
        self.assertRaises(Exception,crd.crd().create,"","2")

        #Checking for proper insertion of data when key is provided but value & Time-To-Live is not provided
        c=crd.crd().create("C","")
        self.assertEqual(c,True)

        #Checking for proper insertion of data when key & Time-To-Live is provided but value is not provided
        d=crd.crd().create("D","",21)
        self.assertEqual(c,True)

        #Checking for exception when key length is greater than 31
        self.assertRaises(Exception,crd.crd().create,"abcdefghijklmnopqrstuvwxyz1234567","2")

        #Checking for file size limited to 1 gb
        self.assertEqual(crd.crd().check_file_size(),True)

   def test_read(self):

        #Checking if key corresponds to right value as inserted before
        val=crd.crd().read("B")
        self.assertEqual(val,'"66"')

        #Checking for exception for a key not inserted
        self.assertRaises(Exception,crd.crd().read,"G")

        #Checking for exception for no key entered
        self.assertRaises(Exception,crd.crd().read,"")

        def test_delete(self):
            # Checking if key is deleted if present
            val = crd.crd().delete("C")
            self.assertEqual(val, "Key-value pair deleted")

            # Checking for exception when key not present is entered
            self.assertRaises(Exception, crd.crd().delete, "notok")

            # Checking for exception when no key is entered
            self.assertRaises(Exception, crd.crd().delete, "")


if __name__ == '__main__':
    unittest.main()