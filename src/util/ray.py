class ray :
    def __init__(self, A, B) :
        """
            A and B represent vector in form A + B * t (t is real number)
        """
        self.A = A
        self.B = B 
    def get_origin(self):
        return self.A
    def get_direction(self):
        return self.B
    def get_point_at(self, t):
        return self.A + self.B * t