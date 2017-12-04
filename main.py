from spirale import Spirale

spirale=Spirale()

for i in range(1, 35):
    #print i, spirale.first(i)
    #print i, spirale.get_position(i)
    #print i, spirale.sector(i)
    print i, spirale.get_position_2(i)

print spirale.get_distance(347991)