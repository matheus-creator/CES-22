class Airplane:
    """
    Class that represents an airplane
    """
    def __init__(self, h_vel):
        self.h_vel = h_vel


    def increase_horizontal_velocity(self, h):
        """
        Increases the horizontal velocity of the airplane
        """
        self.h_vel += h


class Helicopter:
    """
    Class that represents a helicopter
    """
    def __init__(self, v_vel):
        self.v_vel = v_vel


    def increase_vertical_velocity(self, v):
        """
        Increases the vertical velocity of the helicopter
        """
        self.v_vel += v


class Evtol(Airplane, Helicopter):
    """
    Class that represents an eVTOL
    """
    def __init__(self, h_vel, v_vel):
        super().__init__(h_vel)
        super(Airplane, self).__init__(v_vel)


    def __str__(self):
        """
        Prints eVTOL's data
        """
        return 'eVTOL data --> Horizontal velocity: ' + str(self.h_vel) + '  Vertical velocity: ' + str(self.h_vel)

    
    def increase_velocity(self, h, v):
        """
        Increases the vertical and horizontal velocity of the eVTOL
        """
        super().increase_horizontal_velocity(h)
        super(Airplane, self).increase_vertical_velocity(v)


my_evtol = Evtol(600, 20)
print(my_evtol)
my_evtol.increase_velocity(200, 10)
print(my_evtol)