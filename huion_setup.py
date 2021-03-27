#!/usr/bin/env python

# modules used in this script
import argparse, subprocess

def UpdateConfig():
	cmd = "xinput | grep 'HUION Huion Tablet Pen Pen' | awk '{print $9}' > /stor/Documents/Scripts/Huion/huion.cfg"
	subprocess.call(cmd, shell=True)
	
# process command line arguments
def ProcessArguments():
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-f", "--file", dest="file", help="File used in configuration script")
	parser.add_argument("-i", "--id", dest="id", help="ID of device being configured")

	arguments = parser.parse_args()
	
	return arguments

# get the device id from a configuration file created with a bash script
def ExtractIDFromFile(fileName):
	cfgFile = open(fileName)
	
	lines = cfgFile.readlines()
	if(len(lines) > 0):
		deviceID = lines[0].strip().replace("id=", "")
	else:
		deviceID = "-1"
			
	return deviceID

# restrict Huion drawing tablet's pen to specified coordinates with xinput command
def main():
	global previousID
	arguments = ProcessArguments()
	
	UpdateConfig()
	
	if not arguments.file and not arguments.id:
		deviceID = ExtractIDFromFile("/stor/Documents/Scripts/Huion/huion.cfg")
	else:
		if not arguments.file:
			deviceID = arguments.id
		else:
			deviceID = ExtractIDFromFile(arguments.file)
	
	if deviceID == "-1":
		deviceID = previousID
		
		
	cmd = ["xinput set-prop " + deviceID + " --type=float \"Coordinate Transformation Matrix\"  0.5725 0 0.4286 0 .5 0.5 0 0 1"]

	subprocess.call(cmd, shell=True)

# entry point into script
previousID = ExtractIDFromFile("/stor/Documents/Scripts/Huion/huion.cfg")

# execute the logic in the main() function defined above
main()
