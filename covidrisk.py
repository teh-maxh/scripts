#!/usr/bin/env python3

import urllib.request
import json
import os, sys

fp = open(os.path.join(sys.path[0],"covidrisk.conf"), 'r')
conf = json.load(fp)

risk = ["\033[32mLow\t\033[0m", "\033[33mModerate\033[0m", "\033[38;2;203;75;22mSubstantial\033[0m", "\033[38;2;211;54;130mHigh\033[0m", "Unknown"]

stateData = json.loads(urllib.request.urlopen(f"https://api.covidactnow.org/v2/state/{conf['state']}.json?apiKey={conf['apiKey']}").read())
countyData = json.loads(urllib.request.urlopen(f"https://api.covidactnow.org/v2/county/{conf['fips']}.json?apiKey={conf['apiKey']}").read())

overall = risk[max(stateData['riskLevels']['caseDensity'],stateData['riskLevels']['infectionRate'],stateData['riskLevels']['testPositivityRatio'],countyData['riskLevels']['caseDensity'],countyData['riskLevels']['infectionRate'],stateData['riskLevels']['testPositivityRatio'])]
resultsTable = f"\tNew cases\tInfection rate\tPos. tests\nState\t{risk[stateData['riskLevels']['caseDensity']]}\t{risk[stateData['riskLevels']['infectionRate']]}\t{risk[stateData['riskLevels']['testPositivityRatio']]}\nCounty\t{risk[countyData['riskLevels']['caseDensity']]}\t{risk[countyData['riskLevels']['infectionRate']]}\t{risk[countyData['riskLevels']['testPositivityRatio']]}"

print(f"You are at {overall.lower()} risk.\nDetails\n{resultsTable}")