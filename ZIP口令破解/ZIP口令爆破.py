import zipfile
zFile = zipfile.ZipFile('')
passfile = open('dicyionary.txt')
for line in passfile.readlines():
    password = line.strip('\n')
    try:
        zFile.extractall(pwd=password)
        print ('[+] Password =' + password +'\n')
        exit(0)
    except Exception as e:
        pass
