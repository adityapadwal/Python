# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month, day, year = input().split()

weekDay = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

testInput = calendar.weekday(int(year), int(month.strip('0')), int(day.strip('0')))

print(weekDay[testInput])