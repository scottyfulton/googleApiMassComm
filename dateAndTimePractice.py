import datetime

now = datetime.datetime.now()
now2 = now.strftime("%x")




# print (now.strftime("%x"))

# print
# print "Current date and time using str method of datetime object:"
# print str(now)

# print
# print "Current date and time using instance attributes:"
# print "Current year: %d" % now.year
# print "Current month: %d" % now.month
# print "Current day: %d" % now.day
# print "Current hour: %d" % now.hour
# print "Current minute: %d" % now.minute
# print "Current second: %d" % now.second
# print "Current microsecond: %d" % now.microsecond

# print
# print "Current date and time using strftime:"
# print now.strftime("%Y-%m-%d %H:%M")

# print
# print "Current date and time using isoformat:"
# print now.isoformat()


# Directive	Meaning	Notes
# %a	Locale's abbreviated weekday name.	
# %A	Locale's full weekday name.	
# %b	Locale's abbreviated month name.	
# %B	Locale's full month name.	
# %c	Locale's appropriate date and time representation.	
# %d	Day of the month as a decimal number [01,31].	
# %H	Hour (24-hour clock) as a decimal number [00,23].	
# %I	Hour (12-hour clock) as a decimal number [01,12].	
# %j	Day of the year as a decimal number [001,366].	
# %m	Month as a decimal number [01,12].	
# %M	Minute as a decimal number [00,59].	
# %p	Locale's equivalent of either AM or PM.	(1)
# %S	Second as a decimal number [00,61].	(2)
# %U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.	(3)
# %w	Weekday as a decimal number [0(Sunday),6].	
# %W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.	(3)
# %x	Locale's appropriate date representation.	
# %X	Locale's appropriate time representation.	
# %y	Year without century as a decimal number [00,99].	
# %Y	Year with century as a decimal number.	
# %Z	Time zone name (no characters if no time zone exists).	
# %%	A literal "%" character.