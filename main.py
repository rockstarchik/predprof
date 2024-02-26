import csv


def cor(n,m,t,xd,yd) :
    if n <= 5:
        x = -(n+xd) * 4 + t
    if n > 5:
        x = n + xd
    if m > 3:
        y = m + t + yd
    if m <= 3:
        y = -(n+yd) * m
    return x,y


with open("space.txt", encoding="utf8") as file:
    st = list()
    for t in file:
        sp = t.split("*")
        st.append(sp)


with open("space_new.txt","w",newline="") as file2:
    writer = csv.writer(file2)
    s = writer.writerow(st)
    for ShipName, planet, coord_place, direction in st:
        if coord_place == '0 0':
            coord_place = cor(int(ShipName[5]),int(ShipName[6]),len(str(planet)),int(direction[1]),int(direction[2]))

