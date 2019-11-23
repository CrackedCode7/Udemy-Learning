mathTest,physicsTest,chemistryTest=[float(x) for x in input("Enter math grade, physics grade, and chemistry grade:").split()]
if mathTest < 35 or physicsTest < 35 or chemistryTest < 35:
    print("You have failed")
elif mathTest >= 35 and physicsTest >= 35 and chemistryTest >= 35:
    average = (mathTest+physicsTest+chemistryTest)/3
    print("Score is {}".format(average))
    if average <= 59:
        print("Grade is C")
    elif average <= 69:
        print("Grade is B")
    else:
        print("Grade is A")
