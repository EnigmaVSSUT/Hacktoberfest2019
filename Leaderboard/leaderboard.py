import pandas as pd
from datetime import date,datetime
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class Leaderboard:
    '''
    To maintain the leaderboard of the models
    '''
    def __init__(self):
        pass
    def plot(self):
        '''
        Plot model accuracy vs time according to the rank
        in the leaderboard.
        '''
        df = pd.read_excel('op_lbd.xlsx', index_col=0)
        df1 = df.loc[df['SOTA'] == False]
        df = df.loc[df['SOTA'] == True]
        # df = df.drop_duplicates('Rank')
        plt.plot(df['Date'], df['Accuracy'], '.-')
        plt.plot(df1['Date'], df1['Accuracy'], 'co')
        plt.show()

    def leaderboardPush(self, model_name, accuracy, n_params):
        '''
        This will push a new model to the leaderboard.
        @param model_name : Name of the model
        @param accuracy   : Accuracy of the model
        @param n_param    : Nos of parameter of the model

        @returns          : None      
        '''
        assert accuracy > 0.0 , "Accuracy can't be negetive"
        assert accuracy < 100.0, "Accuracy can't be greater than 100.0%"
        assert n_params > 0, "Number of parameters can't be zero or less"
        assert type(n_params) == int, "Number of parameters can't be fraction"
        
        items = {
            "Model_name": model_name,
            "Accuracy"  : accuracy,
            "Parameters": n_params,
            "Date"      : date.today(),
            "SOTA"      : False
        }
        df = pd.read_excel('lbd.xlsx', index_col=0)
        sota = df.Accuracy.max()
        if accuracy > sota:
            items["SOTA"] = True
        df = df.append(items, ignore_index=True)
        df.to_excel('lbd.xlsx')
        df['Rank'] = df['Accuracy'].rank(ascending=False, method='min')
        df = df.sort_values('Rank', ascending=True)

        #Remove this after in the PC
        print(df)
        df.to_excel('op_lbd.xlsx')

        return