import os
root= "/home/mohansai/Automation/B_Python_work"
root1= "/home/mohansai/Automation/B_Python_work/1/1.1.py"

non_blank_count = 0

for path, subdirs, files in os.walk(root1):
    for name in files:
         file = os.path.join(path, name)
         print("file -->",file)
         with open(file,encoding="utf8", errors='ignore') as infp:
             for line in infp:
                 if line.strip():
                     non_blank_count += 1

print('number of non-blank lines found %d' % non_blank_count)
