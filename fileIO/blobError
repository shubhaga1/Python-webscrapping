f = open("DS.txt", "r")
x=[]
i=""
try:
    for line in f:
    #     print(line)
        if "blobId" in line: 
#             x.append(line[90:-2])
            i= i +"\n" +line[90:-2]
except:
    pass
f.close()
print(i)



# saving the result in file
# 'w' is for write which will overwrite the existing data.

f = open("missingBlobs.txt", "a")
f.write(i)
f.close()
