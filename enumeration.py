#!/bin/python3 
#enumerate.py Version 0.6 By Redacted
#Import required libaries
#currently only scans port 80, webservers on different ports would need to be scanned manually

import argparse
import subprocess

def convert_file(file):
	filename = (str(file)).lstrip("['").rstrip("']")
	return filename

def convert_host(host):
	host = (str(host)).lstrip("['").rstrip("']")
	return host
		
def file(file):
	#create files for the functions to save stdout
	nmapfile = open(f'{file}_nmap','w+')
	nmapallports = open(f'{file}_allports','w+')
	gobusterfile = open(f"{file}_gobuster" , 'w+')

def gobuster_scan(host, outfile, quiet):
	#create the gobuster scan
	if quiet is True:
		gobuster = subprocess.call(['gobuster' , 'dir' , '-u' , host ,'-w', '/usr/share/wordlists/dirb/big.txt' , '-x' , '.php,.html,.txt'], shell=False , stdin=None, stderr=None, stdout=open(outfile, 'w', 1)) 
	elif verbose is True:
		gobuster = subprocess.call(['gobuster' , 'dir' , '-u' , host ,'-w', '/usr/share/wordlists/dirb/big.txt' , '-x' , '-v', '.php,.html,.txt'], shell=False , stdin=None, stderr=None, stdout=None)
	else:
		gobuster = subprocess.call(['gobuster' , 'dir' , '-u' , host ,'-w', '/usr/share/wordlists/dirb/big.txt' , '-x' , '.php,.html,.txt', '-o',outfile ], shell=False , stdin=None, stderr=None)

	gobuster

def main(host, file_a, file_b, url, file_c,file_d, quiet):
	#ascii art of some sort to go here?
	print (f"""Scanning {host} \nnmap version and script scan will be saved as {file_a}\nnmap full port scan will be saved as {file_b}
gobuster scan will be saved as {file_c}\n\n\n\n""")
	file(file_d)
	nmap_scan(host, file_a, quiet)
	gobuster_scan(url, file_c, quiet)
	nmap_allports_scan(host, file_b, quiet)

def nmap_scan(host,outfile, quiet):
	#nmap scan 
	if quiet is True:
		nmap = subprocess.call(['nmap','-sV','-sC','-oN',outfile,host], shell=False, stdin=None, stderr=None, stdout=subprocess.DEVNULL )
	elif verbose is True:
		nmap = subprocess.call(['nmap','-sV','-sC','-oN',outfile,host,'-v'], shell=False, stdin=None, stderr=None )
	else:
		nmap = subprocess.call(['nmap','-sV','-sC','-oN',outfile,host], shell=False, stdin=None, stderr=None )
	nmap
	
def nmap_allports_scan(host,outfile,quiet):
	#nmap scan all ports
	if quiet is True:
		nmap_allport= subprocess.call(['nmap' , '-oN' , outfile , host, '-p-'], shell=False, stdin=None, stderr=None, stdout=subprocess.DEVNULL )
	elif verbose is True:
		nmap_allport= subprocess.call(['nmap' , '-oN' , outfile , host, '-p-' , '-v'], shell=False, stdin=None, stderr=None )
	else:
		nmap_allport= subprocess.call(['nmap' , '-oN' , outfile , host, '-p-'], shell=False, stdin=None, stderr=None )
		
	nmap_allport

#Input arguments start here
parser = argparse.ArgumentParser()
# Create a new group to store required arguments
requiredName = parser.add_argument_group('Required arguments')

#required arguments
#positinal arguments (no -)
requiredName.add_argument('host',
					help = 'Provide destination host to enumerate',
					type = str,
					nargs = '+'
					)
					
requiredName.add_argument('filename',
					help = 'Select output file name',
					type = str,
					nargs='+'
					)

#Optional arguments
parser.add_argument('-v', '--verbose',
					dest = 'verbose',
					action = 'store_true',
					help = 'Verbose Output'
					)
					
parser.add_argument('-q', '--quiet',
					action = 'store_true',
					dest = 'quiet',
					help = 'Surpress Output'
					)
					
parser.add_argument('--version', 
					action='version', 
					version='%(prog)s 0.5'
					)

args = parser.parse_args()

filename = convert_file(args.filename)
host = convert_host(args.host)
quiet = args.quiet
verbose = args.verbose

f_nmap = (str(filename) +'_nmap')
f_allports = (str(filename) + '_allports')
f_gobuster = (str(filename) + '_gobuster')
url = ('http://'+host)

main(host, f_nmap, f_allports, url, f_gobuster, filename, quiet)
