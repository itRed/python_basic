import os
path='E:\\pyWorkspace\\project1\\files'
for file in os.listdir(path):    
    if os.path.isfile(os.path.join(path,file))==True:
        newname=file.replace("test1","wangxingyu")
        os.rename(os.path.join(path,file),os.path.join(path,newname))
        print(file)
