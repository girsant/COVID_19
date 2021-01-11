from math import sin, cos, atan2, sqrt, radians

# Alta floresta do Oeste
lat1_d = -11.9283
lon1_d = -61.9953

# Rolim de Moura
lat2_d = -11.7271
lon2_d = -61.7714


lat1 = radians(lat1_d)
lon1 = radians(lon1_d)
lat2 = radians(lat2_d)
lon2 = radians(lon2_d)


dlat = lat2-lat1
dlon = lon2-lon1

# Fórmula de Haversine
R = 6373.0 # Raio da terra (km)
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c
print(distance)