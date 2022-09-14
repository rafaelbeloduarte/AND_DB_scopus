import pyreadr
import csv

# load scopus database
scopus_DB = []
with open('scopus_database.csv', newline='') as csvfile:
	scopus_data = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in scopus_data:
		row[0] = row[0].replace(".", "")
		scopus_DB.append(row)

# load differentiation list prepared manually
differentiation_list = []
with open('to_differentiate.csv', newline='') as csvfile:
	to_differentiate = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in to_differentiate:
		row = list(filter(None, row))
		differentiation_list.append(row)

# replace names contained in differenciation_list into the database
for i in scopus_DB:
	# print(i[1])
	for j in differentiation_list:
		# print("")
		# print(j)
		for k in range(1, len(j), 2):
			# print("")
			# print(j)
			# print(j[k])
			if j[k] in i[1]:
				# print("\n", j[k+1], " -> ", j[k], " is in ", i[1])
				# print(j[0].title())
				i[0] = i[0].replace(j[0].title(), j[k+1].replace(",", ""))
				# print(i[0])

# write a new csv file with disambiguated names
with open('scopus_DB_ANDed.csv', 'w', newline='') as csvfile:
	rowwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for row in scopus_DB:
		rowwriter.writerow(row)
