import os
root= "/home/mohansai/Automation/Mohansai_samples/class"

count=0
Total=0
for path, subdirs, files in os.walk(root):
    for name in files:
       file = os.path.join(path, name)
       with open(file,errors='ignore') as fname:
            for line in fname:
              #print(line)
              if not line.strip():
                 continue
              else:
                count=count+1
            print("{},count-->{}".format(file,count))
       Total=Total+count
print("Total-->", Total)