from src.change_address import address_to_latlon
def preprocess(df):
    df1 = df[['지방청','관서명','구분','주소']]
    df1.columns = ['지역','경찰서명','구분','상세주소']


    df2 = df1[df1['지역'] == '서울청']


    df2.set_axis([i for i in range(len(df2))],inplace=True)


    df3 = df2[['경찰서명','구분','상세주소']]


    # 해당 도로명 주소의 위도, 경도 추가
    latitude, longitude = address_to_latlon(df3['상세주소'])

    df3['위도'] = latitude
    df3['경도'] = longitude

    return df3