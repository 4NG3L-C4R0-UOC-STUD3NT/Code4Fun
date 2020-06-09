import datetime

my_birthdate = datetime.date(1974,4,6)
my_birthtime = datetime.time(16,0)
my_birthday = datetime.datetime.combine(my_birthdate, my_birthtime)
now = datetime.datetime.now()
print("my bithday date: {}".format(my_birthdate))
print("my bithday time: {}".format(my_birthtime))
print("my bithday day: {}".format(my_birthday))
time_passed = now - my_birthday
how_many_seconds = time_passed.total_seconds()
print("how many seconds since I born: {}".format(how_many_seconds))
