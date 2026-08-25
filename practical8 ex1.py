# Read user inputs
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

# Strip leading/trailing whitespaces and convert to title case
clean_first = first_name.strip().title()
clean_last = last_name.strip().title()

# Combine into full name
full_name = f"{clean_first} {clean_last}"

print("Sanitized Full Name:", full_name)