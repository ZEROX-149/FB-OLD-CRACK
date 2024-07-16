import platform,os,time
bit = platform.architecture()[0]
if bit == '64bit':
    import old32
elif bit == '32bit':
    import old64
