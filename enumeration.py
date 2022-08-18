#enumerate.py Version 0.1 By Redacted
#import required libaries
import argparse
import subprocess

#ascii art of some sort to go here?

#def main():
	#convert_filename(args.host, args.filename)
	#nmap_scan(args.host, args.filename)
	#nmap_allports_scan(args.host, args.filename)
	#gobuster_scan(args.host, args.filename)


def file(file):
	nmapfile = open(f"{file}_nmap","w+")
	nmapallports = open(f"{file}_allports","w+")
	gobusterfile = open(f"{file}_gobuster" , "w+")

		
def nmap_scan(a,b):
	#nmap scan 
	nmap = subprocess.call(['nmap','-sV','-sC' , '-oN',b,a], shell=False, stdin=None, stderr=None )
	nmap
	

def nmap_allports_scan(c,d):
	#nmap scan all ports
	nmap_allport= subprocess.call(['nmap' , '-oN' , d , c], shell=False, stdin=None, stderr=None )
	nmap_allport

def gobuster_scan(e, g):
	#create the gobuster scan
	gobuster = subprocess.call(['gobuster' , 'dir' , '-u' , e ,'-w' '/usr/share/wordlist/dirb/big.txt' , '-x' , '.php,.html,.txt'], shell=False , stdin=None, stderr=None) 
	gobuster

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
f_nmap = (str(filename) +'_nmap')
f_allports = (str(filename) + '_allports')
f_gobuster = (str(filename) + '_gobuster')
h_gobuster = ('http://'+host)



print (f"""Scanning {host} \nnmap version and script scan will be saved as {filename}_nmap\nnmap full port scan will be save as {filename}_allports
gobuster scan will be saved as {filename}_gobuster\n\n\n\name""")

file(filename)
nmap_scan(host, f_nmap)
nmap_allports_scan(host, f_allports)
gobuster_scan(h_gobuster, f_gobuster)
