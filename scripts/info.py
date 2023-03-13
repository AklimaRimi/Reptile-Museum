import pandas as pd

# df = pd.read_csv('data/Reptil.csv')
# print(df.columns)

# cols = ['Name', 'Scientific_Name', 'Conservation_Status', 'habitat', 'Color',
#        'Found_In', 'Diet', 'Species']

# data = []
# for col in cols:
#     li = df[col].unique()
#     for l in li:
#         data.append([col,l])
        
# data = pd.DataFrame(data,columns=['columns','values'])
# data.to_csv('data/info.csv',index=False)
    
    
df = pd.read_csv('data/info.csv')

arr = ['Species','Scientific_Name','Name','Conservation_Status','Color','habitat','Found_In','Diet']
vals = ['','','','','','','','']
pred = ['Acrantophis madagascariensis', 'Carnivore', 'Critically Endangered', 'Forest', 'Gray', 'Madagascar', 'Madagascar ground boa ', 'Snake']
for x in pred:
    val = df[df['values'] == x]['columns'].values[0]
    ind = arr.index(val)
    print(ind)
    vals[ind] = x
    
print(vals)