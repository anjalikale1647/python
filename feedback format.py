print("********* Customer Feedback formatter *********")

name = input("Enter your Name: ")
feedback = input("Enter your Feedback: ")
rating = int(input("Enter Your Rating (1-5):"))

name = name.upper()
feedback = feedback.upper()

formatted_name = name.lower()
formatted_feedback = feedback.lower()

formatted_name = name.title()
formatted_feedback = feedback.title()

formatted_name = name.capitalize()
formatted_feedback = feedback.capitalize()

formatted_name = name.strip()
formatted_feedback = feedback.strip()

print("\n******** Formatted Feedback ********")
print("Customer Name :", formatted_name)
print("feedback:", formatted_feedback)
print("Rating:", rating, "/5")

print("======== Thank You For Your Feedback ========")