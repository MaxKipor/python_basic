number = int(input("enter seconds "))
hours, num = divmod(number, 3600)
min, sec = divmod(num, 60)
print("your time {0}:{1}:{2}".format(hours, min, sec))
