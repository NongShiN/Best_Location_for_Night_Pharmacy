import pandas as pd

def preprocess(df):
    # 필요한 colum만 선택 후 적절하게 이름 변경
    df_1 = pd.DataFrame({'id': df['기관ID'], '응급실명': df['기관명'],'상세주소':df['주소'],'위도':df['병원위도'],'경도':df['병원경도']})

    return df_1