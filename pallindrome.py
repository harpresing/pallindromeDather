ascii_char = ""

def findLargestPallindrome(case):
	occurance = {}
	for i in xrange(len(case)):
		if case[i] in occurance:
			occurance[case[i]] += 1
		else:
			occurance[case[i]] = 1
	x = dict((k, v) for k, v in occurance.iteritems() if v >= 2)
   	y = dict((k, v) for k, v in occurance.iteritems() if v % 2 is not 0)
	str = ""
	for key in x:
		for i in xrange((x[key]/2)):
			str += key
	rev = str[::-1]
	if len(y) > 0:
		ans = "%s %s %s" % (str, y.keys()[0], rev)
	else:
		ans = "%s %s" % (str, rev)
	ans = ans.replace(" ", "")
	
	global ascii_char
	
	ascii_char += (chr(65 + len(case) - len(ans)))


def run():
	cases = []
	testCases = int(raw_input().strip())
	for i in xrange(testCases):
		cases.append(raw_input().strip())

	for case in cases:
		findLargestPallindrome(case.replace(" ",""))
		global ascii_char
	print ascii_char

if __name__ == "__main__":
	run()

