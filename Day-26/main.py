# Video-49&50&51

# Read file
# f=open("my-file1.txt","r")
# print(f.read())
# f.close()

# Write file
# f=open('my-file1.txt',"w")
# f.write("I want to marry her")
# f.close()

# with keyword
# with open('my-file1.txt', 'r') as f: print(f.read())

# readiness()
# f = open('my-file1.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# writelines()
# f = open('my-file3.txt', 'w')
# lines=["line1\n", "line2\n","line3\n"]
# f.writelines(lines)
# f.close()



#seek file and tell file function
with open('my-file1.txt', 'r') as f:
    print(type(f))
    # move to  the 10th byte in the file
    f.seek(10)

    # read the next 5 bytes
    data = f.read(5)
    print(data)
