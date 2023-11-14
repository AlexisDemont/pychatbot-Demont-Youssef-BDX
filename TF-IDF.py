from basicsFunctions import list_of_files
def TfIdf(directory='./cleaned/'):
    matrice=[]
    list_files=list_of_files(directory,'.txt')

    for files in list_files:
        matrice.append([])  
        with open(directory+files,'r') as file:
            for line in file:
                for word in line.split():
                    print(word)

