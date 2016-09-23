#Converts List of Documents to Markdown File Ready To Edit

with open("topics.txt") as f:
    content = f.readlines()
print content

newFile = ""
for topic in content:
    newFile += "\n##"
    newFile += topic
    newFile += "\n###Overview\n\n###Cause\n\n###Effect\n\n"

file = open("output.md", "w")
file.write(newFile)
file.close()
