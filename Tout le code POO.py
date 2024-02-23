class Voiture:
    def __init__(self, nom,  v_max, zero_cent, conduite):
        self.nom = nom
        self.v_max = v_max
        self.zero_cent = zero_cent
        self.conduite = conduite
        
    def getNom(self):
        return self.nom

    def getVmax(self):
        return self.v_max

    def getZeroCent(self):
        return self.zero_cent

    def getConduite(self):
        return self.conduite

    
    











voit1 = Voiture("Aston Martin DBS Zagato" , "200", "3", "92")

print(voit1.getNom(), voit1.getVmax(), voit1.getZeroCent(), voit1.getConduite())



