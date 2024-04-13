# Low-Level-Design-of-an-Elevator

In the world of software engineering, designing an elevator system is a classic example of low-level system design that is often used in technical interviews. This blog post will guide you through the process of designing a basic elevator system, focusing on object-oriented principles and clear logic. We will be using Python for our implementation, known for its readability and simplicity, making it ideal for demonstrating design concepts. By the end of this post, you’ll have a functional elevator simulation that you can run and experiment with.

## Introduction: Understanding the Elevator System
### Why Design an Elevator System?
Designing an elevator system is an excellent way to understand complex system design, encapsulation, and the handling of concurrent requests in a controlled environment.

### Objectives of the Design
Our aim is to create a simple yet functional elevator simulation that can:
- Handle multiple elevator requests.
- Process these requests in an efficient manner.
- Demonstrate basic elevator movements: up, down, open, and close doors.

## Breaking Down the Components
### The Main Components
Our elevator system will consist of the following components:

- Elevator: The core class representing the elevator.
- Request: A class to encapsulate an elevator request.
- Controller: Manages the elevators and assigns requests to them.

### Elevator Class
The Elevator class represents a single elevator. Its key responsibilities include:
- Moving up and down.
- Opening and closing doors.
- Keeping track of its current floor.

### Request Class
Each elevator request is an instance of the Request class, which includes:
- Requested floor.
- Direction (up or down).

### Controller Class
The Controller class is the brain of the system, responsible for:
- Handling requests.
- Assigning requests to the appropriate elevator.

## Implementing the Elevator System in Python
Now, let’s dive into the implementation. The following code is a complete, functional simulation of our elevator system.


- The Elevator Class
```
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
```


- The Request Class
```
class Request:
    def __init__(self, floor):
        self.floor = floor
```


- The Controller Class
```
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
```


- Main Program to Run the Elevator System
```
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
```

## Conclusion: Bringing It All Together
This basic elevator simulation demonstrates key concepts in low-level system design, such as handling multiple requests and managing the state and behavior of objects. It is a stepping stone towards understanding more complex systems and designing efficient algorithms to handle real-world scenarios.

Remember, this is a simplified version of what an actual elevator system might entail. In real-world applications, the system would need to handle edge cases, concurrency, and much more complex scheduling algorithms. Feel free to expand on this foundation, perhaps by adding features like request prioritization based on various factors or handling simultaneous requests more efficiently.

