import sys
print('==========================================')
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
with open('1.txt', 'w+') as f:
    f.write('This is new file......')
print("Done")
print('==========================================')
