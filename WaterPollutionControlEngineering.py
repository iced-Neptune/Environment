class BOD:
    def __init__(self, T,t, BOD_T_t, k1_20):
        self.T = T
        self.t = t
        self.BOD_T_t = BOD_T_t
        self.k1_20 = k1_20
        self.k1_T = 0
        self.La_T = 0
        self.La_20 = 0


    def get_k1_t(self):
        if 10 <= self.T and self.T <= 30 :
            self.k1_T = round(self.k1_20 * 1.047 ** (self.T-20),4)
            return self.k1_T
        else:
            return 0

    def get_La_t(self):
        self.La_T = round(self.BOD_T_t / (1-10**(-self.get_k1_t()*self.t)),2)
        return self.La_T
    
    def get_La_20(self):
        self.La_20 = round(self.get_La_t() / (0.02*self.T+0.6),2)
        return self.La_20
    

while True:  
    list = input('输入T t BOD_T_t k1_20 空格分隔')
    list = list.split()
    T = float(list[0])
    t = float(list[1])
    BOD_T_t = float(list[2])
    k1_20 = float(list[3])

    A = BOD(T,t,BOD_T_t,k1_20)

    print("k1_t = ",A.get_k1_t())

    print("La_t = ",A.get_La_t())
    print("La_20 = ",A.get_La_20())
