points = [(1,2),(3,4),(5,6),(7,8),(9,10)]

def euclideanDistance(point1,point2):
    (x1,y1) = point1
    (x2,y2) = point2
    euclideandistance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return euclideandistance

distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        euclideandistance = euclideanDistance(points[i],points[j])
        distances.append(euclideandistance)       
minimumdistance = min(distances)
print("Minimum mesafe:  ", minimumdistance,"'dir.")        




