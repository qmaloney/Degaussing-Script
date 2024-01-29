while True:
    print("")
    print("Degaussing Media Destruction Script for the LM-1 Degausser:")
    print("")
    print("By Quinn Maloney")

    print("Script to Format Test Results from the HDD Degausser to Ensure HDD's Are Properly Degaussed Within AWS DCO Operations:")
    print("")
    print("Please Enter Media Destruction Equiment Info:")
    print("")
    MediaDestructionInfo = []
    SerialID = input("Scan the destruction machine {BIN ID}:")
    AssetID = input("Enter Device Asset ID: ")
    MediaDestructionInfo.append(SerialID)
    MediaDestructionInfo.append(AssetID)
    print("")

    MediaDestructionInfo = ["Serial ID: " + str(SerialID), "Asset ID: " + str(AssetID)]
    for item in MediaDestructionInfo:
        print(item)

    print("")
    print("Next, Please Enter Degaussing Test Measurements:")
    print("TEST 1:")
    print("")
    # Lists for Average
    S_Average = []
    M_Average = []
    L_Average = []


    Test1List = []
    while True:
        try:
            S1 = float(input("Enter Result for S: "))
            M1 = float(input("Enter Result for M: "))
            L1 = float(input("Enter Result for L: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    Test1List.append(S1)
    S_Average.append(S1)

    Test1List.append(M1)
    M_Average.append(M1)

    Test1List.append(L1)
    L_Average.append(L1)

    print(Test1List)


    #Add Prefix:
    Test1List = ["S: " + str(S1), "M: " + str(M1), "L: " + str(L1)]
    print("TEST 1:")
    print("")
    print(Test1List)
    print("")


    print("Please Enter Results for TEST 2:")
    print("")
    Test2List = []
    while True:
        try:
            S2 = float(input("Enter Result for S: "))
            M2 = float(input("Enter Result for M: "))
            L2 = float(input("Enter Result for L: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    Test2List.append(S2)
    S_Average.append(S2)

    Test2List.append(M2)
    M_Average.append(M2)

    Test2List.append(L2)
    L_Average.append(L2)

    print("")
    print("TEST 2:")
    print("")
    print(Test2List)

    #Add Prefix:

    Test2List = ["S: " + str(S2), "M: " + str(M2), "L: " + str(L2)]
    print("")
    print("Please Enter Results for TEST 3:")
    print("")
    Test3List = []


    while True:
        try:
            S3 = float(input("Enter Result for S: "))
            M3 = float(input("Enter Result for M: "))
            L3 = float(input("Enter Result for L: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    Test3List.append(S3)
    S_Average.append(S3)

    Test3List.append(M3)
    M_Average.append(M3)

    Test3List.append(L3)
    L_Average.append(L3)

    #Add Prefix:
    Test3List = ["S: " + str(S3), "M: " + str(M3), "L: " + str(L3)]
    print("TEST 3:")
    print("")
    print(Test3List)
    print("")

    #Create a function for calculating Average:

# Code before rounding:
    ''' for num in lst:
        total += num
    average = total / len(lst)
    return average'''
    def calculate_average(lst):
        total = 0
        
        for num in lst:
            total += num
        average = total / len(lst)
        rounded_average = round(average, 1)
        return rounded_average


    print("DEGAUSSING TEST SUMMARY:")
    print("")
    for item in MediaDestructionInfo:
        print(item)
    print("")
    print("AVERAGE'S:")
    result_S = calculate_average(S_Average)
    print("S Average:",result_S )
    result_M = calculate_average(M_Average)
    print("M Average:", result_M)
    result_L = calculate_average(L_Average)
    print("L Average:", result_L)
    print("")
    print("TEST 1:",Test1List)
    print("TEST 2:",Test2List)
    print("TEST 3:",Test3List)
    print("")
    choice = input ("Do you want to restart the script? (y/n)")
    if choice.lower() != "y":
        break

