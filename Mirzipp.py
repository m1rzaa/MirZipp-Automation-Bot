import zipfile, os

        
def main():
    fileszipped = 0
    filesquantity = 0
    bol = True
    cnt = 0
    for i in os.listdir():
        cnt += 1
        if(cnt<8):
            if bol:
                temp = os.path.splitext(i)
                name = temp[0] + '.zip'
                handle = zipfile.ZipFile(name, 'w')
                fileszipped += 1
            handle.write(i, compress_type = zipfile.ZIP_DEFLATED)
            filesquantity += 1
            bol = False
        
        elif(cnt==8):
            handle.write(i, compress_type = zipfile.ZIP_DEFLATED)
            filesquantity += 1
            handle.close()
            bol = True
            cnt = 0
               
        
    print("{} files are compressed into {} zipped files".format(filesquantity, fileszipped))   
main()
