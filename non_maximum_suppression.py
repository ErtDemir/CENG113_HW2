#Student ID: 260201059
import math
def calcIntersectionCircles(Ax,Ay,Bx,By,radius):
    distance = (((Bx-Ax)**2 )+ (((By-Ay)**2)))**0.5
    if distance >= 2*radius :
        return(0)
    else:
        x = distance/2
        y = ((radius**2)-(x**2))**0.5
        theta = math.degrees(math.acos(x/radius))
        areaC = (theta/360)* math.pi *(radius**2)
        areaT = x*y/2
        area = 4*(areaC - areaT)
        return(area)

while True :
    circle = []
    circles = []
    strongCircles = []
    weakCircles = []
    noOverlapCircles = []
    eliminatedCircles = []
    absoluteCircles = []
    print("Menu:")
    print("[1] Two circles")
    print("[2] Many circles")
    print("[3] Exit program")
    option = input("Please enter an option:")
##############################
    if option == "1" :
        radius = float(input("Enter Radius:"))
        A =input("Enter First Circle(seperate by space):").split(" ")
        B =input("Enter Second Circle(seperate by space):").split(" ")
        Ax,Ay,Bx,By = float(A[0]),float(A[1]),float(B[0]),float(B[1])
        if radius > 0 :
            intersectionArea = calcIntersectionCircles(Ax,Ay,Bx,By,radius)
            Union = (2*math.pi * radius**2) - intersectionArea
            intersectionOverUnion = (intersectionArea/Union)*100
            print("Intersection Area:",intersectionArea,"\nUnion:",Union,"\nIntersection Over Union:",intersectionOverUnion,"%")
        else: print("Radius must be positive")
##############################################
    elif option == "2" :
        radius = float(input("Enter Radius:"))
        numCircles = int(input("Enter the number of circles:"))
        for i in range(numCircles):
            circle=input("Enter Circle"+str(i)+"(seperate by space):").split(" ")
            circles.append(circle)
        threshold = float(input("Enter threshold:"))
        for j in range(len(circles)-1):
            for l in range(j+1 , len(circles)):
                A , B = circles[j] , circles[l]
                intersectionArea = calcIntersectionCircles(float(A[0]),float(A[1]),float(B[0]),float(B[1]),radius)
                Union = (2*math.pi * radius**2) - intersectionArea
                intersectionOverUnion = intersectionArea/Union*100
                if intersectionOverUnion >= (threshold*100) : 
                    strongCircles.append([j,l])
                elif intersectionOverUnion < (threshold*100) and intersectionOverUnion != 0 : 
                    weakCircles.append([j,l])
                elif intersectionOverUnion == 0: 
                    noOverlapCircles.append([j,l])            
                if [j,l] in strongCircles: 
                    print(j,"and",l,": strong overlap") 
                elif [j,l] in weakCircles: 
                    print(j,"and",l,": weak overlap") 
                elif [j,l] in noOverlapCircles: 
                    print(j,"and",l,":no overlap")
        ####### Overlap found up there
        for m in strongCircles:
            if m == strongCircles[0]:
                absoluteCircles.append(m[0])
                eliminatedCircles.append(m[1])
                continue
            if m[0] in eliminatedCircles:
                if m[1] not in eliminatedCircles:
                    absoluteCircles.append(m[1])
            elif m[0] not in eliminatedCircles:
                eliminatedCircles.append(m[1])
        for n in weakCircles:
            if n[0] not in eliminatedCircles:
                absoluteCircles.append(n[0])
            if n[1] not in eliminatedCircles:
                absoluteCircles.append(n[1])
        for o in noOverlapCircles:
            if o[0] not in eliminatedCircles:
                absoluteCircles.append(o[0])
            if o[1] not in eliminatedCircles:
                absoluteCircles.append(o[1])
        for p in (set(absoluteCircles)):
            print(p)
##############################################
    elif option == "3" : 
        break
    else:
        print("Invalid option")
    input("Please enter to continue.")
