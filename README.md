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

## 2️⃣ Project Architecture

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

### 2) Analysis process
<p align="center"><img margin="Auto" width="600" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/b9c53dbb-d5cf-4304-be08-b163688c5787"></p>


#### 1. 서울시 약국 데이터 정제 및 전처리
<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/ea73b1ba-c8ff-451b-87cf-ed87a339bbe9"></p>

#### 2. 변수 선정 및 데이터 결합
<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/5c57162e-b221-4104-88cf-f4e2ab20ea43"></p>
<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/a6cfcf81-27c0-4774-94f8-1780bf2631bf"></p>

#### 3. 변수 데이터 전처리 및 가중치 설정 후 정규화
<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/025e6250-192a-44ef-b8e9-70edb4a7ced3"></p>
<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/70b994ca-e5f7-4ec0-b9fd-c155335ce6ab"></p>
<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/2610a430-1dc0-4703-80c0-b319f27ec7cc"></p>

#### 4. 총점 계산 및 최적입지 선정 시각화
<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/2d7fb870-3cf8-4c50-b952-ec0c4527d766"></p>
<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/8c858839-39d1-4f97-af12-7e081a57963d"></p>

---

## 3️⃣ 분석 결과

![약국 입지선정1](https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/fbc77ebe-cf04-4f7f-ad8e-4bd234571f90)
![약국 입지선정2](https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/3f364383-da4e-4ac7-9750-1c9cf8fcbe32)
![약국 입지선정3](https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/7afc4d94-a3ca-439e-9de5-dea490cc04fc)
![약국 입지선정4](https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/a885e87d-4957-4fac-89a5-3c78e5b725e7)
![약국 입지선정5](https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/87a4dfda-a614-484e-8b49-92af31db2bcd)

## 4️⃣ 활용 방안

### 1) 선제적 분석을 통한 공공 야간약국 활성화

<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/2663b9fc-816a-4eeb-b1ec-ea9721858e13"></p>

- 약국의 자발적 참여에 의존하여 운영 약국 수의 운영 및 유지가 어려운 기존의 체계 극복한다.
- 데이터 분석을 기반으로 국민이 필요로 하는 곳에 공공 야간약국이 선제적으로 마련될 수 있도록 한다.

### 2) 지역별 특성 기반의 홍보를 통한 공공 야간약국 활성화

<p align="center"><img margin="Auto" width="800" src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/bcfe7a10-ed22-4a20-a1ca-6d77ada91090"></p>

---

## 5️⃣ 팀원 소개


&nbsp;

<table align="center">
  <tr height="155px">
    <td align="center" width="150px">
      <a href="https://github.com/asdftyui"><img src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/4b54c480-fdd5-4d57-97cd-e573628eaba1"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/daream2"><img src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/35c667c4-04bc-4bf1-b58d-cac08643b72a"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/NongShiN"><img src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/1aba3dae-51e5-4a3b-9253-67dd2749f9f6"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/HeewonKwak"><img src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/cf65e189-d003-4d45-bf25-c38a984b3a72"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/heeManLee"><img src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/74ecaedc-5b59-4772-8d8a-e90763671018"/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/heeManLee"><img src="https://github.com/NongShiN/Best_Location_for_Night_Pharmacy/assets/44831566/7dbd4321-0561-4fab-8d00-3f9d58658938"/></a>
    </td>
  </tr>
  <tr height="50px">
    <td align="center" width="150px">
      <a href="">이윤서</a>
    </td>
    <td align="center" width="150px">
      <a href="">이재영</a>
    </td>
    <td align="center" width="150px">
      <a href="">진현기</a>
    </td>
    <td align="center" width="150px">
      <a href="">최수인</a>
    </td>
    <td align="center" width="150px">
      <a href="">최승원</a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/NongShiN">황찬웅</a>
    </td>
  </tr>
  </tr>
  <tr height="80px">
    <td align="center" width="150px">
      <a>PM / Imformation Research</a>
    </td>
    <td align="center" width="150px">
      <a>Data Collecting</a>
    </td>
    <td align="center" width="150px">
      <a>Imformation Research</a>
    </td>
    <td align="center" width="150px">
      <a>Presentation</a>
    </td>
    <td align="center" width="150px">
      <a>Project Supporting</a>
    </td>
    <td align="center" width="150px">
      <a>Model Enginnering</a>
    </td>
  </tr>
</table>
&nbsp;
