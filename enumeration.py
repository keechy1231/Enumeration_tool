#enumerate.py Version 0.1 By Redacted

#import required libaries
import argparse
import subprocess

#ascii art of some sort to go here?

def main():
	#to build
	convert_filename(args.host, args.filename)
	nmap_scan(args.host, args.filename)
	nmap_allports_scan(args.host, args.filename)
	gobuster_scan(args.host, args.filename)
	

#convert file name to work with nmap and gobuster	
def convert_filename(h, f):
		f_nmap = (f +'nmap')
		f_allports = (f + 'allports')
		f_gobuster = (f + 'gobuster')
		h_gobuster = ('http://'+ host)
		
def nmap_scan(a,b):
	#create function for the first nmap scan 
	#subprocess()
	#"nmap {a} -sV -sC -oN {b} -Pn"
	print("test")

def nmap_allports_scan(c,d):
	#create function for the second nmap scan (all ports)
	#"nmap {host} -p- -Pn -oN {f_allports}"
	print("test")
	
def gobuster_scan(e, g):
	#create the gobuster scan
	#"gobuster dir -u {h_gobuster} -w /usr/share/wordlists/dirb/big.txt -x .php,.html,.txt > {f_gobuster}"
	print("test")

parser = argparse.ArgumentParser()

# Create a new group to store required arguments
requiredName = parser.add_argument_group('Required arguments')

#arguments for usage with the script

#required arguments
#positinal arguments (no -)
requiredName.add_argument('host',
					help = 'Provide destination host to enumerate',
					type = str,
					nargs = '+'
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
					
parser.add_argument('-f', '--outfile',
					action = 'store_true',
					dest = 'outfile',
					help = 'Select destination file name'
					)
					
parser.add_argument('--version', 
					action='version', 
					version='%(prog)s 0.1'
					)

args = parser.parse_args()

#run the main function
#main()

#for testing
print (f"Enumerating {args.host}")

print (f_nmap)
