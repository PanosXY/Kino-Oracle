import urllib
import json
import time
import collections
import operator
from colors import green, red

AllNumbers    = []
TimesAppeared = []
FinalTimes    = []
Final         = []

date = time.strftime("%d-%m-%Y")
if int(time.strftime("%H")) < 9:
	print 'Draws start at 09:00 AM'
	exit()

url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/" + date + ".json"
try:
    response = urllib.urlopen(url)
except:
    print 'Server is down'
    exit()
data = json.loads(response.read())

draws = len(data['draws']['draw'])

for i in xrange(draws):
	for j in xrange(20):
		AllNumbers.append(data['draws']['draw'][i]['results'][j])

MostUsed = collections.Counter(AllNumbers)

fl = True
while fl:
	try:
		NumbersToPlay = int(input('Numbers To Play (1~12): '))
		if NumbersToPlay > 12:
			print 'Out of bounds.'
		else:
			fl = False
	except KeyboardInterrupt:
		print 'Keyboard Interrupt'
		exit()
	except:
		continue

MostUsed = dict(MostUsed)
TimesAppeared = MostUsed.values()
TimesAppeared.sort(reverse = True)

for i in xrange(NumbersToPlay):
	FinalTimes.append(TimesAppeared[i])

AllTuple =  MostUsed.items()

for i in xrange(80):
	for j in xrange(NumbersToPlay):
		if AllTuple[i][1] == FinalTimes[j]:	
			Final.append(AllTuple[i][0])

Final = list(set(Final))

n, l = [], []
for num in Final:
	for j in xrange(80):
		if num == AllTuple[j][0]:
			n.append(AllTuple[j][0])
			l.append(AllTuple[j][1])

d = dict(zip(n, l))
Sorted_d = sorted(d.items(), key=operator.itemgetter(1))
Reverse_Sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse = True)

print '\nYour numbers are (', red('red'), 'are optional ):',
for fn in xrange(NumbersToPlay):
	print green(str(Reverse_Sorted_d[fn][0])),

for fn in xrange(NumbersToPlay, len(Reverse_Sorted_d)):
        print red(str(Reverse_Sorted_d[fn][0])),

print
