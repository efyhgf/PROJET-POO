class Voiture:
    def __init__(self, v_max, zero_cent, conduite):
        self.v_max = v_max
        self.zero_cent = zero_cent
        self.conduite = conduite
        
    def DireQuelquechose(self, conduite):
        print("J'ai", self.conduite, "de conduite !")







voit1 = Voiture("200", "3", "92")

voit1.DireQuelquechose()

