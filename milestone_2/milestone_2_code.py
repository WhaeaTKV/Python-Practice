
#This python programme finds your age based on the year you were born and the current year.
year = int(input("What year were you born? "))
current_year = int(input("Enter the current year: "))
age = current_year - year
print("You are {} years old in {}.".format(age, current_year))
