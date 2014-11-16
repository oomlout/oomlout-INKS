#!/usr/bin/python

import sys, os
import time
import Image  #USES PIL library http://www.pythonware.com/products/pil/index.htm

import argparse

parser = argparse.ArgumentParser(description='OOMLOUT-IMAG -- Image Resolution Tool')
parser.add_argument('-id','--iLocation', help='InkScape location', required=False)
parser.add_argument('-bd','--directory', help='directory to recursivly go through to generate PDFs for', required=False)

args = vars(parser.parse_args())

#loading variables from comman line









#
def INKSgeneratePDFs(iLocation, directoryName):
	"Generating Resolutions for: " + directoryName
	for root, _, files in os.walk(directoryName):
		for f in files:
			fullName = os.path.join(root, f)
			try:
				type= f.split(".")[1]
			except:
				print "no file type"
				type=""

			#time.sleep(1)

			#make +01 etc okay (fails if more than 10 images
			if type.lower() in ".svg":
				print "    Generating pdf File: " + f 
				execLine = iLocation + " -f " + '"' + fullName + '" -A "' + fullName.split(".")[0] + '.pdf"'
				print "Executing " + execLine
				os.system(execLine)


iLocation = ""
if args['iLocation'] <> None:
	iLocation = args['iLocation']
	print "InkScape Location: " + iLocation

directoryName = ""
if args['directory'] <> None:
	directoryName = args['directory']
	print "Genrating PDFs for Directory: " + directoryName

if iLocation <> "" and directoryName <> "":
	INKSgeneratePDFs(iLocation, directoryName)




