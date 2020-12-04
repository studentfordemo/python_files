import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
        access_token = 'sl.Amig3GqbjfMw6XuHBnacM76HPbaQOQxgHn5QdP3_RQRRieQF7nWKs1BvV7cePzR7og82aMvE9LcglZ1hjtzz8iOt6WgAGaLWNvfNoJqUIorRL1RVTWDdKoAbb7T901Dhj0NIVo0'
        transferData = TransferData(access_token)
        file_from = input("Enter The File Path That Needs To Be Transfered:")
        file_to = input("Enter The File Destination:")
        transferData.upload_file(file_from,file_to)
        print("File Has Been Moved")
        
main()
