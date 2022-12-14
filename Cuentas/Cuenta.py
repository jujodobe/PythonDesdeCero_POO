class Cuenta:

    def __init__(self, id, numero, titular, saldo, limiteSaldo):
        self.__id = id
        self.__Numero = numero
        self.__Titular = titular
        self.__Saldo = saldo
        self.__LimiteSaldo = limiteSaldo

    def getNumero(self):
        return self.__Numero

    def setNumero(self, numero):
        self.__Numero = numero

    def getTitular(self):
        return self.__Titular

    def setTitular(self, titular):
        self.__Titular = titular

    def getSaldo(self):
        return self.__Saldo

    def setSaldo(self, saldo):
        self.__Saldo = saldo

    def getLimite(self):
        return self.__LimiteSaldo

    def setLimite(self, limiteSaldo):
        self.__LimiteSaldo = limiteSaldo

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def extracto(self):
        print("EXTRACTO DE LA CUENTA")
        print(f" Cuenta: {self.__Numero} \n Titular: {self.__Titular} \n saldo: {self.__Saldo}")

    def deposita(self, cantidadValor):
        self.__Saldo += cantidadValor

    def retiro(self, cantidadValor):
        self.__Saldo -= cantidadValor
