#!/bin/bash

THRESHOLD_PERCENT=90

# Get the current disk utilization for the / volume
CURRENT_PERCENT=$(df -h / | awk 'NR==2 {print $5}' | cut -d'%' -f1)

# Check if the current utilization exceeds the threshold
if [ "$CURRENT_PERCENT" -gt "$THRESHOLD_PERCENT" ]; then
    # Log the warning message
    echo "$(date +"%Y-%m-%d %H:%M:%S") - WARNING: Disk utilization exceeded ${THRESHOLD_PERCENT}%" >> /var/log/disk.log
fi
