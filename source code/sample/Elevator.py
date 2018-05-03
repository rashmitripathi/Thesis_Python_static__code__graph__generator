from time import sleep

class Elevator():

    def __init__(self, num, floor=0):
        """Takes current floor as a parameter."""

        self.floor = floor
        self.num = num
        self.wear = 0
        self.direction = None

    def __str__(self):
        return "Elevator {} on floor {}".format(self.num, self.floor)

    def __repr__(self):
        return "<Elevator object {} currently on floor {}>".format(
                                            self.num, self.floor)

    def open(self):
        print ("Doors opening on elevator {}.".format(self.num))

    def close(self):
        print ("Doors closing on elevator {}.".format(self.num))

    def move(self, system):
        """Takes an ElevatorSystem and moves one floor in self.direction."""

        system.floors[self.floor].remove(self)
        self.wear += 1
        self.floor += self.direction
        system.floors[self.floor].append(self)

        print("On floor {}...".format(self.floor))

    def deactivate(self, system, warning=True):
        """Takes Elevator System to remove self from."""

        system.floors[self.floor].remove(self)
        if warning:
            print ("Elevator {} needs servicing. It is now deactivated".
                                                            format(self))

    def repair(self, system=None):
        """Resets wear optionally takes system to reattach to.

        If the elevator was broken, pass in an ElevatorSystem that
        the elevator should reattach itself to.
        For normal maintenance, this isn't required."""

        self.wear = 0
        if system is not None:
            system.floors[self.floor].append(self)
            print ("Elevator {} has been repaired.".format(self))


class ElevatorSystem():
    """A system for managing a building's elevators.

    Takes floor and elevator count as parameters.
    init will create the necessary Elevator objects.
    Active elevators are held on floors and accessed there."""

    #Constants to determine how in need of repair elevators are
    WEAR_WARNING = 4000
    WEAR_THRESHOLD = 5000

    def __init__(self, floor_count=3, elevator_count=2):
        if floor_count < 2 or elevator_count < 2:
            raise (ValueError, "Invalid parameters"
                   "Floor and elevator counts should be greater than 1.")

        self.elevators = [Elevator(i) for i in range(elevator_count)]
        self.floors = [[] for _ in range(floor_count)]
        self.floors[0] = self.elevators[:]
        self.deactivated = []

    def __repr__(self):
        return ("<ElevatorSystem object containing {} floors and {} elevators>"
                            .format(len(self.floors), len(self.elevators)))

    def __str__(self):
        return ("Elevator System with {} elevators on floors "
                .format(len(self.elevators)) +
                ', '.join(str(elevator.floor if elevator.floor else 'G')
                              for elevator in self.elevators))

    def validate_floor(self, floor):
        """Raises a ValueError if floor doesn't exist."""

        if floor >= len(self.floors):
            raise ValueError("Invalid floor {}, system only "
                             "has {} floors.".format(floor, len(self.floors)))

    def choose_elevator(self, elevators, direction):
        """Return elevator that's most suitable.

        Takes in direction to first filter out moving elevators.
        Alternatively filters out elevators moving the wrong direction.
        Lastly will take the least worn elevator as its choice."""

        # First try take static elevators
        chosen_elevators = [elevator for elevator in elevators if
                                elevator.direction is None]

        # Now get elevators travelling in the right direction
        if not chosen_elevators:
            [elevator for elevator in elevators if
                elevator.direction == direction]

        #If that fails too, just take what we've got
        if not chosen_elevators:
            chosen_elevators = elevators

        #Sort by wear and take the first ie. lowest value in the sorted list
        return sorted(chosen_elevators, key=lambda ele: ele.wear)[0]


    def call_elevator(self, floor, direction):
        """Chooses and returns an elevator after moving it to floor.

        Floor should be the floor the elevator is called to.
        Direction should indicate which way the user wants to travel.
        Valid values are 1 or -1."""

        self.validate_floor(floor)
        if direction not in (1, -1):
            raise ValueError("direction only accepts 1 or -1, not {}".
                                                        format(direction))

        #Check if there's any elevators on the current floor
        if self.floors[floor]:
            elevator = self.choose_elevator(self.floors[floor], direction)
            elevator.open()
            return elevator

        #Now search outward, one floor up and down at a time.
        #None pads the list if we run out of floors in one direction
        check_floors = map(None, range(floor + 1, len(self.floors)),
                                 range(floor - 1, -1, -1))
        for up, down in check_floors:
            if down is not None and self.floors[down]:
                elevator = self.choose_elevator(self.floors[down], direction)
                break
            if up is not None and self.floors[up]:
                elevator = self.choose_elevator(self.floors[up], direction)
                break
        else:
            raise Exception("Cannot find elevators.")

        self.move_elevator(elevator, floor)
        return elevator

    def move_elevator(self, elevator, floor):
        """Send elevator to floor, moving one floor at a time."""

        self.validate_floor(floor)
        print("Elevator {} moving".format(elevator.num))

        move_up = elevator.floor < floor
        elevator.direction = 1 if move_up else -1

        # Build the range based on which direction we need to go
        # We do this because range won't work if floor < elevator.floor
        for _ in (range(elevator.floor, floor) if move_up
                            else range(elevator.floor, floor, -1)):
            elevator.move(self)
            sleep(0.5)

        elevator.open()
        elevator.direction = None

    def maintenance_check(self, warnings=True):
        """Update list of deactivated elevators

        Optionally warns about elevators that need maintenance now or soon.
        Pass False to suppress printing these warnings."""

        for floor in self.floors:
            for elevator in floor:
                wear = elevator.wear
                if wear > self.WEAR_THRESHOLD:
                    self.deactivated.append(elevator)
                    elevator.deactivate(self, warnings)
                elif warnings and wear > self.WEAR_WARNING:
                    print ("{} has wear of {} and should be serviced soon".
                                format(elevator, elevator.wear))

    def repair_elevators(self, maintenance=False):
        """Repair or optionally service broken and worn elevators.

        maintenance determines whether or not to repair any elevator with
        significant wear or just to repair deactivated ones."""

        for elevator in self.deactivated:
            elevator.repair(self)

        if maintenance:
            for floor in self.floors:
                for elevator in floor:
                    if elevator.wear > self.WEAR_WARNING:
                        elevator.repair()





