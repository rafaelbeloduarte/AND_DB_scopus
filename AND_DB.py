import pyreadr

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
			print(i, "repeats at position ", j)
			author_name_repeat_count[i] = author_name_repeat_count[i] + 1

print(author_name_repeat_count)


