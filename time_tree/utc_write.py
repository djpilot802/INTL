import zulu


print("Zulu object when timezone is passed:",
	zulu.parse('2020-04-17T16:10:15.708064+00:00'))

print("Zulu object when only date is passed:",
	zulu.parse('2020-04-17'))

print("Zulu object when date and time is passed:",
	zulu.parse('2020-04-17 16:10'))

print("Zulu object when ISO8601 is passed as formats:",
	zulu.parse('2020-04-17T16:10:15.000000Z',
				zulu.ISO8601))

print("Zulu object when Default timezone is used :",
	zulu.parse('2020-04-17',
				default_tz ='US/Eastern'))
