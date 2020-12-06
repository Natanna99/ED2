class Tree:
    def __init__(self):
        self.raiz = None
    def insere(self,valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz = self.raiz.insere(valor)
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()
        else:
            return 0

class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
        self.fb = 0

    def insere(self, valor):
        if valor<=self.info:
            if self.esq == None:
                self.esq = No(valor)
                self = self.balancear()
            else:
                self.esq.insere(valor)
                self = self.balancear()
        else:
            if self.dir == None:
                self.dir = No(valor)
                self = self.balancear()
            else:
                self.dir.insere(valor)
                self = self.balancear()
        return self
                
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info,  " | ",self.fb)
        if self.dir != None:
            self.dir.inOrdem()

    def preOrdem(self):
        print(self.info,  " | ",self.fb)
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()

    def alturaLimpa(self, valor):
        if valor != None:
            return valor.altura()
        return 0
   
    def max(self, a, b):
        return (b if b > a else a)

    def altura(self):
        hesq=hdir=0
        if self.esq!=None:
            hesq= self.esq.altura()
        if self.dir!=None:
            hdir= self.dir.altura()
        return 1+max(hesq,hdir)

    def rotacionarParaDireita(self):
        p = self
        q = p.esq
        temp = q.dir
        q.dir = p
        p.esq = temp
        p=q
        return p

    def rotacionarParaEsquerda(self):
        p = self
        q = p.dir
        temp = q.esq
        q.esq = p
        p.dir = temp
        p=q
        return p

    def rebalancear(self):
        if self!=None: self.fb = self.alturaLimpa(self.dir) - self.alturaLimpa(self.esq)
        if self.esq!=None: self.esq.fb = self.esq.alturaLimpa(self.esq.dir) - self.esq.alturaLimpa(self.esq.esq)
        if self.dir!=None: self.dir.fb = self.dir.alturaLimpa(self.dir.dir) - self.dir.alturaLimpa(self.dir.esq)

        return self

    def balancear(self):
        self.fb = self.alturaLimpa(self.dir) - self.alturaLimpa(self.esq)

        if(self.fb == -2 and self.esq.fb == -1):
            self = self.rotacionarParaDireita()
            self = self.rebalancear()

        elif(self.fb == 2 and self.dir.fb == 1):
            self = self.rotacionarParaEsquerda()
            self = self.rebalancear()

        elif(self.fb == -2 and self.esq.fb == 1):
            self.esq = self.esq.rotacionarParaEsquerda()
            self = self.rebalancear()
            self = self.rotacionarParaDireita()
            self = self.rebalancear()
            
        elif(self.fb == 2 and self.dir.fb == -1):
            self.dir = self.dir.rotacionarParaDireita()
            self = self.rebalancear()
            self = self.rotacionarParaEsquerda()
            self = self.rebalancear()

        return self
