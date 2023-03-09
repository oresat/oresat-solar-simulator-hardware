from math import pi
class Cubesat:
    def __init__(self) -> None:
        self.cube = {'theta': 0,
                     'sides': []}
        for i in range(4):
            face = {'normal': i * 90}
            self.cube['sides'].append(face)
    
    def get_normal(self, side):
        return (self.cube['sides'][side]['normal'])

    def rotate(self, rot_theta):
        self.cube['theta'] += rot_theta
        for i, side in enumerate(self.cube['sides']):
            side['normal'] = self.cube['theta'] + i * (pi/2)
            if side['normal'] > pi:
                side['normal'] -= 2 * pi
