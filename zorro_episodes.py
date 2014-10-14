import sys
import os
def parseEpisodes(content):
	# with open(path) as f:
	# 	content = f.readlines()
	lines = [l.split() for l in content]
	listOfCategories = [el[1] for el in lines]
	return listOfCategories

def countHeusticTDD(events):
	#events = events[::-1]  #reverse the list AND returns it
	TFCounter = 0
	TLCounter = 0
	RafactoringCounter = 0
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
		elif el == "refactoring":
			RefactoringCounter+=1
		else:
			if TF:
				TFCounter+=1
			else:
				TLCounter+=1
		result = {"TF": TFCounter, "TL": TLCounter, "Refactoring": RefactoringCounter}
	return result



def mergeZorroEpisodes(dir):
	buff = []
	for zorroDir in os.listdir(dir):
		epdisode_file = dir+"/"+zorroDir+'/zorroEpisodes.txt'
		if os.path.isfile(epdisode_file):
			with open(epdisode_file) as f:
				buff= buff + f.readlines()
	return buff

def main(besouro_dir):
	#basePath = "C:\\Users\\dfucci\\Dropbox\\TOL\\PhD\\Publications\\TDD Process Conformance Relationship With Code Quality\\BSK\\"
	#subjectPath = basePath + subject + '\\BSK\\'
	print "========================="
	for dir in os.listdir(besouro_dir):
		if os.path.isdir(besouro_dir+"/"+dir):
			print dir
			content = mergeZorroEpisodes(besouro_dir)
			cats  = parseEpisodes(content)
			denominator = len(cats)
			res = countHeusticTDD(cats)
			numerator = float(res["TF"])
			print "number of eposides %s" % denominator
			if denominator > 0:
				print "Conformance level: {0:.0f}%".format(numerator/denominator*100)

			else:
				print "No episodes present"
			print "========================="

if __name__ == "__main__":
	if (len(sys.argv)>1):
		main(sys.argv[1])
	else:
		print "Usage: zorro_episode <path to besouro folder>"
