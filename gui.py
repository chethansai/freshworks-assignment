from tkinter import *
import crd

root = Tk()


#Creating and storing given Key, Value & optional Time-To-Live into file
def create():
    #assigning entered key, value & TTL
    st1=c_key.get()
    st2=c_value.get()
    st3=c_ttl.get()

    #Checking if optional TTL is entered or not & converting into integer if entered
    if (st3 == ''):
        st3 = None
    else:
        st3 = int(st3)

    #Storing entered data
    try:
        if (crd.crd().create(st1, st2, st3)):
            l = Label(root, text='Value is added!!',width=20)
            l.grid(row=12, column=1)
    except Exception as e:
        l = Label(root, text=e.args[0],width=20)
        l.grid(row=12, column=1)





#GUI Window to Create, Read & Delete

#Create Section of GUI
#Create Heading
c_label = Label(root, text="CREATE")
c_label.grid(row=0,column=1)

#Key Label
c_key_l = Label(root, text="Key *")
c_key_l.grid(row=4,column=0)

#Key Input Box
c_key = Entry(root,width=35)
c_key.grid(row=4,column=1)

#Value Label
c_value_l = Label(root, text="Value *")
c_value_l.grid(row=6,column=0)

#Value input box
c_value = Entry(root, width=35)
c_value.grid(row=6,column=1)

#TTL Label
c_ttl_l = Label(root, text="Time-To-Live")
c_ttl_l.grid(row=8,column=0)

#TTL Input Box
c_ttl = Entry(root, width=35)
c_ttl.grid(row=8,column=1)

#Submit Button
c_button=Button(root,text="Submit",command=create)
c_button.grid(row=10,column=1)




#Read Section of GUI
#Read Heading
r_label = Label(root, text="READ")
r_label.grid(row=14,column=1)

#Key Label
r_key_l = Label(root, text="Key *")
r_key_l.grid(row=16,column=0)

r_key = Entry(root,width=35)
r_key.grid(row=16,column=1)

#Submit Button
r_button=Button(root,text="Submit",command=read)
r_button.grid(row=18,column=1)
