import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
land = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    land.append((land_x, land_y))
for i in range(len(land)-1):
    if land[i][1] == land[i+1][1]:
        flatland = [land[i], land[i+1]] # [(4000, 150), (5500, 150)]
landingspot = ((flatland[0][0]+flatland[1][0])//2, flatland[0][1]) # (4750, 150)
# game loop
down = True
time = 0

while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    realinput = [i for i in input().split()]
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in realinput]

    distance = x-landingspot[0]
    altitude = y-landingspot[1]
    direction = 1 if distance < 0 else -1
    # enoughheight = 2 if (y-landingspot[0]) > 500 else 1
    # rotate = direction*15*enoughheight
    # if x != landingspot[0]:
    #     if abs(distance)> 500:
    #         if h_speed>30:
    #             rotation = rotate*-1
    #         else:
    #             rotation = rotate
    #     else:
    #         if h_speed > 0:
    #             rotation = rotate*-1
    #         else:
    #             rotation = rotate

    hspeed = abs(distance)/85
    hratio = abs(h_speed/hspeed)
    if hratio > 1:
        rotate = 90*hratio-90
        print("1", rotate, file=sys.stderr, flush=True)
        if rotate > 90:
            rotate = 90
    else: 
        rotate = 180*hratio-180
        print(rotate, file=sys.stderr, flush=True)

        if rotate < -90:
            rotate = -90
    rotation = int(direction*rotate)
    
    if y > 2700:
        thrust = 3
    else: thrust = 4
    if v_speed < -20:
        rotation = int(rotation/3)
    if altitude < 100:
        rotation = 0
    # if y <2000:
    #     down = False
    # if down: thrust = 3
    # else: thrust = 4
    # thrust = 4
    # rotation = 0
    # time += 1
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(hspeed, h_speed, hratio, rotate, distance, rotation, file=sys.stderr, flush=True)

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(rotation, thrust)

###############################
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
surface = []
surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    landx, landy = [int(j) for j in input().split()]
    surface.append((landx, landy))

### FINDING THE MIDDLE POINT OF THE FLAT SURFACE TO LAND
flatsurface = []
for i in range(len(surface)-1):
    if surface[i][1] == surface[i+1][1]:
        flatsurface.append(surface[i])
        flatsurface.append(surface[i+1]) # in the first test case it is [(4000, 150), (5500, 150)]
landingspot = ((flatsurface[0][0] + flatsurface [1][0])//2, flatsurface[0][1]) # in the first test case it is (4750, 150)
print(landingspot, file = sys.stderr, flush = True)
# game loop
while True:
    x, y, hspeed, vspeed, fuel, rotate, power = [int(i) for i in input().split()]
    if x - 200 < landingspot[0] and x + 200 > landingspot[0]


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(-10, 4)