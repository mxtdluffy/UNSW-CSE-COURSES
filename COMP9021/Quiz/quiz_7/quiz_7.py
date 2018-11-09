# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by *** and Eric Martin for COMP9021


from math import pi, hypot


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'

class Disk:
    def __init__(self, *, centre = Point(0.00, 0.00), radius = 0.00):
        self.centre = centre
        self.radius = radius
        self.area = pi * self.radius * self.radius
        # print(f'Disk({self.centre.__repr__()}, {self.radius:.2f})')
    def __repr__(self):
        return f'Disk(Point({self.centre.x:.2f}, {self.centre.y:.2f}), {self.radius:.2f})'

    def change_radius(self, r):
        self.radius = r
        self.area = pi * self.radius * self.radius
    
    def intersects(self, disk):
        distance = (self.centre.x - disk.centre.x) ** 2 + \
                    (self.centre.y - disk.centre.y) ** 2
        if distance > (self.radius + disk.radius) ** 2:
            return False
        else:
            return True
    
    def absorb(self, disk):
        distance = ((self.centre.x - disk.centre.x) ** 2 + \
                    (self.centre.y - disk.centre.y) ** 2) ** 0.5
        cos = abs(self.centre.x - disk.centre.x) / distance
        sin = abs(self.centre.y - disk.centre.y) / distance
        if self.centre.x > disk.centre.x:
            self_x_compare = 1
        elif self.centre.x == disk.centre.x:
            self_x_compare = 0
        else:
            self_x_compare = -1
        if self.centre.y > disk.centre.y:
            self_y_compare = 1
        elif self.centre.y == disk.centre.y:
            self_y_compare = 0
        else:
            self_y_compare = -1

        if distance <= abs(self.radius - disk.radius) and self.radius >= disk.radius:
            newdisk_r_x = self.centre.x
            newdisk_r_y = self.centre.y
            newdisk_r = self.radius
        elif distance <= abs(self.radius - disk.radius) and self.radius <= disk.radius:
            newdisk_r_x = disk.centre.x
            newdisk_r_y = disk.centre.y
            newdisk_r = disk.radius            
        else:
            if self_x_compare == 0:
                newdisk_r_x = self.centre.x
                newdisk_r_y = (self.centre.y + self.radius * self_y_compare + \
                    disk.centre.y + disk.radius * (- self_y_compare)) / 2
                newdisk_r = (distance + self.radius + disk.radius) / 2
            elif self_y_compare == 0:
                newdisk_r_x = (self.centre.x + self.radius * self_x_compare + \
                    disk.centre.x + disk.radius * (- self_x_compare)) / 2
                newdisk_r_y =  self.centre.y
                newdisk_r = (distance + self.radius + disk.radius) / 2
            else:
                newdisk_r_x = (self.centre.x + self.radius * cos * self_x_compare + \
                    disk.centre.x + disk.radius * cos * (- self_x_compare)) / 2
                newdisk_r_y = (self.centre.y + self.radius * sin * self_y_compare + \
                    disk.centre.y + disk.radius * sin * (- self_y_compare)) / 2
                newdisk_r = (distance + self.radius + disk.radius) / 2
            
        newdisk = Disk(centre = Point(newdisk_r_x, newdisk_r_y), radius = newdisk_r)
        return newdisk
            

