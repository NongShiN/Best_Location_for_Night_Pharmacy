def preprocess(file):
    # 필요한 colum만 선택 후 적절하게 이름 변경
    re_file = file[['관리번호','영업상태명','도로명주소','사업장명','좌표정보(X)','좌표정보(Y)']]
    re_file.columns = ['id','영업상태','상세주소','약국명','위도','경도']

    # 현재 영업 중이 아닌 편의점 데이터는 drop
    idx = re_file[re_file['영업상태'] == '폐업'].index
    re_file.drop(idx,inplace = True)

    idx1 = re_file[re_file['영업상태'] == '취소/말소/만료/정지/중지'].index
    re_file.drop(idx1,inplace = True)

    idx2 = re_file[re_file['영업상태'] == '휴업'].index
    re_file.drop(idx2,inplace = True)

    #행번호 재세팅
    re_file.set_axis([i for i in range(len(re_file))],inplace=True)

    return re_file