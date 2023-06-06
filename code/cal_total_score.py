import pandas as pd

########### file_name 선언 ##################################
전처리데이터셋 = 'total_preprocessed.csv'
심야약국현황 = 'night_pharmacy_preprocessed.csv'
############################################################
DATA_PATH = '../data/'


df = pd.read_csv(DATA_PATH + f'{전처리데이터셋}', header=0, encoding='cp949', engine='python')

df.drop_duplicates(['gid']) # 구 경계 겹치는 부분 제거

전체칼럼 = df.columns.tolist()


# 구별 심야약국 갯수 파악
df_1 = pd.read_csv(DATA_PATH + f'{심야약국현황}', header=0, encoding='utf-8', engine='python')
dic = {'구이름':[], '가중치':[]}
dic = df_1['구이름'].value_counts()
dic['양천구'] = 0 # 값이 0인 양천구는 value_counts()로 추가되지 않으므로 직접 추가 

# 구별 심야약국 갯수를 기준으로 가중치 설정
df_gu = pd.DataFrame(dic, columns=['구이름','가중치'])

#전처리데이터에 구가중치를 추가
merge = pd.merge(df, df_gu, how='outer',on='구이름')

# 구가중치를 적절하게 조정
merge.rename(columns = {'가중치':'구가중치'},inplace=True)

merge['구가중치'] = (dic.max() - dic.min()) - merge['구가중치']


### 하단에 있는 "점수칼럼"에 점수로 환산할 대상인 칼럼을 수정하도록 함
점수칼럼 =  ['심야약국', '응급실', '상비의약품', '경찰서', '고위험군', '총인구', '구가중치']
가중치 = [1] * len(점수칼럼)


### 건물 가중치 설정
가중치 = [-1,1,1,1,1,1,2]     


### gid를 기준으로 DataFrame sort
df = merge.copy()
df.set_index('gid', inplace=True)
pre_process_set = merge
pre_process_set = pre_process_set.sort_values(by='gid')

# Null 이 있을 수 있는 칼럼은 Null을 0로 변경
pre_process_set.fillna(0, inplace=True)


################## MinMax정규화 ##########################################################################
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

# 점수칼럼 정규화
norm = pre_process_set.copy()
norm.fillna(0, inplace=True)
norm.set_index('gid', inplace=True)

norm[점수칼럼] = scaler.fit_transform(norm.loc[:,점수칼럼])
norm.reset_index(inplace=True)
################## 정규화 끝################################################################################



# 총점 계산
df = norm.copy()

for i in range(0, len(점수칼럼)):
    name = 점수칼럼[i]
    df[name] = df[name] * 가중치[i] 

df['sum'] = df[점수칼럼].sum(1)
df.reset_index(inplace=True)

# 순위 계산 
df['순위'] = df['sum'].rank(method='dense', ascending=False).astype(int)

final = df.sort_values(by='순위')
final.reset_index(drop=True, inplace=True)


# 최종 결과 CSV 파일쓰기
final.to_csv(DATA_PATH + '최종순위결과.csv', index=False, sep=',', encoding='cp949')