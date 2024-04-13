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
