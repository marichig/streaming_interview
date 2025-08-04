from . import weather
from .test_data import (
   SAMPLE_DATA_1, TARGET_SNAPSHOT_1, TARGET_RESET_1, ONE_SAMPLE_SNAPSHOT, ONE_SAMPLE,
   BAD_MESSAGE_TYPE, BAD_CONTROL, MIXED_MESSAGES_SNAPSHOT_1, MIXED_MESSAGES_RESET, 
   MIXED_MESSAGES_SNAPSHOT_2, MIXED_MESSAGES
)
from .constants import CONTROL_SNAPSHOT, CONTROL_RESET

def test_empty_message():
   try:
      list(weather.process_events([{}]))
      assert False, "Expected an error in this text"
   except Exception as e:
      assert "Received message with no type field" in str(e), f"Value Error Message: {e}"

def test_add_one_sample():
   assert [ONE_SAMPLE_SNAPSHOT] == list(weather.process_events([ONE_SAMPLE, CONTROL_SNAPSHOT]))

def test_add_samples():
   assert [TARGET_SNAPSHOT_1] == list(weather.process_events(SAMPLE_DATA_1 + [CONTROL_SNAPSHOT]))

def test_reset():
   assert [TARGET_RESET_1] == list(weather.process_events(SAMPLE_DATA_1 + [CONTROL_RESET]))

def test_mixed_messages():
   assert [MIXED_MESSAGES_SNAPSHOT_1, MIXED_MESSAGES_RESET, MIXED_MESSAGES_SNAPSHOT_2] == list(
      weather.process_events(MIXED_MESSAGES)
   )

def test_snapshot_with_no_data():
   assert [{"type":"snapshot", "asOf": None, "stations":{}}] == list(weather.process_events([CONTROL_SNAPSHOT]))

def test_reset_then_snapshot_with_no_data():
   # should take the convention of returning None's when there is no data entered
   # could throw the user a warning letting them know taking snapshot of no actual data
   assert [{"type":"reset", "asOf": None},
           {"type":"snapshot", "asOf": None, "stations":{}}] == list(
              weather.process_events([CONTROL_RESET, CONTROL_SNAPSHOT])
           )
   
def test_bad_message_type():
   try:
      list(weather.process_events([BAD_MESSAGE_TYPE]))
      assert False, "Expected an error in this text"
   except Exception as e:
      assert BAD_MESSAGE_TYPE["type"] in str(e), f"Value Error Message: {e}"

def test_bad_control_type():
   try:
      list(weather.process_events([BAD_CONTROL]))
      assert False, "Expected an error in this text"
   except Exception as e:
      assert BAD_CONTROL["command"] in str(e), f"Value Error Message: {e}"
