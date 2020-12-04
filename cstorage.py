import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = 'sl.AmcXEKIzbZQUMBbHQY8HNvi3OcjK_-Ej2KmKJPJjNkWhhNlRh1Coix3PERIfeFfG8EExjtQ1oydSkwv2Pb798ywbQgaAePEGKv3IMtLKmNNbu2pVTE8I-FkU5pOO1Ks3PXqmznc'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()