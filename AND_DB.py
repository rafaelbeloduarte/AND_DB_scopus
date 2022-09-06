import pyreadr

result = pyreadr.read_r('/run/media/rafael/Dados_ext4/Mega2/uem/Mestrado/Dissertação/análise_bibliométrica/python_author_name_disambiguation/Bibliometrix-Export-File-2022-09-06.RData') # also works for Rds

# done! let's see what we got
# result is a dictionary where keys are the name of objects and the values python
# objects
#print(result.keys()) # let's check what objects we got
M = result["M"] # extract the pandas data frame for object M

#print(M.AU)

# criando uma lista com todos os autores
todos_autores_repetidos = []
todos_AU_ID_repetidos = []

# objeto author ID
AU_ID = getattr(M, 'Author.s..ID')
# print(AU_ID)

for i in range(len(M.AU)):
	autores_tmp = []
	AU_ID_tmp = []
	
	autores_tmp = M.AU[i]
	AU_ID_tmp = AU_ID[i]
	
	autores_tmp = autores_tmp.split(";")
	AU_ID_tmp = AU_ID_tmp.split(";")
	#print(AU_ID_tmp)
	#print(autores_tmp)
	for j in range(len(autores_tmp)):
		todos_autores_repetidos.append(autores_tmp[j])
	for j in range(len(AU_ID_tmp)):
		todos_AU_ID_repetidos.append(AU_ID_tmp[j])
#print(i+1, " linhas")

#print(todos_autores_repetidos)
#print(len(todos_autores_repetidos))

# Python 3 code to demonstrate
# removing duplicate elements from the list
todos_autores = [*set(todos_autores_repetidos)]
todos_AU_ID = [*set(todos_AU_ID_repetidos)]
todos_AU_ID.remove('')
#print("List after removing duplicate elements: ", todos_autores)
print("Quantidade de autores: ", len(todos_autores))
print("Quantidade de IDs: ", len(todos_AU_ID))


