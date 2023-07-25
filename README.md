# The Golden Route Challenge

A challenge where I need to build a website with two pages:

On the first page, the user enters the weight of the aircraft's cargo.

The website shows the aircraft's minimum take-off time and take-off distance.

In the event that the mass is greater than the maximum mass,

the website will display a message stating that the aircraft must shed weight from the cargo in order to take off.

On the second page, the user enters the date of a flight.

The website displays the hours during which the weather suits the flight.

If there are no such hours on the relevant date, the site displays a message saying it is impossible to reach the destination on the date.

# Buiness logic - Answers

## Question 1:

We can check all the service functions using unit tests.

In each function, we will check its output with manual output that we will check ourselves.

The possible edge cases are when the cargo is zero, negative, or not a number.

A cargo of zero is an edge case where the service should work fine, and it is a case where the system should calculate the output as usual according to the same formulas.

It is important to check that the system works even when the cargo is zero kilograms.

If the cargo mass is negative or not a number, we will ask the user to enter a valid cargo mass, and we will not get output until he enters a non-negative cargo mass.

If one of the functions receives a negative or non-number input, we will throw an exception.

## Question 2:

To improve the system's physical model, we can consider the change in mass of the aircraft due to fuel usage.

We can also compute the friction (with air and with the surface).

And we also can use equations of motion for changing acceleration.

# External API connection - Answers

In my opinion, it is advisable to present to customers both the wind 

(speed and direction) and the temperature at the height at which the aircraft is flying,

as well as the weather data at the destination of the flight.

# System Survivability

The system I built depends on an internet connection and will not work when the customer is not connected to the internet.

The system will also not survive in the event of a malfunction in the server computers.

The application is also dependent on the external API, 

and, therefore, will not survive in the event of a malfunction in the external API server.

# Running instructions

Make sure you are connected to the internet.

Make sure you have active and valid docker and docker-compose.

You can install docker and docker-compose from here:
https://docs.docker.com/get-docker/

Make sure nothing is running on ports 3000 and 8000.

Make sure you have active and valid git.

You can install git from here:

https://git-scm.com/downloads

Run the following commands in the terminal:
1. `git clone https://github.com/yonikremer/golden_route.git` (clone the repository)
2. `cd golden_route` (enter the repository directory)
3. `docker-compose up -d --build` (build and run the containers)
