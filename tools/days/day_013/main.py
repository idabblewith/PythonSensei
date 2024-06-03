# Copyright (c) 2024 Jarid Prince

from days.day_013.files.helpers import *

################################################################
# RUN
################################################################


def check_npcap():
    npcap_installed = False
    try:
        # Check if npcap is installed by attempting to use the conf.iface function
        conf.iface
        npcap_installed = True
    except Exception as e:
        npcap_installed = False
    return npcap_installed


def day_013():
    title("MULTIPROCESS PORT SCANNER")
    if check_npcap():
        for port in PORTS:
            PORTS[port]["status"] = "UNSET"
        target = nli(
            "Enter a target address to scan.\nE.g 1.1.1.1, 192.168.20.1, google.com"
        )
        verbose = nli("Would you like to see the process?\nE.g. y, n")
        if verbose in yes_array:
            verbose = True
        else:
            verbose = False

        ports = [(port, target, verbose) for port in PORTS]
        # Avoiding ProcessPoolExecutor due to Windows issues
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(scan_ports, *zip(*ports))
            for result in results:
                port = result[0]
                status = result[1]
                PORTS[port]["status"] = status

            print_results(target)
    else:
        nls("Npcap is not installed on the local device running this app. Ending.")
        sys.exit(1)


################################################################
# CONDUCT SCAN PER PORT
################################################################


def scan_ports(port, target, verbose):
    try:
        pkt = IP(dst=target) / TCP(sport=RandShort(), dport=port)
        resp = (
            sr1(pkt, timeout=2.0, retry=2, verbose=1)
            if verbose == True
            else sr1(pkt, timeout=1.0, retry=1, verbose=0)
        )
        if resp is None:
            # communication blocked by firewall (silent drop)
            return [port, "FLTRD"]

        elif resp[TCP].flags == "SA":
            # S=SYN A=ACK ()
            return [port, "OPEN"]

        elif resp[TCP].flags == "RA":
            # R=RST (Reset from error) A=ACK (Acknowledgement)
            return [port, "CLOSED"]
        else:
            return [port, resp[TCP].flags]

    except:
        return [port, "UNSET"]


################################################################
# DISPLAY RESULTS
################################################################


# Display PORTS in a table form
def print_results(target):

    nls(f'Scan results for host "{target}"')
    nls(f"  PORT\t\tSTATUS\t\tDESCRIPTION")

    for port in PORTS:
        # SA response - open
        if PORTS[port]["status"] == "OPEN":
            print(
                f'  {bcolors.OKGREEN}{port}\t\t{PORTS[port]["status"]}\t\t{PORTS[port]["port"]}{bcolors.ENDC}'
            )

        # RA response - closed
        # None response - Filtered
        elif PORTS[port]["status"] == "FLTRD":
            print(
                f'  {bcolors.HEADER}{port}\t\t{PORTS[port]["status"]}\t\t{PORTS[port]["port"]}{bcolors.ENDC}'
            )

        elif PORTS[port]["status"] == "CLOSED":
            print(
                f'  {bcolors.FAIL}{port}\t\t{PORTS[port]["status"]}\t\t{PORTS[port]["port"]}{bcolors.ENDC}'
            )


if __name__ == "__main__":
    day_013()
