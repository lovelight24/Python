class Mf:
    def __init__(self, name):
        self.name = name

    def schemeName(self):
        print("SchemeName Is "+self.name)


class  Inv(Mf):
    def __init__(self, name, amount):
        Mf.__init__(self, name)
        self.amt = amount


    def Investment(self):
        Mf.schemeName(self)
        print("Your Investment is "+str(self.amt))

a = Inv("Hdfc Tax Saver Fund", 20000)
a.Investment()
