import os 
import shutil
destination= 'C:/Users/mitta_ck4oqhq/Downloads'
source= 'C:/Users/mitta_ck4oqhq/OneDrive/Desktop/folder/document_files'
files=os.listdir(source)
for i in files:
    new,ext=os.path.splitext(i)
    if ext=='':
        continue
    if ext in['.txt','.doc','.docx','.pdf']:
        path1=source + '/' + i 
        path2=destination + '/' + 'document_files'
        path3=destination + '/' + 'document_files' + '/' + i

        if os.path.exists(path2):
            print('Moving'+ 'document_files' + '.....')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Moving'+ 'document_files' + '.....')
            shutil.move(path1,path3)