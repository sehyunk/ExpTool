import numpy as np
from scipy.stats import norm , binom_test

class ExpTool:
    def __init__(self, cl = 0.95, p = 0.5, moe = 0.01):
        self.cl = cl
        self.p = p
        self.moe = moe
        self.z = norm.ppf(1-(1-cl)/2)

        print(f'''
+-------------------------------+
|  Confidence Level:\t{self.cl*100}%\t|
|   Margin of Error:\t{self.moe*100}%\t|
|           z-score:\t{round(self.z,2)}\t|
|                 p:\t{self.p}\t|
+-------------------------------+
''')
    
    def get_n(self):
        n = np.ceil(self.z**2*(self.p*(1-self.p))/self.moe**2)
        return n
    
    def get_pvalue(self, converted, b_count, noti = True):
        pvalue = binom_test(converted, b_count, self.p)
        pvalue_standard = 1-self.cl
        if noti == True:
            if pvalue < 1-self.cl:
                print(f'result: lesser then {round(pvalue_standard,3)} :)')
            else:
                print(f'result: larger then {round(pvalue_standard,3)} :(')
            
        return pvalue
