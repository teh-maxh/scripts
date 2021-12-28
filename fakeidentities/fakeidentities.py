#!/usr/bin/env python3

import datetime
import json
import os
import random
import sys

MIN_PYTHON = (3,10) #pattern matching requires py 3.10
if (sys.version_info < MIN_PYTHON): #min Version
	sys.exit("Minimum python %s.%s!" %MIN_PYTHON)
	
def main():
	identity = genIdentity()
	print(formatName(identity['name']))
	print("Email:", identity['email'])
	print("Address:", formatAddress(identity['address']), sep="\n")
	print("Birthdate:", identity['birthdate'].strftime("%d %b %Y"))
	print("Mother's maiden name:", identity['mothersMaidenName'])
	print("SSN:", identity['ssn'])

def genIdentity():
	name = genName()
	mothersMaidenName = genMothersMaidenName()
	email = genEmail(name)
	address = genAddress()
	birthdate = genBirthdate()
	ssn = genSSN()
	identity = {'name': name, 'email': email, 'address': address, 'birthdate': \
		birthdate, 'mothersMaidenName': mothersMaidenName, 'ssn': ssn}
	return identity

def genName():
	fp = open(os.path.join(sys.path[0],"data/names.json"), 'r')
	names = json.load(fp)
	fp.close()
	name = {'surname': "", 'given': ""}
	i = random.randrange(len(names['surnames']))
	name['surname'] = names['surnames'][i]
	i = random.randrange(len(names['givens']))
	name['given'] = names['givens'][i]
	del names
	return name

def genMothersMaidenName():
	fp = open(os.path.join(sys.path[0],"data/names.json"), 'r')
	names = json.load(fp)
	fp.close()
	i = random.randrange(len(names['surnames']))
	mothersMaidenName = names['surnames'][i]
	del names
	return mothersMaidenName

def genEmail(name):
	fp = open(os.path.join(sys.path[0],"data/emails.json"), 'r')
	emails = json.load(fp)
	fp.close()
	localPartStyle = random.choice(emails['localPartStyles'])
	domain = random.choice(emails['domains'])
	del emails
	
	match localPartStyle: #various ways to construct local-part
		case "first.last": localPart = name['given'] + "." + name['surname']
		case "last.first": localPart = name['surname'] + "." + name['given']
		case "firstlast": localPart = name['given'] + name['surname']
		case "lastfirst": localPart = name['surname'] + name['given']
		case "flast": localPart = name['given'][0] + name['surname']
		case "lastf": localPart = name['surname'] + name['given'][0]
		case "firstl": localPart = name['given'] + name['surname'][0]
		case "lfirst": localPart = name['surname'][0] + name['given']
	
	i = 0
	while (random.random() < 0.24 and i < 3): #maybe add digits to local-part
		localPart = localPart + str(random.randrange(10))
		i = i+1
	del i
	
	email = (localPart + '@' + domain).lower()
	return email

def genAddress():
	fp = open(os.path.join(sys.path[0],"data/addresses.json"), 'r')
	addresses = json.load(fp)
	fp.close()
	i = random.randrange(len(addresses['streets']))
	address = {'street': addresses["streets"][i]}

	if (random.random() < 0.85): #add a directional
		if (random.random() < 0.85): #it's probably cardinal
			directional = random.choice(['N', 'E', 'S', 'W'])
		else: #some are intercardinal
			directional = random.choice(['NE', 'SE', 'SW', 'NW'])
		
		if (random.random() < 0.90): #most addresses use predirectionals
			#easy but ugly way to shove it in
			address['street'] = directional + " " + address['street']
		else: #postdirectionals are rare
			address['street'] = address['street'] + " " + directional
		
	address['street'] = str(random.randrange(9999)) + " " + address['street']

	i = random.randrange(len(addresses['cities']))
	address = address | addresses['cities'][i] #this is weird syntax
	return address
	
def genBirthdate(min=18,max=65):
	d = datetime.timedelta(weeks=(random.uniform(min,max))*52) #can't use years
	birthdate = datetime.datetime.now() - d
	return birthdate

def genSSN():
	ssn = str(random.randrange(999999999)).zfill(9) #up to all 9s, can start w 0
	return ssn

def formatName(name):
	fName = name['surname'].upper() + ", " + name['given'] #LAST, First
	return fName

def formatAddress(address):
	fAddress = address['street'] + "\n" + \
	address['city'] + ", " + address['st'] + " " + address['postcode']
	return fAddress

if __name__ == "__main__":
	main()