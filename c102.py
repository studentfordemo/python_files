import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,50)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        result=False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def upload_file(img_name):
    access_token="sl.AmvO3CeNa_Cu8QAOuDbiH7Safof5fqRAEe4pJ0-C-K-C60mYOn4e5du8tphhbxJQbeSCFUNl5qRcDE9ofo8taFkFRL2b558RuxnHY2R0U4SnQa2eD42C1d_2rRVrNcSUNad52Ns"
    file=img_name
    file_from=file
    file_to="/newFolder2/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")
        
def main():
    while(True):
        if((time.time()-start_time)>120):
            name=take_snapshot()
            upload_file(name)
main()

    
    