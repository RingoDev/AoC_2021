def create_area():
    pass


class Missile:
    x = 0
    y = 0
    max_y = 0

    # default constructor
    def __init__(self, x_vel, y_vel, target_x1, target_x2, target_y1, target_y2):
        self.x_start_vel = x_vel
        self.y_start_vel = y_vel
        self.x_velocity = x_vel
        self.y_velocity = y_vel
        self.target_x1 = min(target_x1, target_x2)
        self.target_x2 = max(target_x1, target_x2)
        self.target_y1 = min(target_y1, target_y2)
        self.target_y2 = max(target_y1, target_y2)

    def __repr__(self):
        return f"({self.x},{self.y}) with velocity ({self.x_velocity}, {self.y_velocity})"

    def do_step(self):
        self.x = self.x + self.x_velocity
        self.y = self.y + self.y_velocity
        if self.x_velocity < 0:
            self.x_velocity = self.x_velocity + 1
        elif self.x_velocity > 0:
            self.x_velocity = self.x_velocity - 1
        self.y_velocity = self.y_velocity - 1
        if self.max_y < self.y:
            self.max_y = self.y

    def can_still_hit(self):
        if self.y < self.target_y1 and self.y_velocity <= 0:
            return False
        if self.x < self.target_x1 and self.x_velocity <= 0:
            return False
        return True

    def is_in_target_area(self, ):
        return self.x in range(self.target_x1, self.target_x2 + 1) and \
               self.y in range(self.target_y1, self.target_y2 + 1)


def run(x1, x2, y1, y2):
    solution_count = 0
    max_missile = None
    for x in range(max(x1, x2) + 1):
        # 200 is chosen arbirarily
        for y in range(min(y1, y2), 200):
            missile = Missile(x, y, x1, x2, y1, y2)
            while missile.can_still_hit():
                missile.do_step()
                if missile.is_in_target_area():
                    print(f"({x},{y}) did hit target with max height {missile.max_y}")
                    solution_count = solution_count + 1
                    if max_missile is None or max_missile.max_y < missile.max_y:
                        max_missile = missile
                    break
    if max_missile is not None:
        print(
            f"Highest y: {max_missile.max_y} with start velocity: ({max_missile.x_start_vel}, {max_missile.y_start_vel})")
        print(f"Found {solution_count} solutions")


run(235, 259, -118, -62)
