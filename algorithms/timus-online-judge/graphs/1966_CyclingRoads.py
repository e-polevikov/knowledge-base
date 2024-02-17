

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(point1, point2, point3):
    slopes_relation = \
          (point2.y - point1.y) * (point3.x - point2.x) \
        - (point3.y - point2.y) * (point2.x - point1.x)

    # collinear
    if slopes_relation == 0:
        return 0
    
    # clockwise / counterclockwise
    if slopes_relation > 0:
        return 1
    else:
        return 2


def inside_segment(point, segment):
    point1, point2 = segment

    min_x, max_x = min(point1.x, point2.x), max(point1.x, point2.x)
    min_y, max_y = min(point1.y, point2.y), max(point1.y, point2.y)

    return min_x < point.x < max_x and min_y < point.y < max_y


def intersect(point1, point2, point3, point4):
    orientation1 = orientation(point1, point2, point3)
    orientation2 = orientation(point1, point2, point4)
    orientation3 = orientation(point3, point4, point1)
    orientation4 = orientation(point3, point4, point2)

    if orientation1 != orientation2 and orientation3 != orientation4:
        return True
    
    if orientation1 == 0 and inside_segment(point3, (point1, point2)):
        return True

    if orientation2 == 0 and inside_segment(point4, (point1, point2)):
        return True

    if orientation3 == 0 and inside_segment(point1, (point3, point4)):
        return True

    if orientation4 == 0 and inside_segment(point2, (point3, point4)):
        return True

    return False


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]

    def union(self, i, j):
        i_id, j_id = self.find(i), self.find(j)

        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id

            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


def main():
    n, m = map(int, input().split())

    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    
    segments = []
    points_set = DisjointSet(n)
    single_points = {i for i in range(n)}

    for _ in range(m):
        point_from, point_to = map(lambda x: int(x) - 1, input().split())
        segments.append((point_from, point_to))
        points_set.union(point_from, point_to)
        single_points.discard(point_from)
        single_points.discard(point_to)
    
    for i in range(m - 1):
        for j in range(i + 1, m):
            point_from1, point_to1 = segments[i][0], segments[i][1]
            point_from2, point_to2 = segments[j][0], segments[j][1]

            p1, q1 = points[point_from1], points[point_to1]
            p2, q2 = points[point_from2], points[point_to2]

            if intersect(p1, q1, p2, q2):
                points_set.union(point_from1, point_to2)
    
    for point_id in single_points:
        for segment in segments:
            point = points[point_id]
            point1, point2 = points[segment[0]], points[segment[1]]
            if orientation(point, point1, point2) == 0:
                if inside_segment(point, (point1, point2)):
                    points_set.union(point_id, segment[0])

    components = {points_set.find(i) for i in range(n)}

    print(["YES", "NO"][len(components) > 1])
    

if __name__ == "__main__":
    main()
