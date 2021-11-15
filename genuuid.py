#!/usr/bin/env python3

import uuid
import sys

argc = len(sys.argv)

if(argc == 2):
	from socket import gethostname
	domain = gethostname().split('.', 1)[1]
	name = sys.argv[1];

elif(argc == 3):
	domain = sys.argv[1];
	name = sys.argv[2];

else:
	print("Usage: genuuid [domain] name");
	quit();

uuid = str(uuid.uuid5(uuid.uuid5(uuid.NAMESPACE_DNS,domain),name));
print(uuid);