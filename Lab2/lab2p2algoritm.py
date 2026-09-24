import unittest
from random import randint

class test_lab(unittest.TestCase):

    def test_closets_pair_and_distance(self):
        self.assertEqual(unittest_result([])[1:], ([]))
        self.assertEqual(unittest_result([[1,1]])[1:], ([]))
        self.assertEqual(unittest_result([[2,3],[3,4]])[1:], ([2,3],[3,4]))
        self.assertEqual(unittest_result([[2,3],[1,9],[6,2]])[1:], ([6,2],[2,3]))
        self.assertEqual(unittest_result([[2,9],[2,4],[2,1],[2,-8]])[1:], ([2,1],[2,4]))
        self.assertEqual(unittest_result([[2,3],[0,4],[11,9],[2,8],[4,4],[3,6],[6,5],[1,9]])[1:], ([2,8],[1,9]))
        self.assertEqual(unittest_result([[5,6],[1,2],[4,-2],[-9,0],[-1,-2],[0,7],[2,-1],[-3,1]])[1:], ([4,-2],[2,-1]))
        self.assertEqual(unittest_result([[-1,20],[-1.5,10],[-2,-10],[-2.7,-20],[-10,20],[-10.5,10],[-11.7,-10],[-12.2,-20],[1,21],[1.5,11],[2,-9],[2.7,-19],[10,21],[10.5,11],[11.7,-9],[12.2,-19]])[1:], ([-1,20],[1,21]))
        self.assertEqual(unittest_result([[2,2],[2,3]])[0], 1)
        self.assertEqual(unittest_result([[3,3],[-1,3]])[0], 4)
        self.assertEqual(unittest_result([[2.7,1.5],[4.7,2.5]])[0], 5**0.5)



class Point:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def __repr__(self) -> str:
        return f'[{self.x}, {self.y}]'

def unittest_points(_list):
    points = []

    for i in range(len(_list)):
        points.append(Point(_list[i][0], _list[i][1], i))

    return points

def unittest_result(_list):
    if len(_list) <= 1:
        return _list
    points = unittest_points(_list)
    d, p1, p2 = calc_min_dist(points)
    ans = []
    for i in points:
        if i.id == p1:
            ans.append(i)
        if i.id == p2:
            ans.append(i)
    
    return dist(ans[0], ans[1]), [ans[0].x, ans[0].y], [ans[1].x, ans[1].y]

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
                for j in range(i - 1, -1, -1):
                    p1 = close_points[i]
                    p2 = close_points[j]
                    if p1.y - p2.y > min_d:
                        break

                    ans = min(ans, (dist(p1, p2), p1.id, p2.id))
            
            return ans
    
    return calc_rec(points, 0, len(points))

if __name__ == '__main__':
    unittest.main()
    # points = gen_random_point(2)
    
    # print(*points)
    # d, p1, p2 = calc_min_dist(points)
    # d1, p11, p21 = calc_min_dist_slow(points)

    # ans = []
    # for i in points:
    #     if i.id == p1:
    #         ans.append(i)
    #     if i.id == p2:
    #         ans.append(i)
    
    # print(dist(ans[0], ans[1]), ans[0], ans[1])

    # ans1 = []
    # for i in points:
    #     if i.id == p11:
    #         ans1.append(i)
    #     if i.id == p21:
    #         ans1.append(i)
    
    # print(dist(ans[0], ans[1]), ans[0], ans[1])