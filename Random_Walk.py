from random import choice

class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_vals = [0]
        self.y_vals = [0]

    def fill_walk(self):
        while len(self.x_vals) < self.num_points:

            x_direction = choice([-1, 1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_vals[-1] + x_step
            y = self.y_vals[-1] + y_step

            self.x_vals.append(x)
            self.y_vals.append(y)

