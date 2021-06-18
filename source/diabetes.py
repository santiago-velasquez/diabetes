import pandas as pd
import joblib
import numpy as np
import warnings
warnings.simplefilter('ignore')

class Diabetes:

    def __init__(self):
        self.test_data = pd.read_csv('../data/processed/X_test.csv')
        self.model = joblib.load('../models/rf.pkl')
    
    def predict(self, data):
        preds = self.model.predict(data)
        return preds
    
    def main(self):
        print('Params: \n')
        self.get_best_params()
        print('\n__________________________\n')
        preds = self.predict(self.test_data)
        np.savetxt('../data/processed/preds.txt',preds)
        print('File with predictions generated on data/processed')
        print(preds)
    
    def get_best_params(self):
        print(self.model.steps[1][1].get_params())
    
if __name__ == '__main__':
    diabetes = Diabetes()
    diabetes.main()
