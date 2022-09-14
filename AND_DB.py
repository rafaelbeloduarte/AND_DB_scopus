import pyreadr
from collections import Counter
from pybliometrics.scopus import AuthorRetrieval
import csv

# result is a dictionary where keys are the name of objects and the values python
# objects
result = pyreadr.read_r('Bibliometrix-Export-File-2022-09-06.RData') # also works for Rds
M = result["M"] # extract the pandas data frame for object M

# initialize lists of all authors names and IDs
all_authors_repeated = []
all_AU_ID_repeated = []

# get author ID objetc
AU_ID = getattr(M, 'Author.s..ID')

# create lists of IDs and authors in the order of appearance
for i in range(len(M)):
	authors_tmp = []
	AU_ID_tmp = []
	
	authors_tmp = M.AU[i]
	AU_ID_tmp = AU_ID[i]
	
	authors_tmp = authors_tmp.split(";")
	AU_ID_tmp = AU_ID_tmp.split(";")
	
	for j in range(len(authors_tmp)):
		all_authors_repeated.append(authors_tmp[j])
	for j in range(len(AU_ID_tmp)):
		all_AU_ID_repeated.append(AU_ID_tmp[j])

# filtering empty items
temp_list = all_AU_ID_repeated
all_AU_ID_repeated = list(filter(None, temp_list))

temp_list = all_authors_repeated
all_authors_repeated = list(filter(None, temp_list))

print("Authors string count: ", len(all_authors_repeated))
print("Authors IDs count: ", len(all_AU_ID_repeated))

# removing duplicate elements from the list
all_authors = [*set(all_authors_repeated)]
todos_AU_ID = [*set(all_AU_ID_repeated)]

print("Total unique author strings: ", len(all_authors))
print("Total unique IDs: ", len(todos_AU_ID))

# creating a list to count all the times a name repeats
author_name_repeat_count = [0] * len(all_authors)

for i in range(len(all_authors)):
	for j in range(len(all_authors_repeated)):
		if all_authors[i] in all_authors_repeated[j]:
			# print(all_authors[i], "repeats at position ", j)
			author_name_repeat_count[i] = author_name_repeat_count[i] + 1

# creating a list of authors that appear more than once in the data set
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
			# print(k, " -> ID: ", all_AU_ID_repeated[i])
			name_IDs.append(all_AU_ID_repeated[i])
	authors_coupled_ID_list.append(name_IDs)

# count number of unique IDs for each name
authors_more_than_1_ID = []
# print("Below are all authors unique names with more than 1 ID:")
f = open("authors_with_multiple_IDs.csv", "w")
for i in authors_coupled_ID_list:
	elements = list(Counter(i).keys()) # equals to list(set(words))
	frequency = list(Counter(i).values()) # counts the elements' frequency
	if len(elements) > 2:
		# print("Author ", elements[0], " has ", len(elements) - 1, "IDs: ", elements[1:len(elements)])
		#print(elements)
		#print("Author's IDs: ", list(elements))
		#print("Element count: ", list(frequency))
		name = "\n" + elements[0] + ";"
		f.write(name)
		for j in range(1,len(elements)):
			some_author = AuthorRetrieval(elements[j])
			#information = ";" + elements[j] + ";" + some_author.surname + ", " + some_author.given_name + "; Publication range: " + str(some_author.publication_range) + " Orcid: " + str(some_author.orcid) + " Date created: " + str(some_author.date_created)
			information = ";" + elements[j] + ";" + some_author.surname + ", " + some_author.given_name
			f.write(information)
f.close()
