
def getData(infname, homes):
	#homes will be passed as an empty list
	with open(infname, 'r') as inp:
		streetlen = int(inp.readline().strip())
		for el in inp.readline().strip().split():
			homes.append(int(el))
	return streetlen


## Test code

homes = []
streetlen = getData('python/sprint1_nonfinals/input.txt', homes)
#if streetlen:
#	print(homes)

distances = []

for i in range(streetlen):
	if homes[i]==0:
		distances.append(0)
		continue
	count = 0
	ldist = streetlen+1
	for l in range(i, 0, -1):
		count += 1
		if homes[l-1]==0:
			ldist = count
			break
	count = 0
	rdist = streetlen+1
	for r in range(i, streetlen-1):
		count += 1
		if homes[r+1]==0:
			rdist = count
			break
	# print(homes[i], ':', ldist, rdist)
	distances.append(min(ldist, rdist))
 
	
print(*distances)		

#0 7 9 4 8 20




