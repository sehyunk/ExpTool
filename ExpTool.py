import numpy as np
import pandas as pd
from tqdm import tqdm

from scipy.stats import norm , binom_test

def exp_result(df, cl = 0.95, su = 100):
    result = pd.DataFrame()
    z = norm.ppf(1-(1-cl)/2)

    for n in tqdm(range(su,df.shape[0], su)):
        group_a = df.iloc[:n,:].loc[df.iloc[:n,:].group == 'a', ['sample_id', 'converted']]
        group_b = df.iloc[:n,:].loc[df.iloc[:n,:].group == 'b', ['sample_id', 'converted']]

        n_a = group_a.shape[0]
        n_b = group_b.shape[0]
        p_a = group_a.converted.sum()/n_a
        p_b = group_b.converted.sum()/n_b

        uplift = p_b - p_a

        # Margin of Error
        me = z*df.iloc[:n,:].converted.std()/np.sqrt(n_a + n_b)
        # Confidence Interval
        ci = [uplift-me, uplift+me]
        # P value
        p_value = binom_test(group_b.converted.sum(),n_b,p_a)
        # Statistical significance
        stat_sig = p_value <= (1-cl)

        result.loc[n, 'uplift'] = uplift
        result.loc[n, 'ci_low'] = ci[0]
        result.loc[n, 'ci_high'] = ci[1]
        result.loc[n, 'p_value'] = p_value
        result.loc[n, 'stat_sig'] = stat_sig

    print(f'''
    [CL: {round(cl,3)}]
    +-------------------+
    |   |a      |b      |
    +-------------------+
    |n  |{n_a}  |{n_b}  |
    |p  |{round(p_a,4)} |{round(p_b,4)} |
    +-------------------+
    - Uplift: {round(uplift,4)}
    - Confidence Interval: {round(ci[0],4)} to {round(ci[1],4)}
    - P value: {round(p_value,2)}
    - Statistical significance: {stat_sig}
    ''')
    
    return result

class Vexp:
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
