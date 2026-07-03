try:
    marks = float(input("Enter your marks: "))

    if marks >= 75:
        print("Grade: Distinction")
    elif marks >= 60:
        print("Grade: First Class")
    elif marks >= 50:
        print("Grade: Second Class")
    elif marks < 50:
        print("Grade: Fail")
    else:
        print("Invalid marks entered.")
except ValueError:
    print("Please enter a valid numeric value.")