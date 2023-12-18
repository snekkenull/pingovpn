import socket
import re
from collections import defaultdict
import sys

def domain_to_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return domain  # return the original domain if it cannot be resolved

# Check if filename is provided
if len(sys.argv) < 2:
    print("Please provide a filename.")
    sys.exit()

filename = sys.argv[1]
new_filename = 'modified_' + filename

# Open the original file
with open(filename, 'r') as file:
    lines = file.readlines()

# Initialize dictionary to track encountered IPs
used_ips = defaultdict(lambda: False)

# Define pattern to match domain lines
domain_pattern = re.compile(r'remote (\S+) (\d+)')

modified_lines = []
for line in lines:
    match = domain_pattern.search(line)
    if match:
        domain = match.group(1)
        port = match.group(2)
        ip = domain_to_ip(domain)
        # Check if IP already used
        if not used_ips[ip]:
            line = line.replace(domain, ip)
            used_ips[ip] = True
    modified_lines.append(line)

# Write the modified lines to a new file
with open(new_filename, 'w') as file:
    file.writelines(modified_lines)

print(f"Modified openvpn file saved as '{new_filename}'")
