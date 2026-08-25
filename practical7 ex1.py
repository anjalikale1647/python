text = input("Enter email/text: ")

at_count = text.count("@")
dot_count = text.count(".")
exclamation_count = text.count("!")

print("@ occurs", at_count, "times")
print(". occurs", dot_count, "times")
print("! occurs", exclamation_count, "times")