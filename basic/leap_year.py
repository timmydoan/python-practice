def get_year():
    year = int(input("Enter a year: "))
    return year

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print (f"{year} is a leap year.")
    else:
        print (f"{year} is not a leap year.")

def main():
    year = get_year()
    check_leap_year(year)

main()