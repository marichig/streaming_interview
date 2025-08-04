import json
import sys
import weather
from test_data import SAMPLE_DATA

def generate_input():
    for line in sys.stdin:
        yield json.loads(line)

for output in weather.process_events(generate_input()):
    print(json.dumps(output))

