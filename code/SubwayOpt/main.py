import time
import random
from person import person
from pathnode import pathnode
from goal import goal
from train import train

Timelimit = 1
Trians = [ train("Train-" + str(i),random.randint(1,10)) for i in range(10) ]
People = [ person(goal(True, None)) for i in range(10) ]
PathNodes = [ pathnode(random.random(),random.random(),random.random(),2) for i in range(10) ]

def Simulate():
	timestep = 0
	while 1:
		time.sleep(1) # delay for 1 second.
		if Timelimit <= timestep: break
		timestep += 1
		print ("The timestep of the simulation is: {}".format(str(timestep)))


def main():
	Simulate()

if __name__ == "__main__":
	main()
