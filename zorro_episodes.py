import sys

def parseEpisodes(path):
	with open(path) as f:
		content = f.readlines()
	lines = [l.split() for l in content]
	listOfCategories = [el[1] for el in lines]
	return listOfCategories

def countHeusticTDD(events):
	#events = events[::-1]  #reverse the list AND returns it
	TFCounter = 0
	TLCounter = 0 
	TF = False
	TL = False
	while(events):
		el = events.pop()
		if el == "test-first":
			TFCounter +=1
			TF=True
			TL=False
		elif el == "test-last":
			TLCounter+=1
			TF=False
			TL=True
		else:
			if TF:
				TFCounter+=1
			else:
				TLCounter+=1
	result = {"TF": TFCounter, "TL": TLCounter}
	return result


	# for i, ev in events:
	# 	if ev=="test-first"
	# 		start = i

def main(argv):
	baseUri = "C:\\Users\\dfucci\\Desktop\\SQAT\\return box\\"
	subjectUri = baseUri + argv
	if os.path.exists(subjectUri):
		cats  = parseEpisodes("C:\Users\dfucci\Desktop\SQAT\zorroEpisodes.txt")
		denominator = len(cats)
		res = countHeusticTDD(cats)
		numerator = float(res["TF"])
		print "Conformance level: {0:.0f}%".format(numerator/denominator*100)
	else:
		print "Cannot find directory"

		
if __name__ == "__main__":
	main(sys.argv[1])