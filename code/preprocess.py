from src import convenience_store, emergency, night_pharmacy, police_office, total_pharmacy
import pandas as pd

DATA_PATH = '../data/'

name_dict = {'convenience_store':'cp949', 'emergency_room':'cp949', 'police_office':'cp949',
            'night_pharmacy':'UTF-8-sig', 'total_pharmacy':'cp949'}
    
function_arr = [convenience_store, emergency, police_office, night_pharmacy, total_pharmacy]
print("*"*19 + ' Stat Preprocess!! ' + "*"*18)

#for k, v, func in zip(name_dict), function_arr):
for k, func in zip(name_dict, function_arr):
    print("*"*20 + ' '+ k + ' '+ "*"*20)
    print("*"*23 + ' Load Data ' + "*"*22)
    df = pd.read_csv(DATA_PATH + 'raw_data/' + k + '.csv', encoding = name_dict[k])
        
    df = func.preprocess(df)
        
    print("*"*19 + ' Save preprocessed ' + "*"*18)
    df.to_csv(DATA_PATH + k + '_preprocessed.csv', encoding = name_dict[k], index = False)
        
    print("*"*25 + ' Done ' + "*"*25)
    print()

print("All Done!!")

