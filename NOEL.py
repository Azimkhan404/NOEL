import os,platform
os.system('git pull')
 
NOEL=platform.architecture()[0]
if NOEL=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif NOEL=="64bit":
     __import__("NOEL")
 
