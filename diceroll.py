#! /usr/bin/env python3

import sys
import random
try:
	import hotbits
except ImportError:
	quit("Please install hotbits. (pip install hotbits)")

if (len(sys.argv) == 1):
	roll = [1,6]
else:
	roll = sys.argv[1].split("d")
	if (roll[0] == ''):
		roll[0] = 1
	else:
		roll[0] = int(roll[0])
	roll[1] = int(roll[1])

random.seed(int.from_bytes(hotbits.RandomDataGenerator().generate(length=512), byteorder='big'))

if (roll[0] == 1):
	result = random.randint(1,roll[1])
else:
	result = []
	for i in range(roll[0]):
		result.append(random.randint(1,roll[1]))

quit(result)