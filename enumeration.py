#enumerate.py Version 0.1 By Keechy

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
#def convert_filename(h, f):
	#print (h_gobuster)
		
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

					
requiredName.add_argument('filename',
					help = 'Select destination file name',
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
					version='%(prog)s 0.1'
					)

args = parser.parse_args()

host = (str(args.host)).lstrip("['").rstrip("']")
filename =  (str(args.filename)).lstrip("['").rstrip("']")
#f_nmap = (str(f) +'nmap')
#f_allports = (str(f) + 'allports')
#f_gobuster = (str(f) + 'gobuster')
h_gobuster = ('http://'+host)


#run the main function


#main()

#for testing
print (f"""Scanning {host} \nnmap version and script scan will be saved as {filename}_nmap\nnmap full port scan will be save as {filename}_allports
gobuster scan will be saved as {filename}_gobuster""")


def file(file):
	nmapfile = open(f"{file}_nmap","w+")
	nmapallports = open(f"{file}_allports","w+")
	gobusterfile = open(f"{file}_gobuster" , "w+")

file(filename)
