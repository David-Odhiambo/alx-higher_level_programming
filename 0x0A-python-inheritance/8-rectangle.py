class Polygon(object):
    ...
    def isConvex(self):
        for i in range(self.n):
            #Check every triplet of point
            A = self.points[i % self.n]
            B = self.pointd[(i + 1) % self.n]
            C = self.points[(i + 2) % self.n]
            if not ccw(A, B, C)
                return False
            return True