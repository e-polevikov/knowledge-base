

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


def main():
    n, m = map(int, input().split())

    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    
    segments = set()
    for _ in range(m):
        point_from, point_to = map(lambda x: int(x) - 1, input().split())
        segments.add((point_from, point_to))


if __name__ == "__main__":
    main()
