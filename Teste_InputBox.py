#Scripts Python - Amaury
list1 = ['Taskmaster', 'Rede Skull', 'Zemo']
list2 = ['Capt. America', 'Iron Man', 'Thor']

def findguy (where, inputguy):
	a = "not here"
	for i in (renge (len(where))):
		if where [i] == inputguy:
		a = "yes here"
	print a
	
#findguy (list2, 'Thor')

x = Application.XSIInputbox ("Who are you lookin for?","find character")
y = Application.XSIInputbox ("Which list?", "Search List")

#print yes

#print locals

findguy (x, y)
