#!/usr/bin/env python3

import urllib.request
import json
import os, sys

fp = open(os.path.join(sys.path[0],"covidrisk.conf"), 'r')
conf = json.load(fp)

risk = ["\033[32mLow\033[0m", "\033[33mModerate\033[0m", "\033[38;2;192;106;11mSubstantial\033[0m", "\033[31mHigh\033[0m", "Unknown", "\033[1;31mExtreme\033[0m"]

stateData = json.loads(urllib.request.urlopen(f"https://api.covidactnow.org/v2/state/{conf['state']}.json?apiKey={conf['apiKey']}").read())
countyData = json.loads(urllib.request.urlopen(f"https://api.covidactnow.org/v2/county/{conf['fips']}.json?apiKey={conf['apiKey']}").read())

factors = [stateData['riskLevels']['caseDensity'],stateData['riskLevels']['infectionRate'],stateData['riskLevels']['testPositivityRatio'],countyData['riskLevels']['caseDensity'],countyData['riskLevels']['infectionRate'],stateData['riskLevels']['testPositivityRatio']]
i = 0
allKnown = True
for n in factors:
	if (n == 4):
		allKnown = False
		factors[i] = -1
		i+=1
	

overall = risk[max(factors)]
risk[0] += "\t"; risk[3] += "\t"; risk[4] += "\t"; risk[5] += "\t";
resultsTable = f"\tNew cases\tInfection rate\tPos. tests\nState\t{risk[stateData['riskLevels']['caseDensity']]}\t{risk[stateData['riskLevels']['infectionRate']]}\t{risk[stateData['riskLevels']['testPositivityRatio']]}\nCounty\t{risk[countyData['riskLevels']['caseDensity']]}\t{risk[countyData['riskLevels']['infectionRate']]}\t{risk[countyData['riskLevels']['testPositivityRatio']]}"

if (allKnown):
	print(f"You are at {overall.lower()} risk.")
else:
	print("Not all risk factors are known.")
	print(f"Based on known risk factors, you are at {overall.lower()} risk.")
print(f"Details\n{resultsTable}")