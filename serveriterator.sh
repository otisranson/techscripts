#!/bin/bash

# List of server IP addresses or hostnames
servers=("server1" "server2" "server3" ... "server20")

# Loop through the list of servers
for server in "${servers[@]}"; do
    echo "Connecting to $server..."
    
    # Use SSH to run the 'hostname' command remotely and store the result in a variable
    hostname=$(ssh "$server" hostname 2>/dev/null)
    
    # Check if the SSH command was successful
    if [ $? -eq 0 ]; then
        echo "Hostname of $server: $hostname"
    else
        echo "Failed to connect to $server."
    fi
done
