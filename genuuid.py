#!/usr/bin/env python3

import uuid
import sys

if(len(sys.argv) == 1):
	print("Usage: genuuid [domain] name");
	quit();

if(len(sys.argv) == 2):
	from socket import gethostname
	domain = gethostname().split('.', 1)[1]
	name = sys.argv[1];

if(len(sys.argv) == 3):
	domain = sys.argv[1];
	name = sys.argv[2];

uuid = str(uuid.uuid5(uuid.uuid5(uuid.NAMESPACE_DNS,domain),name));
print(uuid);