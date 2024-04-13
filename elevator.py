class Elevator:
    def __init__(self, id, total_floors):
        self.id = id
        self.current_floor = 0
        self.total_floors = total_floors
        self.direction = None

    def move_up(self):
        if self.current_floor < self.total_floors:
            self.current_floor += 1

    def move_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def open_doors(self):
        print(f"Elevator {self.id} opening doors.")

    def close_doors(self):
        print(f"Elevator {self.id} closing doors.")
      
class Request:
    def __init__(self, floor):
        self.floor = floor

class Controller:
    def __init__(self):
        self.elevators = [Elevator(i, 10) for i in range(3)]

    def handle_request(self, request):
        # Simple logic to assign the request to the first available elevator
        for elevator in self.elevators:
            if elevator.current_floor == request.floor:
                elevator.open_doors()
                elevator.close_doors()
                return
            elif elevator.current_floor < request.floor:
                while elevator.current_floor != request.floor:
                    elevator.move_up()
                elevator.open_doors()
                elevator.close_doors()
                return
            else:
                while elevator.current_floor != request.floor:
                    elevator.move_down()
                elevator.open_doors()
                elevator.close_doors()
                return

def main():
    controller = Controller()
    while True:
        floor_request = int(input("Enter a floor number (0-10): "))
        if floor_request < 0 or floor_request > 10:
            print("Invalid floor. Please try again.")
        else:
            controller.handle_request(Request(floor_request))

if __name__ == "__main__":
    main()
  
