#junk file organizer
#python project to sort files


import os,shutil

print("welcome to junk file organizer")

print("Enter Yes if u want to do sorting by size")

typeofsort = input("Enter your decision")

folderpath = input("Enter your folder path to sort the files:")


#To sort according to size

if typeofsort == "Yes":
    def sizecheck(folderpath):
    list_dir = os.walk(folderpath)
    for dir,filename,file in list_dir:
        for f in file:
sizeoffile = os.stat(dir+"/"+f).st_size
         try:
             if sizeoffile<1024:
                 if
        os.path.exists(folderpath+"/byte_files/")
        shutil.move(folderpath+"/"+f,folderpath+"/byte_files/"+f)
              else:
                  os.mkdir(folderpath+"/byte_files/")
                  shutil.move(folderpath+"/"+f,folderpath+"byte_files/"+f)
             elif sizeoffile >= 1024 and sizeoffile<1000*1024:
            if
                      os.path.exists(folderpath+"/kilobytes_files/")

                      shutil.move(folderpath+"/"+ f,folderpath +"/kilobytes_files/"+f)
             else:
                           os.mkdir(folderpath+"/kilobytes_files/")
                           shutil.move(folderpath+"/"+f,folderpath+"/kilobytes_files/"+f)
             elif sizeoffile>=
                               1000*1024 and sizeoffile<=1000*1024*1024:
                               ifos.path.exists(folderpath+"/megabytes_files/"):
                                shutil.move(folderpath+"/"+f,folderpath +"/megabytes_files/"+f)
                else:
                    if
                    os.path.exists(folderpath+"/gigabytes_files/")

                    shutil.move(folderpath+"/"+f,folderpath+"/gigabytes_files/"+f)
                else:
                    os.mkdir(folderpath+"/gigabytes_files/")

                    shutil.move(folderpath+"/"+f,folderpath+"/gigabytes_files/"+f)

                    except fileexistsError:
                        continue
                    print("Done sorting:)")
                    sizecheck(folderpath)
