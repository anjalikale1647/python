print("\n=====* Traffic Light Program *=====\n")

signal = input("Enter the traffic light color (Red, Yellow, Green): ")

if signal.lower() == "red":
    print("Stop.!!")
elif signal.lower() == "yellow":
    print("Get Ready")
elif signal.lower() == "green":
    print("Go")
else:
    print("Invalid traffic light color")
