def solution(month, day):
    days = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    months = {"January": 1, "February" :2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October":10, "November": 11, "December": 12}
    
    day_name = ["", "Monday", "Tuesday", "wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    days = days[months[month]] + day 
    print (months[month], " ", day)

    calc = (days - 4) % 8

    if (days - 4) % 8 == 0: return "Weeknday"
    else: return day_name[(days - 4)%8]

print(solution("January", 4))
print(solution("February", 4))


print (" " * 5 + "1")