from os import listdir,system

file_list = [x for x in listdir('.') if x[-3:]=='IMG']

for element in file_list:
    command = "convert -size 2048x2048 -depth 16 -endian MSB -normalize gray:"+str(element)+' '+str(element[:-4])+".tif"
    system(command)
