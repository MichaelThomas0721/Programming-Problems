with open('GenerateTestCode.txt') as f:
    lines = f.readlines()
tests = []
currentTest = []
for line in lines:
    if "Input" in line and len(currentTest) == 0:
        splitLine = line.split(' = ')
        del splitLine[0]
        input = []
        while splitLine:
            if len(splitLine) >= 1:
                input.append(splitLine[0].rsplit(",", 1)[0].strip("'"))
                del splitLine[0]
            else:
                input.append(splitLine[0].rsplit("\n", 1)[0].strip("'"))
                print("HEEUERIREHIUREH")
                del splitLine[0]
            print(splitLine)
        currentTest.append(input)
    elif "Output" in line and len(currentTest) == 1:
        line = line.strip("Output: ")
        line = line.strip("\n")
        currentTest.append(line)
        tests.append(currentTest)
        currentTest = []
    elif "Input" in line and len(currentTest) != 0:
        print("ERROR, DOUBLE INPUT")
        break;
    elif "Output" in line and len(currentTest) != 1:
        print("ERROR, DOUBLE OUTPUT BEFORE INPUT OR SOMETHING IDK")
    
testVariables = '['

print("E", tests)

for test in tests:
    testVariables += str(test[0])
    testVariables += ','
    testVariables += str(test[1])
    testVariables += ','
testVariables += ']'

print(testVariables)