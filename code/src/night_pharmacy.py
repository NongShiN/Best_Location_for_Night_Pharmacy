from src.change_address import address_to_latlon
import pandas as pd

def preprocess(df):
# 데이터 출처: https://news.seoul.go.kr/welfare/archives/522756
    #####Dataframe만들기######
    address_df = pd.DataFrame({'약국명': df['약국명'],'상세주소':df['소재지']})

    # 해당 도로명 주소의 위도, 경도 추가

    latitude, longitude = address_to_latlon(address_df['상세주소'])

    address_df['위도'] = latitude
    address_df['경도'] = longitude

    # 구이름 추가
    address_df['구이름'] = address_df['상세주소'].apply(lambda x: x.split(' ')[1])

    return address_df