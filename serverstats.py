import subprocess

# Define a list of server hostnames or IP addresses
servers = ["server1.example.com", "server2.example.com", "server3.example.com"]

def get_cpu_usage(server):
    command = f"ssh {server} 'top -b -n 1 | grep \"Cpu(s)\"'"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    return output.strip()

def get_memory_usage(server):
    command = f"ssh {server} 'free -m'"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    lines = output.split('\n')
    return lines[1]

def get_disk_usage(server):
    command = f"ssh {server} 'df -h /'"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    lines = output.split('\n')
    return lines[1]

if __name__ == "__main__":
    for server in servers:
        print(f"Server: {server}")

        cpu_usage = get_cpu_usage(server)
        memory_usage = get_memory_usage(server)
        disk_usage = get_disk_usage(server)

        print("\nCPU Usage:")
        print(cpu_usage)

        print("\nMemory Usage:")
        print(memory_usage)

        print("\nDisk Usage:")
        print(disk_usage)

        print("\n" + "=" * 40 + "\n")

