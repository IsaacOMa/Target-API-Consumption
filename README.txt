The constructed program finds the time remaining until the next departure for a given bus route provided the bus stop name and the direction. 
This is the API consumption option.

The project imports sys, requests, and time.

In order to run the program, put "nextbus.py <bus route> <bus stop name> <direction>" into the command line. 
Ex: nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "south"

Additional Notes: 
For the most part, nextbus.py tries to make use of nextripv2. This was however not always feasible. 
When looking for the bus route_id for example, only the metro routes are named - all other routes are only provided with a number. 
Therefore nextbus.py makes use of the text file routes.txt from version 1 to find the route_id.

When there are no more buses for the day, the program explains that is the case and returns the string saying "The last bus has departed".

Test samples (where x is a number):

Correct input samples:
nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "south"
- output: x Minutes

nextbus.py "Uptown - Lake St - Midway - Selby" "6th St and Cedar St" "west"
- output: x Minutes


Incorrect route name:
nextbus.py "Express - Target - Hwy 252 and 73rd Av P&R - Mpls" "Target North Campus Building F" "south"
- output: Error: invalid bus route input

Asking for the next departure when there are no more buses for the day:
nextbus.py "Express - Brooklyn Park - Xerxes - 49th Av - Mpls" "2nd Ave and 6th St" "north"
- output: The last bus has departed

Incorrect direction input (this route only has westbound):
nextbus.py "Plymouth - Express - Midday - Northeast Plymouth" "11th St and Harmon P1" "south"
- output: Error: direction not found



