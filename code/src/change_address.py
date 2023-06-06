import re
from geopy.geocoders import Nominatim

# 도로명주소 위도 경도 값으로 바꿔주는 함수
geo_local = Nominatim(user_agent='South Korea')
def geocoding(address): 
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y

    except:
        return [0,0]

def address_to_latlon(address):
    for i in range(len(address)):
        a = address[i].split(' ')
        address[i] = " ".join(a[0:4])
        address[i] = address[i].replace(',','')
        address[i] = re.sub(r'\([^)]*\)', '', address[i])

    # 주소를 위,경도 값으로 변환하기
    latitude = []
    longitude =[]
    for i in address:
        latitude.append(geocoding(i)[0])
        longitude.append(geocoding(i)[1])
    
    return latitude, longitude