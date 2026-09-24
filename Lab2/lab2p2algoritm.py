from random import randint

class Point:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def __repr__(self) -> str:
        return f'[{self.x}, {self.y}]'

def dist(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

def gen_random_point(length):
    points = []

    for i in range(length):
        points.append(Point(randint(0, 50), randint(0, 50), i))
    
    return points

def merge(points, l, r):
    m = (l + r) // 2
    tmp = []
    i = l
    j = m
    while i < m or j < r:
        if j == r or (i < m and points[i].y < points[j].y):
            tmp.append(points[i])
            i += 1
        else:
            tmp.append(points[j])
            j += 1
    points[l:r] = tmp

def calc_min_dist_slow(points):
    ans = (100, -1, -1)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if ans[0] > dist(points[i], points[j]):
                ans = (dist(points[i], points[j]), points[i].id, points[j].id)
    
    return ans

def calc_min_dist(points):
    points.sort(key = lambda point: point.x)
    def calc_rec(points, l, r):
        if r - l <= 3:
            ans = calc_min_dist_slow(points[l:r])
            points[l:r] = sorted(points[l:r], key=lambda point: point.y)
            return ans
        else:
            m = (l + r) // 2
            middle_x = points[m].x
            ans = min(calc_rec(points, l, m), calc_rec(points, m, r))
            merge(points, l, r)
            min_d = ans[0]

            close_points = list(filter(lambda point: abs(point.x - middle_x) < min_d, points))
            
            for i in range(len(close_points)):
                for j in range(i - 1, 0, -1):
                    p1 = close_points[i]
                    p2 = close_points[j]
                    if p1.y - p2.y > min_d:
                        break

                    ans = min(ans, (dist(p1, p2), p1.id, p2.id))
            
            return ans
    
    return calc_rec(points, 0, len(points))

if __name__ == '__main__':
    points = gen_random_point(2)

    print(*points)
    d, p1, p2 = calc_min_dist(points)
    d1, p11, p21 = calc_min_dist_slow(points)

    ans = []
    for i in points:
        if i.id == p1:
            ans.append(i)
        if i.id == p2:
            ans.append(i)
    
    print(dist(ans[0], ans[1]), ans[0], ans[1])

    ans1 = []
    for i in points:
        if i.id == p11:
            ans1.append(i)
        if i.id == p21:
            ans1.append(i)
    
    print(dist(ans[0], ans[1]), ans[0], ans[1])