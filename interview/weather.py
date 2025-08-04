from typing import Any, Iterable, Generator
import json
from .constants import (
    TYPE,
    STATION_NAME,
    TIMESTAMP,
    TEMPERATURE,
    COMMAND,
    AS_OF,
    STATIONS,
    HIGH,
    LOW,
    SAMPLE,
    CONTROL,
    SNAPSHOT,
    RESET,
)


latest_timestamp = None
stations = {}

def process_events(events: Iterable[dict[str, Any]]) -> Generator[dict[str, Any], None, None]:
    # reset global data before running
    # in actual system would need to address storing state in between runs
    update_timestamp(None)
    reset_stations()

    for line in events:
        if line[TYPE] == SAMPLE:
            update_timestamp(line[TIMESTAMP])
            process_sample(line)
        elif line[TYPE] == CONTROL:
            yield process_control(line)
        else:
            raise ValueError("Did not recognize type input:" + line[TYPE] + 
                             " in message received after time: " + 
                             str(latest_timestamp) + ". Proceeding.")
        
def process_sample(sample: dict[str, Any]):
    station = sample[STATION_NAME]
    temperature = sample[TEMPERATURE]

    if station in stations:
        if temperature > stations[station][HIGH]:
            stations[station][HIGH] = temperature
        elif temperature < stations[station][LOW]:
            stations[station[LOW]] = temperature
    else:
        stations[station] = {HIGH: temperature, LOW: temperature}

def process_control(message: dict[str, Any]) -> dict[str,Any]:
    if message[COMMAND] == SNAPSHOT:
        return __snapshot_builder()
    if message[COMMAND] == RESET:
        reset_stations()
        return __reset_builder()
    raise ValueError("Did not recognize command input:" + message[COMMAND] +
                     " in command message received after time: " 
                     + str(latest_timestamp) + ". Proceeding.")

def reset_stations():
    global stations
    stations = {}

def update_timestamp(timestamp):
    global latest_timestamp
    latest_timestamp = timestamp

def __snapshot_builder():
    #return json.dumps({TYPE: SNAPSHOT, AS_OF: latest_timestamp, STATIONS: stations})
    return {TYPE: SNAPSHOT, AS_OF: latest_timestamp, STATIONS: stations}

def __reset_builder():
    #return #json.dumps({TYPE: RESET, AS_OF: latest_timestamp})
    return {TYPE: RESET, AS_OF: latest_timestamp}

def get_stations():
    return stations

def get_timestamp():
    return latest_timestamp
