"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("Please enter your age: "))

maxRate = 220 - age
slowestRate = maxRate * 0.65
fastestRate = maxRate * 0.85

# Use an f-string to create and print a message for the user to see.
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowestRate:.0f} and {fastestRate:.0f}")
print("beats per minute.")
