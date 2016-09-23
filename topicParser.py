with open("topics.txt") as f:
    content = f.readlines()
print content

newFile = ""
for topic in content:
    newFile += "\n##"
    newFile += topic
    newFile += "\n###Overview\n\n###Cause\n\n###Effect\n\n"

file = open("output.txt", "w")
file.write(newFile)
file.close()
