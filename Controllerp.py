class Controllerp:
    def __init__(self, Kp,Sp):
        self.Kp = Kp
        self.Sp = Sp

    def proportional(self,PV):
        MV = self.Kp * (self.Sp - PV)
        return MV