from . import weather
from .test_data import SAMPLE_DATA, TARGET_SNAPSHOT

#def test_replace_me():
#   assert [{}] == list(weather.process_events([{}]))

def test_add_one_sample():
   weather.process_events([{"type": "sample", 
                           "stationName": "Station A", 
                           "timestamp": 1692000000000, 
                           "temperature": 21.4}])
   assert weather.get_stations() == {"Station A": {"high": 21.4, "low": 21.4}}

#def test_add_samples():
#   assert [TARGET_SNAPSHOT] == list(weather.process_events(SAMPLE_DATA))
