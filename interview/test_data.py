#### SAMPLE_DATA_1: Build correct snapshot; correct resets / snapshot at very end
### Sample message

from .constants import CONTROL_SNAPSHOT, CONTROL_RESET

SAMPLE_DATA_1 = [
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000000000, "temperature": 21.4},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000005000, "temperature": 16.9},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000010000, "temperature": 19.2},
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000015000, "temperature": 21.6},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000020000, "temperature": 19.4},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000025000, "temperature": 17.0},
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000030000, "temperature": 21.7},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000035000, "temperature": 19.5},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000040000, "temperature": 17.3},
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000045000, "temperature": 21.9},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000050000, "temperature": 17.5},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000055000, "temperature": 19.6},
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000060000, "temperature": 22.0},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000065000, "temperature": 19.7},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000070000, "temperature": 17.8}
]

TARGET_SNAPSHOT_1 = {"type": "snapshot", "asOf": 1692000070000, 
        "stations":{
            "Station A": {"low": 21.4, "high": 22.0},
            "Station B": {"low": 19.2, "high": 19.7},
            "Station C": {"low": 16.9, "high": 17.8}
        }
}

TARGET_RESET_1 = {"type":"reset", "asOf": 1692000070000}

#### Test 2: Add one sample

ONE_SAMPLE = {"type": "sample", 
                           "stationName": "Station A", 
                           "timestamp": 1692000000000, 
                           "temperature": 21.4}

ONE_SAMPLE_SNAPSHOT = {"type": "snapshot", "asOf": 1692000000000, 
        "stations":{
            "Station A": {"low": 21.4, "high": 21.4}
        }
      }

BAD_MESSAGE_TYPE = {"type": "jeronimo"}

BAD_CONTROL = {"type":"control", "command": "do that thang"}

MIXED_MESSAGES = [
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000000000, "temperature": 21.4},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000005000, "temperature": 16.9},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000010000, "temperature": 19.2},
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000015000, "temperature": 21.6},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000020000, "temperature": 19.4},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000025000, "temperature": 17.0},
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000030000, "temperature": 21.7},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000035000, "temperature": 19.5},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000040000, "temperature": 17.3},
  CONTROL_SNAPSHOT, #{A: 21.4, 21.7; B: 19.2, 19.5; C: 16.9, 17.3}
  CONTROL_RESET, #{asOf: 1692000040000}
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000045000, "temperature": 21.9},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000050000, "temperature": 17.5},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000055000, "temperature": 19.6},
  {"type": "sample", "stationName": "Station A", "timestamp": 1692000060000, "temperature": 22.0},
  {"type": "sample", "stationName": "Station B", "timestamp": 1692000065000, "temperature": 19.7},
  {"type": "sample", "stationName": "Station C", "timestamp": 1692000070000, "temperature": 17.8},
  CONTROL_SNAPSHOT #{A: 21.9, 22.0; B: 19.6, 19.7; C: 17.5, 17.8}
]

MIXED_MESSAGES_SNAPSHOT_1 = {"type": "snapshot", "asOf": 1692000040000, 
        "stations":{
            "Station A": {"low": 21.4, "high": 21.7},
            "Station B": {"low": 19.2, "high": 19.5},
            "Station C": {"low": 16.9, "high": 17.3}
        }
      }

MIXED_MESSAGES_RESET = {"type":"reset", "asOf": 1692000040000}

MIXED_MESSAGES_SNAPSHOT_2 = {"type": "snapshot", "asOf": 1692000070000, 
        "stations":{
            "Station A": {"low": 21.9, "high": 22.0},
            "Station B": {"low": 19.6, "high": 19.7},
            "Station C": {"low": 17.5, "high": 17.8}
        }
      }