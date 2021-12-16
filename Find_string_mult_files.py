import os
import re

word = "cat"
for root, dirs, files in os.walk("/Users/karpuri/Documents/Devnet/automate_project"):
    #file1 = os.path.join(root, str(files))
    #print(type(dirs))
    for i in files:
        #print(i)
        try:
            file1 = os.path.join(root, i)
        except OSError as err:
            if err.errno == 2:
                continue
        print(file1)
    #open_file = open(file1, "r")
    #if(word in file1.read()):
           
   
    
    #test = re.search(r'(.*?cat.*?)\n', 'I like elephants.\nThey are nice')

    #print ("Root Files")
    #print(root)
    #print ("dir Files")
    #print(dirs)
    #print ("Files")
    #print(files)

