#Resume Parsing

#file_name = input("Enter data file")
file_name = "AccentureAnalyst2020.txt"
fHandle = open(file_name)

for line in fHandle:
    print(line)
fHandle.close()
