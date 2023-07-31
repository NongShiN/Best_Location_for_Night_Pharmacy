<p align="center"><img margin="Auto" width="1200" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/5dd49e0c-767e-4b59-b694-00fd529e1f10"></p>

## 1️⃣ Introduction

### 1) Background
- 의약분업 이후 의료취약시간대 환자접근성의 제고가 필요합니다. 
2000년 7월에 실시된 의약분업 이후 대부분의 약국이 병원의 진료시간에 맞추어 운영합니다. 이로인해 심야 및 휴일등의 의료 취약 시간대 의약품 이용에 어려움이 발생합니다. 

- 안전 상비 의약품의 환자 안전 문제가 있습니다. 의약품 접근성 향상을 위해 안전 상비의약품 제도가 도입되었으나 전문 지식이 없는 환자가 스스로 의약품을 선택 하면서 약물의 오남용 등 환자 안전에 위협이 되는 문제가 제기되었습니다. 

- 응급의료 서비스 효율성 제고가 필요합니다. 
야간이나 공휴일의 보건의료서비스 공백으로 인한 비응급 경증 환자의 응급의료 서비스의 이용률을 높여 건강보험의 비 효율적 사용이 증가하고 있습니다.

<p align="center"><img margin="Auto" width="600" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/94630ca8-d1c5-4386-bb15-0d5bc3aa9ae8"></p>



### 2) Project Objective
<p align="center"><img margin="Auto" width="600" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/fcf8f388-1c29-4a5b-beda-e6c5546e4209"></p>

- 서울시 야간 약국 데이터 정제 및 전처리 과정 -> 변수 선정 및 데이터 결합 -> 총점 계산 및 최적입지 선정 시각화의 분석 프로세스 단계를 통해 야간약국의 확대와 지역별 균형을 고려하여 서울시 공공 야간약국의 최적입지를 도출 해보았습니다.

---

## 2️⃣ Service Architecture

### 1) Project Tree

```
📦Best_Location_for_Night_Pharmacy
├─ 📂code
│  ├─ 📂src
│  │   ├─ 📜change_address.py
│  │   ├─ 📜convenience_store.py
│  │   ├─ 📜emergency.py
│  │   ├─ 📜night_pharmacy.py
│  │   ├─ 📜police_office.py
│  │   └─ 📜total_pharmacy.py
│  ├─ 📜cal_total_score.py
│  ├─ 📜preprocess.py
│  └─ 📜최적입지선정결과_TOP5_시각화.ipynb
├─ 📂data
│  ├─ 📂raw_data
│  │  ├─ 📜convenience_store.csv
│  │  ├─ 📜emergency_room.csv
│  │  ├─ 📜night_pharmacy.csv
│  │  ├─ 📜police_office.csv
│  │  └─ 📜total_pharmacy.csv
│  ├─ 📂shp
│  │  ├─ 📂tl_emd_seoul_4326_읍면동
│  │  ├─ 📂고령
│  │  ├─ 📂유소년
│  │  ├─ 📂유아
│  │  └─ 📂총인구 격자 1km
│  ├─ 📜convenience_store_preprocessed.csv
│  ├─ 📜emergency_room_preprocessed.csv
│  ├─ 📜night_pharmacy_preprocessed.csv
│  ├─ 📜police_office_preprocessed.csv
│  ├─ 📜total_pharmacy_preprocessed.csv
│  ├─ 📜total_preprocessed.csv
│  ├─ 📜격자별_위도경도.csv
│  └─ 📜최종순위결과.csv
├─ 📂visualize
│  ├─ 📜결과 순위 시각화.qgz
│  ├─ 📜시울시 전체 1km 격자.qgz
│  └─ 📜현황 시각.qgz
├─ 📜서울시-공공-야간약국-활성화를-위한-최적입지-선정 최종본.pdf
└─ 📜README.md
```

### 2) Service Overview
<p align="center"><img margin="Auto" width="1067" src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/5f30996b-8dfb-49e5-a375-e916e7e0fb0d"></p>


1. 웹 서비스가 시작되면 웹 페이지에 시작 화면이 전시됩니다.
2. 사용자는 서비스의 [START] 버튼을 클릭하면 사용자 정보 입력 페이지로 이동합니다.
3. 사용자는 나이, 선호 장르, 보유중인 게임 장비, 해봤던 게임 등 사용자 정보를 입력합니다.
4. 해당 정보는 FastAPI를 통해 Modeling Component에 전달됩니다.
5. Modeling 모듈에서는 사용자 정보 전처리 → 기존 유저와의 유사도 분석 → 새로운 유저의 추천 목록 생성 → 사용자 정보를 통한 필터링을 수행합니다.
6. 필터링된 추천 아이템 목록은 FastAPI를 통해 웹 서비스로 전송됩니다.
7. 서비스는 데이터 저장소로부터 추천 아이템 ID 목록에 해당하는 URL과 제품 image, 장르 정보를 추출하여 웹 페이지에 전시합니다.

---

## 3️⃣ DataSet

### 1) 데이터셋 수집

- 1차 : Metacritic 사이트의 games this year (2000년 ~ 2023년) 데이터 크롤링
    - https://www.metacritic.com/browse/games/score/metascore/year/all/filtered
- 2차 : 1차배포의 피드백을 통한 부족한 게임들을 직접 DB에 추가

### 2) Database ERD
<p align="center"><img margin="Auto" width="800" src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/99057a5a-6a73-40a0-a7c1-c9efd97a265c"></p>

- 게임 이름을 id로 나타내는 column을 전체 테이블의 Primary Key로 설정
- Game table에 앞서 메타 크리틱을 통해 수집한 게임들의 데이터를 저장
- CB 모델 table에는 GPT 모델을 이용하여 구한 게임 태그 데이터가 포함되며 이는 content based model로 제품을 추천할 때 사용
- 각 게임에 리뷰를 남긴 유저들의 리뷰 게임 목록을 수집하여 각 유저들과 게임 이름을 인덱스화 하여 각각 cf_model 테이블, user 테이블에 저장
- 당장의 구현 과정에서는 사용하지 않지만 추후 서비스 고도화에 사용할 수 있는 정보들은 따로 details 테이블에 저장
- 사용자 입력을 user_info에 입력에 대한 각 모델별 output을 gpt_output, hb_model_output에 사용자 피드백을 final_feedback에 저장
- 위의 데이터는 예외 상황 파악 및 처리, 모델 학습 및 개선을 위한 데이터 수집을 위해 저장


---

## 4️⃣ Modeling
### 1) Flow Chart
<p align="center"><img margin="Auto" width="900" src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/c48fe21b-1a14-48b9-9a91-0043fdbb6ab1"></p>
<p align="center"><img margin="Auto" width="900" src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/1ac25c93-d725-48b2-ada8-54f5688437d8"></p>

### 2) Model Selection
<p align="center"><img margin="Auto" width="700" src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/cc0851d6-4b25-4d89-bb01-9114162b7ef7"></p>

- 한정된 시간안에 여러가지 다양한 모델을 실험해보기 위해 Recbole 라이브러를 사용
- 우리가 수집한 유저들의 게임로그 데이터의 sparsity는 99.6%로 매우 높았는데, sparse한 데이터와 cold start problem에 특히 강한 Ease 모델이 단일모델 기준 성능이 가장 좋았음
- 결과적으로, Ease를 베이스라인모델로 정하고, 다양한 모델을 결합한 하이브리드 모델을 구상
   
### 3) Model Train

- 수집한 유저 게임로그 데이터를 8:2 비율로 train-test set으로 split
- train set 으로는 모델을 학습시키고, test set에서는 무작위로 masking을 진행 한 뒤 이를 모델이 예측하는 방식으로 성능평가를 진행
- 성능지표는 precision@5, recall@5를 사용

### 4) Collaborate Filtering
- Ease 모델을 통해 사전 수집된 유저들의 추천 결과를 도출
- 이후 새로운 유저가 들어오면 Collaborative Filtering을 통해 사용자들 간의 유사도를 계산하고, 새로운 유저와 유사한 이전 사용자들을 필터링

### 5) Content Based Filtering
- Collaborative Filtering 을 통해 만들어진 추천리스트를 Content-based Filtering을 사용하여 사용자가 선호할 만한 아이템을 필터링

### 6) GPT-3.5-turbo-Model
<p align="center"><img margin="Auto" width="900" src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/03285f7e-a933-4d06-94a1-188ff63dc68c"></p>

- 대화형 인터페이스를 활용한 GPT 프롬포트를 통해 사용자의 입력에 따른 게임 추천 모델로서 활용

---

## 5️⃣Product Serving

### 1) Workflow
<p align="center"><img margin="Auto" width="900" src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/ecd96ad0-8633-4af9-8083-ed0100a21b4c"></p>

### 2) FrontEnd

- 사용자 데이터 입력 : 나이, 플랫폼, 선호 장르, 태그, 했던 게임 등
- 게임 추천 결과 출력 : 게임 이름, 플랫폼, 메인 장르, url 등

### 3) BackEnd (FastAPI)

- 웹 서버와 모델 서버로 구성 
- 웹 서버에서 Frontend로부터 사용자 정보를 수신하여 모델 서버에 Request 전송
- 웹 서버에서 모델 서버로부터 Response를 받아 Frontend로 전송

### 4) github-action

- github에 코드 push되면 모델과 웹 서버에 배포 자동화

### 5) redis

- 모델 서버에서의 inference 시간 단축을 위하여 캐시 서버인 redis 서버 사용

### 6) DB

- Frontend의 자동 완성 기능에 사용할 전체 게임 목록 생성
- 모델 서버에서 받은 추천 게임 id 목록을 토대로 Frontend에 제공할 게임 정보 검색
- Frontend로부터 받은 사용자 입력, 모델 서버로부터 받은 모델 출력과 Frontend로부터 받은 사용자 피드백을 저장

---

## 6️⃣ **How to Run**

### run web(local)

```
cd Backend/web/
poetry shell
poetry install
pip install python-multipart
python app.py
```

### run model server(local)

```
cd Backend/backend_model/
poetry shell
poetry install
exit
make run
```

#### You need to make 4 server(Model, Web, DB, Redis)

#### You need to install [Docker](https://docs.docker.com/engine/install/) at model and Web server

## 7️⃣ **Demo (시연 영상)**

<p align="center"><img src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/87e0c1d3-7c6c-4ed9-b0d2-8b61122e16a9"></p>


## 8️⃣ Reference

- 자동완성: https://gurtn.tistory.com/212
- Metacritic API: https://github.com/melroy89/metacritic_api
- cookiecutter-fastapi-template: https://github.com/arthurhenrique/cookiecutter-fastapi

## 9️⃣ 팀원 소개


&nbsp;

<table align="center">
  <tr height="155px">
    <td align="center" width="150px">
      <a href="https://github.com/asdftyui"><img src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/62365068-052d-4504-98d0-6dfbe1391e73"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/daream2"><img src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/f4ce270c-4641-4839-b645-bfb71e1c21e4"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/NongShiN"><img src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/d4aa43e0-7591-4d2b-88d4-c0de30c95d29"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/HeewonKwak"><img src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/fec01eb2-0d04-4e70-a5c9-8b9eff745103"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/heeManLee"><img src="https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-09/assets/44831566/ce2579db-d79c-475d-8b60-7b9d759a2ce5"/></a>
    </td>
  </tr>
  <tr height="50px">
    <td align="center" width="150px">
      <a href="https://github.com/asdftyui">김현정_T5070</a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/daream2">민현지_T5078</a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/NongShiN">황찬웅_T5232</a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/HeewonKwak">곽희원_T5015</a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/heeManLee">이희만_T5169</a>
    </td>
  </tr>
  </tr>
  <tr height="80px">
    <td align="center" width="150px">
      <a>Web Server</a>
    </td>
    <td align="center" width="150px">
      <a>Front End / PM</a>
    </td>
    <td align="center" width="150px">
      <a>Model Enginnering</a>
    </td>
    <td align="center" width="150px">
      <a>Model Server</a>
    </td>
    <td align="center" width="150px">
      <a>Data Enginnering</a>
    </td>
  </tr>
</table>
&nbsp;
