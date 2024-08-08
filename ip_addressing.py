from math import log2, ceil

def calculate_log_values(host):
    log_value = log2(host)
    ceil_value = ceil(log_value)
    return ceil_value

def calculate_blocksize(n_bits):
    rem = n_bits % 8
    binary_str = ""

    while rem > 0:
        binary_str += "1"
        rem -= 1

    i = 8 - len(binary_str)
    while i > 0:
        binary_str += "0"
        i -= 1

    binary_str = binary_str.ljust(8, '0')

    blocksize = 0
    for i in range(8):
        blocksize += int(binary_str[i]) * (2 ** (7 - i))

    return 256 - blocksize

def calculate_subnets(hosts, ip_add):
    current_ip = ip_add
    index = ip_add.find('/')
    sub = ip_add[index + 1:]
    eff_octet = int(int(sub) / 8)
    ip_add = ip_add[:index]
    tokens = ip_add.split('.')

  
    hosts.sort(reverse=True)

    results = []
    for host in hosts:
        print(f"\nCalculating for host requirement: {host}")
        x = calculate_log_values(host)
        blocksize = calculate_blocksize(32 - x)

        nid_1 = current_ip
        tokens[eff_octet] = str(int(tokens[eff_octet]) + blocksize)
        nid_2 = '.'.join(tokens)

        results.append({
            "host": host,
            "nid_1": nid_1,
            "nid_2": nid_2,
            "allocated_ips": x,
            "blocksize": blocksize
        })

        current_ip = nid_2

    return results

ip_add = input("Enter the IP address in CIDR notation (e.g., 192.168.1.0/24): ")

hosts_input = input("Enter host requirements: ")
hosts = list(map(int, hosts_input.strip().split()))

subnet_details = calculate_subnets(hosts, ip_add)

for subnet in subnet_details:
    print(f"\nHost requirement: {subnet['host']}")
    print(f"nid_1: {subnet['nid_1']}")
    print(f"nid_2: {subnet['nid_2']}")
    print(f"Allocated IPs: {subnet['allocated_ips']}")
    print(f"Block size: {subnet['blocksize']}")
