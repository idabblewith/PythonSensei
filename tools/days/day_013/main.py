# Copyright (c) 2022 Jarid Prince

from days.day_013.files.helpers import *

################################################################
# RUN
################################################################

def day_013():
	title("MULTIPROCESS PORT SCANNER")
	nls("This program is under reconstruction due to breaking changes in dependencies.")
	# for port in PORTS:
	# 	PORTS[port]["status"] = "UNSET"
	# target = nli("Enter a target address to scan.\nE.g 1.1.1.1, 192.168.20.1, google.com")
	# verbose = nli("Would you like to see the process?\nE.g. y, n")
	# if verbose in yes_array:
	# 	verbose = True
	# else:
	# 	verbose = False
		
	# ports = [(port, target, verbose) for port in PORTS]
	# with concurrent.futures.ProcessPoolExecutor() as executor:
	# 	results = executor.map(scan_ports, *zip(*ports))
	# 	for result in results:
	# 		port = result[0]
	# 		status = result[1]
	# 		PORTS[port]["status"] = status

	# 	print_results(target)
	

# ################################################################
# # CONDUCT SCAN PER PORT
# ################################################################

# def scan_ports(port, target, verbose):
# 	try:
# 		pkt = IP(dst=target)/TCP(sport=RandShort(), dport=port)	
# 		resp = sr1(pkt, timeout=2.0, retry=2, verbose=1) if verbose == True else sr1(pkt, timeout=1.0, retry=1, verbose=0)
# 		if resp is None:
# 			# communication blocked by firewall (silent drop)
# 			return [port, "FLTRD"]

# 		elif resp[TCP].flags == "SA":
# 			# S=SYN A=ACK ()
# 			return [port, "OPEN"]

# 		elif resp[TCP].flags == "RA":
# 			# R=RST (Reset from error) A=ACK (Acknowledgement)
# 			return [port, "CLOSED"]
# 	except:
# 		return [port, "UNSET"]

# ################################################################
# # DISPLAY RESULTS
# ################################################################

# # Display PORTS in a table form
# def print_results(target):

#     nls(f'Scan results for host "{target}"')
#     nls(f'  PORT\t\tSTATUS\t\tDESCRIPTION')

#     for port in PORTS:
#         # SA response - open
#         if PORTS[port]["status"] == "OPEN":
#             print(f'  {bcolors.OKGREEN}{port}\t\t{PORTS[port]["status"]}\t\t{PORTS[port]["port"]}{bcolors.ENDC}')

#         # RA response - closed
#         # None response - Filtered
#         elif PORTS[port]["status"] == "FLTRD":
#             print(f'  {bcolors.HEADER}{port}\t\t{PORTS[port]["status"]}\t\t{PORTS[port]["port"]}{bcolors.ENDC}')

#         elif PORTS[port]["status"] == "CLOSED":
#             print(f'  {bcolors.FAIL}{port}\t\t{PORTS[port]["status"]}\t\t{PORTS[port]["port"]}{bcolors.ENDC}')
