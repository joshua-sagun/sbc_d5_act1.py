#corrupt office

#stack
l = []
def wala():
    print(line)
    print("Removed from line:", line[-1])
    line.pop(-1)
    print(line)

#queue
def naa():
        print(line)
        print("Removed from line:", line[0])
        line.pop(0)
        print(line)

line = []
line_length = int(input("Enter length to the line: "))

for l in range(1,line_length + 1):
      line.append(l)

print("Process Line: ", line)

for c in range(len(line)):
      Head_status = input("Naa atong boss? naa/wala: ")
      Head_status.lower

      if Head_status == "wala":
            wala()

      elif Head_status == "naa":
            naa()


      