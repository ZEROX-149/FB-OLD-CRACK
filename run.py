import platform,os,time
bit = platform.architecture()[0]
if bit == '64bit':
    import old64
elif bit == '32bit':
    import old32
