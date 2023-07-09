import numpy as np
class RegionGeometry(object):

    def __init__(self, poly_list):
        self.polys=poly_list

    @staticmethod
    def flatten(l):
        return [item for sublist in l for item in sublist]

    def bbox(self):
        flat_polys=RegionGeometry.flatten(self.polys)
        top=max(flat_polys,key=lambda pt:pt[1])
        left=min(flat_polys,key=lambda pt:pt[0])
        bottom=min(flat_polys,key=lambda pt:pt[1])
        right=max(flat_polys,key=lambda pt:pt[0])
        return top,right,bottom,left

    def in_bbox(self,pos):
        top, right, bottom, left=self.bbox()
        return left[0] <= pos[0] <= right[0] and bottom[1] <= pos[1] <= top[1]

    def in_polys(self,pos):
        for poly in self.polys:
            if self.is_inside_sm(poly,pos):
                return True

    def is_inside_sm(self,polygon, point):
        length = len(polygon) - 1
        dy2 = point[1] - polygon[0][1]
        intersections = 0
        ii = 0
        jj = 1

        while ii < length:
            dy = dy2
            dy2 = point[1] - polygon[jj][1]

            # consider only lines which are not completely above/bellow/right from the point
            if dy * dy2 <= 0.0 and (point[0] >= polygon[ii][0] or point[0] >= polygon[jj][0]):

                # non-horizontal line
                if dy < 0 or dy2 < 0:
                    F = dy * (polygon[jj][0] - polygon[ii][0]) / (dy - dy2) + polygon[ii][0]

                    if point[0] > F:  # if line is left from the point - the ray moving towards left, will intersect it
                        intersections += 1
                    elif point[0] == F:  # point on line
                        return 2

                # point on upper peak (dy2=dx2=0) or horizontal line (dy=dy2=0 and dx*dx2<=0)
                elif dy2 == 0 and (point[0] == polygon[jj][0] or (
                        dy == 0 and (point[0] - polygon[ii][0]) * (point[0] - polygon[jj][0]) <= 0)):
                    return 2

            ii = jj
            jj += 1

        # print 'intersections =', intersections
        return intersections & 1
