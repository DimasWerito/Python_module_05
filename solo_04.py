"""
You are developing software for a medical device 
that informs patients about their blood sugar level.

 

Task

Complete the given code to display different messages to the patient based on the blood sugar levels
"""


# Glucose level is an input for this software
glucose_level = int(input())

# Display message if glucose level is less than 70
if glucose_level < 70:
    print("Low glucose level")

# Display message if glucose level is greater than 140
elif glucose_level > 140:
    print("High glucose level")

# Display message if none of the conditions above are met
else:
    print("Normal range")