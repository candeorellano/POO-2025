class Libro:
    __titulo:str
    __autor:str
    __isbn:str
    __genero:str

    def __init__(self, tit, aut, isbn, gen):
        self.__titulo = tit
        self.__autor = aut
        self.__isbn = isbn
        self.__genero = gen
    
    #Getters
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getISBN(self):
        return self.__isbn
    def getGenero(self):
        return self.__genero
    
    def __str__(self):
        return f"Titulo: {self.__titulo} - Autor: {self.__autor} - ISBN: {self.__isbn} - Genero: {self.__genero}"