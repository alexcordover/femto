from os import listdir,system

file_list = [x for x in listdir('X_Rays') if x[-3:]=='IMG']

for element in file_list[:2]:
    command = "convert -size 2048x2048 -depth 16 -endian MSB -normalize gray:"+str(element)+" -compress lzw"+str(element)+".tif"
    print(command)
    #system(command)
