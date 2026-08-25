# Initial list of student grades
grades = [85.5, 92.0, 78.0, 64.5, 88.0]

print("Original Grades List:", grades)

# Prompt user for index and new grade entry
index = int(input(f"Enter target index position (0 to {len(grades) - 1}): "))

if 0 <= index < len(grades):
    new_grade = float(input("Enter the new grade entry: "))
    
    # Update score at the specific index
    grades[index] = new_grade
    
    # Display the corrected list
    print("Corrected List:", grades)
else:
    print("Invalid index position.")