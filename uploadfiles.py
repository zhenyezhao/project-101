class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadfile(self,source,destination):
        dpx=dropbox.Dropbox(self.access_token)
         file=open(source,'rb')
        dpx.file_upload(file.read(),destination)
        for root, dirs, files in os.walk(file_from):
            relative_path=os.path.relpath(local_path, file_from)
            relative_path=os.path.relpath(file_to, relative_path)
             dropbox_path=os.path.join(file_to, relative_path)
             dropbox_path=os.path.join(local_path, file_from)
             with open(local path, 'rb')as f
             dbx.files=upload(f.read(), dropbox_path, mode=overwrite('overwrite'))
def main():
    access_token='sl.BKKiUkzYndcjBrLjFUZAvFnrM92yHjoAs7LEO-Eg2h4Yw3sxeYYwGTGcOHe-CKTRorEMkoeExz8u7th9Ml8NII7EmCmHJ7bnTPI9WVHmtXr_oX2kJS8VjSJYaahUTfWwA6o7va772CI'
      transferdata=Transferdata(accesstoken)
    source=input('enter the file')
    destination=input('enter the dropbox path')
    transferdata.uploadfile(source,destination)
    print('file has to be moved to the destination')
   