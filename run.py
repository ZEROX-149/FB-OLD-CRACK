import platform,os,time
bit = platform.architecture()[0]
if bit == '64bit':
    os.system("python index.py")
elif bit == '32bit':
    import run32
