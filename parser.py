import json
from collections import Counter
import argparse

def load_alerts(filepath):
    alerts = []
    with open(filepath, 'r') as f:
        for line in f: 
            try: 
                event = json.loads(line)
                if event.get('event_type') == 'alert':
                    alerts.append(event)
                        continue
    return alerts