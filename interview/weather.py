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


latest_timestamp = -1
stations = {}

def process_events(events: Iterable[dict[str, Any]]) -> Generator[dict[str, Any], None, None]:
    for line in events:
        if line[TYPE] == SAMPLE:
            latest_timestamp = line[TIMESTAMP]
            process_sample(line)
        if line[TYPE] == CONTROL:
            yield process_control(line)
        else:
            raise Exception #fill in later
        
def process_sample(sample: dict[str, Any]):
    station = sample[STATION_NAME]
    temperature = sample[TEMPERATURE]

    if station in stations:
        if temperature > stations[stations][HIGH]:
            stations[station][HIGH] = temperature
        elif temperature < stations[station[LOW]]:
            stations[station[LOW]] = temperature
    else:
        stations[station] = {HIGH: temperature, LOW: temperature}


def process_control(message: dict[str, Any]) -> dict[str,Any]:
    return {}
