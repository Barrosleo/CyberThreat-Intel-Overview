#!/usr/bin/env python3
import json
import datetime

def collect_data():
    """
    Simulate the data collection phase by returning dummy threat intelligence data.
    In a real-world scenario, this function might fetch data from public APIs or read log files.
    """
    data = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "indicator": "1.2.3.4",
        "description": "Suspicious IP address observed in simulated threat feed",
        "source": "Dummy Threat Feed"
    }
    return data

if __name__ == '__main__':
    collected_data = collect_data()
    print("Collected Data:")
    print(json.dumps(collected_data, indent=2))
