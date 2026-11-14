file_read = open("mode.txt","r")
print("Read mode-")
print(file_read.read())
file_read.close() 

file_write = open("mode.txt","w")
file_write.write("Write mode...")
file_write.write("Hi How are You Doing?")
file_write.close()

file_append = open("mode.txt","a")
file_append.write("\n Append mode...")
file_append.write("I am Happy!")
file_append.close() 