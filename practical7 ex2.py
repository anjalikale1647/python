

paragraph = input("Enter your paragraph: ")


paragraph = paragraph.lower()

count = paragraph.split().count("python")

print("The word 'python' appears", count, "time(s).")