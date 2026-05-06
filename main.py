from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

niye_jao = RideSharing('Niye Jao')
rohim = Rider("Rohim uddin", 'rahim@gmail.com' , 25416564, "Mohakhali", 1200)
niye_jao.add_rider(rohim)
kolim = Driver("Kolim uddin", 'kolim@gmail.com', 163421, 'Gulshan')
niye_jao.add_driver(kolim)


print(niye_jao)