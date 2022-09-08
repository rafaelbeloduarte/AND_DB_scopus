import pyreadr
from collections import Counter
import csv

result = pyreadr.read_r('Bibliometrix-Export-File-2022-09-06.RData') # also works for Rds

# done! let's see what we got
# result is a dictionary where keys are the name of objects and the values python
# objects
#print(result.keys()) # let's check what objects we got
M = result["M"] # extract the pandas data frame for object M

# print(dir(M))
# print(M.RP)

# criando uma lista com todos os autores
all_authors_repeated = []
all_AU_ID_repeated = []

# objeto author ID
AU_ID = getattr(M, 'Author.s..ID')
#corr_addr = getattr(M, 'Correspondence Address')
# print(M.AU)
authors_addr = {}
authors_addr_list = []

for i in range(len(M)):
	authors_tmp = []
	AU_ID_tmp = []
	
	authors_tmp = M.AU[i]
	AU_ID_tmp = AU_ID[i]
	
	authors_tmp = authors_tmp.split(";")
	AU_ID_tmp = AU_ID_tmp.split(";")
	#print(AU_ID_tmp)
	#print(authors_tmp)
	for j in range(len(authors_tmp)):
		all_authors_repeated.append(authors_tmp[j])
	for j in range(len(AU_ID_tmp)):
		all_AU_ID_repeated.append(AU_ID_tmp[j])
		
	# list of authors correspondance addresses
	
	# authors_addr_tmp = M.RP[i]
	
	# print(authors_addr_tmp)
	# authors_addr_split = authors_addr_tmp.split('\n')
	
	# for i in range(len(authors_addr_split)):
	# 	authors_addr_list.append(authors_addr_split[i].split(';'))

temp_list = all_AU_ID_repeated
all_AU_ID_repeated = list(filter(None, temp_list))

temp_list = all_authors_repeated
all_authors_repeated = list(filter(None, temp_list))

print("Authors string count: ", len(all_authors_repeated))
print("Authors IDs count: ", len(all_AU_ID_repeated))

# print(authors_addr_list[50][0])
# authors_addr_list_names = []
# authors_addr_list_addr = []
# for i in range(len(authors_addr_list)):
	# try:
		# authors_addr_list_names.append(authors_addr_list[i][0])
		# authors_addr_list_addr.append(authors_addr_list[i][1])
	# except Exception as e: 
		# print(e)

# check for duplicates in authors_addr_list
# import collections
# print("Repeated correspondance names:")
# print([item for item, count in collections.Counter(authors_addr_list_names).items() if count > 1])

# Python 3 code to demonstrate
# removing duplicate elements from the list
all_authors = [*set(all_authors_repeated)]
todos_AU_ID = [*set(all_AU_ID_repeated)]
# todos_AU_ID.remove('')
#print("List after removing duplicate elements: ", all_authors)
print("Total unique author strings: ", len(all_authors))
print("Total unique IDs: ", len(todos_AU_ID))

# creating a list to count all the times a name repeats
author_name_repeat_count = [0] * len(all_authors)
for i in range(len(all_authors)):
	for j in range(len(all_authors_repeated)):
		if all_authors[i] in all_authors_repeated[j]:
			# print(all_authors[i], "repeats at position ", j)
			author_name_repeat_count[i] = author_name_repeat_count[i] + 1

# creating a list of authors that appear more than once in data set
repeated_authors = []
unique_authors = []
for i in range(len(author_name_repeat_count)):
	if author_name_repeat_count[i] > 1:
		repeated_authors.append(all_authors[i])
	else:
		unique_authors.append(all_authors[i])

print("Number of repeated authors: ", len(repeated_authors))
print("Number of unique authors: ", len(unique_authors))

# generate a list of IDs coupled to each unique name
authors_coupled_ID_list = []
for k in all_authors:
	name_IDs = []
	name_IDs.append(k)
	for i, j in enumerate(all_authors_repeated):
		if j == k:
			# print authors IDs
			print(k, " -> ID: ", all_AU_ID_repeated[i])
			name_IDs.append(all_AU_ID_repeated[i])
	authors_coupled_ID_list.append(name_IDs)

# count number of unique IDs for each name
authors_more_than_1_ID = []
print("Below are all authors unique names with more than 1 ID:")
for i in authors_coupled_ID_list:
	elements = list(Counter(i).keys()) # equals to list(set(words))
	frequency = list(Counter(i).values()) # counts the elements' frequency
	if len(elements) > 2:
		print("Author ", elements[0], " has ", len(elements) - 1, "IDs: ", elements[1:len(elements)])
		authors_more_than_1_ID.append(elements)
		#print("Author's IDs: ", list(elements))
		#print("Element count: ", list(frequency))
# write csv file with authors_more_than_1_ID
  
with open('authors_with_multiple_IDs.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerows(authors_more_than_1_ID)
