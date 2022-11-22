"""Constances for testing purposes."""

TEST_HOST = "127.0.0.1"
TEST_PORT = 9883
TEST_USER_NAME = "test"
TEST_PASSWORD = "test_password"
TEST_DEBUG_TRUE = True
TEST_DEBUG_FALSE = False

TEST_INELS_MQTT_NAMESPACE = "inelsmqtt"
TEST_INELS_MQTT_CLASS_NAMESPACE = "inelsmqtt.InelsMqtt"

TEST_SWITCH_TOPIC_STATE = "inels/status/4254524524/02/452454"
TEST_SWITCH_TOPIC_SET = "inels/set/4254524524/02/452454"
TEST_SWITCH_TOPIC_CONNECTED = "inels/connected/4254524524/02/452454"

TEST_SWITCH_WITH_TEMP_TOPIC_STATE = "inels/status/4254524524/07/452454"
TEST_SWITCH_WITH_TEMP_TOPIC_SET = "inels/set/4254524524/07/452454"
TEST_SWITCH_WITH_TEMP_TOPIC_CONNECTED = "inels/connected/4254524524/07/452454"
TEST_SWITCH_WITH_TEMP_STATE_ON_VALUE = b"07\n00\n92\n09\n"
TEST_SWITCH_WITH_TEMP_STATE_OFF_VALUE = b"07\n01\n34\n08\n"

TEST_AVAILABILITY_ON = "on\n"
TEST_AVAILABILITY_OFF = "off\n"

TEST_SENSOR_TOPIC_STATE = "inels/status/4254524524/10/454354"
TEST_SENSOR_TOPIC_CONNECTED = "inels/connected/4254524524/10/454354"
TEST_TEMPERATURE_DATA = b"00\nB4\n0A\n6E\n0A\n"

TEST_LIGHT_DIMMABLE_TOPIC_STATE = "inels/status/4254524524/05/88556633"
TEST_LIGHT_DIMMABLE_CONNECTED = "inels/connected/4254524524/05/88556633"
TEST_LIGH_STATE_HA_VALUE = 20
TEST_LIGH_STATE_INELS_VALUE = b"C9\n4F\n"
TEST_LIGHT_SET_INELS_VALUE = "01 C9 4F"

TEST_COVER_RFJA_12_TOPIC_STATE = "inels/status/4254524524/03/444555225"
TEST_COVER_RFJA_12_TOPIC_CONNECTED = "inels/connected/4254524524/03/444555225"
TEST_COVER_RFJA_12_INELS_STATE_OPEN = b"03\n01\n"
TEST_COVER_RFJA_12_INELS_STATE_CLOSED = b"03\n00\n"
TEST_COVER_RFJA_12_HA_STATE_OPEN = "open"
TEST_COVER_RFJA_12_HA_STATE_CLOSED = "closed"
TEST_COVER_RFJA_12_SET_OPEN = "02 00 00"
TEST_COVER_RFJA_12_SET_CLOSE = "01 00 00"
TEST_COVER_RFJA_12_SET_STOP_UP = "05 00 00"
TEST_COVER_RFJA_12_SET_STOP_DOWN = "03 00 00"

TEST_CLIMATE_RFATV_2_TOPIC_STATE = "inels/status/4254524524/09/4249589"
TEST_CLIMATE_RFATV_2_TOPIC_CONNECTED = "inels/connected/4254524524/09/4249589"
TEST_CLIMATE_RFATV_2_OPEN_TO_40_STATE_VALUE = b"50\n34\n00\n40\n00\n"
TEST_CLIMATE_RFATV_2_SET_VALUE = "00 3C 00"

TEST_BUTTON_RFGB_40_TOPIC_STATE = "inels/status/4254524524/19/10904"
TEST_BUTTON_RFGB_40_TOPIC_CONNECTED = "inels/connected/4254524524/19/10904"
TEST_BUTTON_RFGB_40_STATE_VALUE = b"20\n01\nDA\n23\n54"

# Relay
TEST_RELAY_MAC_ADDRESS = "???"
TEST_RELAY_ADDRESS = "XXXXX"

TEST_RELAY_SA3_01B_TOPIC_STATE = f"inels/status/{TEST_RELAY_MAC_ADDRESS}/100/{TEST_RELAY_ADDRESS}"
TEST_RELAY_SA3_01B_CONNECTED = f"inels/connected/{TEST_RELAY_MAC_ADDRESS}/100/{TEST_RELAY_ADDRESS}"
TEST_RELAY_SA3_01B_STATE_VALUE = b"00\n00\n0A\nC4\n00\n"
#   00  RELAY OFF
#   00  SPARE
#   0A  TEMP (25,00ºC)
#   C4  TEMP (25,00ºC)
#   00  OVERFLOW OFF

# Two channel dimmer
TEST_TWOCHANNELDIMMER_MAC_ADDRESS = "???"
TEST_TWOCHANNELDIMMER_ADDRESS = "XXXXX"

TEST_TWOCHANNELDIMMER_DA3_22M_TOPIC_STATE = f"inels/status/{TEST_TWOCHANNELDIMMER_MAC_ADDRESS}/101/{TEST_TWOCHANNELDIMMER_ADDRESS}"
TEST_TWOCHANNELDIMMER_DA3_22M_CONNECTED = f"inels/connected/{TEST_TWOCHANNELDIMMER_MAC_ADDRESS}/101/{TEST_TWOCHANNELDIMMER_ADDRESS}"
TEST_TWOCHANNELDIMMER_DA3_22M_STATE_VALUE = b"0A\nC4\n00\n00\n00\n00\n"
#   0A  TEMP (25,00ºC)
#   C4  TEMP (25,00ºC)
#   00  INPUTS
#   00  SPARE
#   00  OUT1
#   00  OUT2

# Thermostat
TEST_THERMOSTAT_MAC_ADDRESS = "???"
TEST_THERMOSTAT_ADDRESS = "XXXXX"

TEST_THERMOSTAT_GTR3_50_TOPIC_STATE = f"inels/status/{TEST_THERMOSTAT_MAC_ADDRESS}/102/{TEST_THERMOSTAT_ADDRESS}"
TEST_THERMOSTAT_GTR3_50_CONNECTED = f"inels/connected/{TEST_THERMOSTAT_MAC_ADDRESS}/102/{TEST_THERMOSTAT_ADDRESS}"
TEST_THERMOSTAT_GTR3_50_STATE_VALUE = b"00\n00\n0A\nC4\n00\n00\n00\n00\n00\n00\n00\n00\n00\n00\n00\n00\n00\n00\n"
#   00  RESERVED
#   00  INPUTS
#   0A  TEMP (25,00ºC)
#   C4  TEMP (25,00ºC)
#   00  RESERVED
#   00  RESERVED
#   00  RESERVED
#   00  INPUTS
#   ??  LIGHT-IN
#   ??  LIGHT-IN
#   ??  LIGHT-IN
#   ??  LIGHT-IN
#   ??  AIN
#   ??  AIN
#   ??  HUMIDITY
#   ??  HUMIDITY
#   ??  DEWPOINT
#   ??  DEWPOINT

# Button array
TEST_BUTTONARRAY_MAC_ADDRESS = "???"
TEST_BUTTONARRAY_ADDRESS = "XXXXX"

TEST_BUTTONARRAY_GSB3_90X_TOPIC_STATE = f"inels/status/{TEST_BUTTONARRAY_MAC_ADDRESS}/102/{TEST_BUTTONARRAY_ADDRESS}"
TEST_BUTTONARRAY_GSB3_90X_CONNECTED = f"inels/connected/{TEST_BUTTONARRAY_MAC_ADDRESS}/102/{TEST_BUTTONARRAY_ADDRESS}"
TEST_BUTTONARRAY_GSB3_90X_STATE_VALUE = b"00\n00\n0A\nC4\n00\n00\n00\n00\n00\n00\n00\n00\n00\n00\n"
#   00  INPUTS
#   00  INPUTS
#   0A  TEMP (25,00ºC)
#   C4  TEMP (25,00ºC)
#   ??  LIGHT-IN
#   ??  LIGHT-IN
#   ??  LIGHT-IN
#   ??  LIGHT-IN
#   ??  AIN
#   ??  AIN
#   ??  HUMIDITY
#   ??  HUMIDITY
#   ??  DEWPOINT
#   ??  DEWPOINT