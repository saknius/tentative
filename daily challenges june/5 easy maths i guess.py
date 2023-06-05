"""
You are given an array coordinates,
coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.
"""
"""
should have thought through exception
"""

class Solution:
    def checkStraightLine(self, coordinates):
        n = len(coordinates)
        if n<=2:
            return True
        if coordinates[1][0] == coordinates[0][0]:
            original_slope = -1
        else:
            original_slope = (coordinates[1][1] - coordinates[0][1]) // (coordinates[1][0] - coordinates[0][0])
        for i in range(n-1):
            if coordinates[i+1][0] == coordinates[i][0]:
                current_slope = -1
            else:
                current_slope = (coordinates[i+1][1] - coordinates[i][1]) // (coordinates[i+1][0] - coordinates[i][0])
            if original_slope!=current_slope:
                return False
        return True