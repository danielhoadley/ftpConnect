from ftplib import FTP

ftp = FTP('hostname.goes.here')
ftp.login(user='username', passwd='password')

# Get a list of the directories on the FTP site to test the connection work
ftp.retrlines('LIST') 
