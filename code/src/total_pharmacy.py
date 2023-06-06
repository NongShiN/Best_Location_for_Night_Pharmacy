import pandas as pd

def preprocess(df):
    # 현재 영업중이 아닌 약국은 drop
    idx = df[df['영업상태명'] == '폐업'].index
    df.drop(idx, inplace=True)

    idx = df[df['영업상태명'] == '제외/삭제/전출'].index
    df.drop(idx, inplace=True)

    idx = df[df['영업상태명'] == '취소/말소/만료/정지/중지'].index
    df.drop(idx, inplace=True)

    idx = df[df['영업상태명'] == '휴업'].index
    df.drop(idx, inplace=True)

    # dataframe 재구성
    df_1 = pd.DataFrame({'id': df['관리번호'], '약국명': df['사업장명'],'상세주소':df['도로명주소'], '위도':df['위도'], '경도':df['경도']})


    # 정상 영업중이지만 주소가 없는곳은 '김상돈 약국' 단 1곳 뿐이다 따라서 이는 직접 찾아서 추가해준다
    df_1.loc[df_1.약국명=='김상돈약국','상세주소'] = '서울특별시 용산구 독서당로 76'
    df_1.loc[df_1.약국명=='김상돈약국','위도'] = 37.5338823
    df_1.loc[df_1.약국명=='김상돈약국','경도'] = 127.0090525

    return df_1
	