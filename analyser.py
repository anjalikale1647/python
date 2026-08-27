print("====== Text Analyzer ======")

text = input("Enter your paragraph: ")

characters = len(text)

spaces = text.count(" ")


vowels = 0
for char in text:
    if char.lower() in "aeiou":
        vowels += 1


words = len(text.split())


print("\n--- Text Analysis ---")
print("Words      :", words)
print("Vowels     :", vowels)
print("Spaces     :", spaces)
print("Characters :", characters)
