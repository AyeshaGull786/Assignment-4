# 06_seconds_in_year

# Problem Statement
# Use Python to calculate the number of seconds in a year, and tell the user what 
# the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 
# 60 minutes in an hour, and 60 seconds per minute.

#storing constant values 
days_in_year: int = 365
hours_per_day: int = 24
min_per_hour: int = 60
sec_per_hour: int= 60
LEAP_YEAR_DAYS = 366

def main():
# Calculate total seconds in a year
    Total_sec_in_year: int = days_in_year * hours_per_day * min_per_hour * sec_per_hour

# Calculate total seconds in a leap year
    Total_sec_in_leap_year: int = LEAP_YEAR_DAYS * hours_per_day * min_per_hour * sec_per_hour

# Print the result in a formatted statement
    print(f"There are {Total_sec_in_year} seconds in a year!\n")
    
#result for leap year    
    print(f"There are {Total_sec_in_leap_year} seconds in a leap year!")
    
#call main function
if __name__ == '__main__':
    main()
