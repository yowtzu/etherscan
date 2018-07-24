import pandas as pd
import os

folder_name = './data/'
all_files = [ os.path.join(folder_name, file_name) for file_name in os.listdir(folder_name) if file_name.endswith('csv') ]

df_list = [ pd.read_csv(file, thousands=',', index_col=0).iloc[:, -1].rename(file[14:-4]).to_frame() for file in all_files ] 

df = pd.DataFrame(df_list[0])
df.index = pd.to_datetime(df.index)

for df_tmp in df_list[1:]:
    df_tmp.index = pd.to_datetime(df_tmp.index) 
    df = df.join(df_tmp, how='outer')
    
df = df.sort_index()

df.TransactionFee = df.TransactionFee.astype('float')

