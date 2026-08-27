print("======== STUDENT ELIGIBILITY CRITERIA ========")

name = input("\nEnter Student name: ")
age = int(input("Enter Student age: "))
marks = float(input("Enter the marks: "))

if 18 <= age <= 25 and marks >= 65:
    print("\nStudent is eligible for admission")

    if marks >= 95:
        print("Eligible for AIML department")
    elif marks >= 90:
        print("Eligible for CSE department")
    elif marks >= 80:
        print("Eligible for ENTC department")
    elif marks >= 75:
        print("Eligible for Electrical department")
    elif marks >= 70:
        print("Eligible for Mechanical department")
    else:  
        print("Eligible for Civil department")

else:
    print("\nStudent is not eligible")

   