#Converts List of Documents to Markdown File Ready To Edit
import sys

if(len(sys.argv) == 1):
	print("Usage: python " + str(sys.argv[0]) + " <filepath.txt>")
	sys.exit()
file = sys.argv[1]
with open(file) as f:
    content = f.readlines()
#print content

newFile = ""
for topic in content:
    newFile += "\n## "
    newFile += topic
    newFile += "\n\n### Overview\n\n### Cause\n\n### Effect\n\n\n"

file = file.replace(".txt", "")
fileName = file + "-output.md"
file = open(fileName, "w")
file.write(newFile)
file.close()
