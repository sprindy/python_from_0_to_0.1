#!/usr/local/bin/python3

# "alt + shift" for column select
print("     March 2020")
print("Mo Tu We Th Fr Sa Su")
print("                   1")
print(" 2  3  4  5  6  7  8")
print(" 9 10 11 12 13 14 15")
print("16 17 18 19 20 21 22")
print("23 24 25 26 27 28 29")
print("30 31")

#''' OOB
import calendar

# 0=Mon, 6=Sun
#calendar.setfirstweekday(6)
cal = calendar.month(2020, 3)
print(cal)
#'''