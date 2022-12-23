#Reading Files


#Opens file
myFile=open('VaibhavMojidra.txt')

line1=myFile.readline()

print(line1) #Print line 1
print(myFile.readline()) #Print line 2
print(myFile.read()) #Prints all lines from line 3 to last line

myFile.close() #Closes files and unlock it from memory

print('\n\n\n')

with open("VaibhavMojidra.txt") as fileObj: #no Need to close however code should be in this block only
    print(fileObj.readline()) #Print line 1
    print(fileObj.readline()) #Print line 2
    print(fileObj.read()) #Prints all lines from line 3 to last line

print('\n\n\n')

myFile2=open('VaibhavMojidra.txt')
lines=myFile2.readlines()

print('Lines: ')
print(lines)
