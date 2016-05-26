

# Reads an annotation file and returns a dictionary:
# {key : value} -> {gene : (chr., starting position)}
def readGTF(annotationFile):
	gtf=open(annotationFile, "r")
	tss={}
	for l in gtf:
		s=l.split()
		if (len(s) >=9):
			if (s[2]=="gene" and s[0]!='chrM' and s[0]!='chrX' and s[0]!='chrY'):	
				if (s[6]=="+"):
					tss[s[9]]=(s[0].replace("chr",""),int(s[3]))
				else:
					tss[s[9]]=(s[0].replace("chr",""),int(s[4]))
	gtf.close()
	return tss


# Reads a loop file and returns a dictionary containg all intrachromosomal loops per chromosome in a list:
# {key : value} -> {chr : [(loopID, start X, end X, start Y, end Y, observations count)]}
def readIntraLoops(loopsFile):
	lf = open(loopsFile, 'r')
	loops = {}
	
	for i in range(1, 23):
		loops[str(i)] = []
	
	loopID = 0
	for l in lf:
		s=l.split()
		if (len(s) >=8):
			if(s[0] == s[3] and s[0]!='X' and s[0]!='Y'): # check if loop is intra-chromosomal
				loopID += 1
				loops[s[0]].append((loopID, int(s[1]), int(s[2]), int(s[4]), int(s[5]), int(s[7])))
	lf.close()
	return loops


# Reads a loop file and returns a dictionary containg all intrachromosomal loops per chromosome in a list:
#TODO: define format	
def readInterLoops(loopsFile):
	#TODO: implement this
	print 'Not implemented yet!'
	return 0


# Writes given header and body to a file defined by filename
def writeToFile(filename, header, body ):
	print 'Writing contents of ' + filename + ' to disk...' 
	f = open(filename, 'w')
	f.write(str(header))
	f.write('\n')
	f.write(str(body))
	f.close()
	print 'Finished'
