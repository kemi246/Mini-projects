greeting =input("Good day, what was your grade on the last assignment? Please enter your grade as a percentage (e.g., 85 for 85%). ")
grade = float(greeting)

#90 = A 80 = B 70 = C 60 = D 59 and below = F
if grade >= 90:
    print("Excellent work! You received an A.")
elif grade >= 80:
    print('Good work! You received a B.')
elif grade >=70:
    print('You received a C. Keep working hard!')
elif grade >= 60:
    print('You received a D. Keep trying, you can do better!')
else:
    print('You received an F. Better luck next time!')