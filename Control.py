import serial

def get_setpoint_message(node=128):
    node_string = (node).to_bytes(2, byteorder='big').hex()[2:]
    string = f':06{node_string}0401210121\r\n'
    string_bytes = string.encode('ascii')
    return string_bytes

def get_setpoint(serial, node=128, max_flow=100):
    string_bytes = get_setpoint_message(node)
    serial.write(string_bytes)
    string = serial.read_until()
    setpoint_hex = string[-6:-2]
    setpoint = int(setpoint_hex, 16)
    setpoint = max_flow*setpoint/32000
    
    return setpoint

def get_measure_message(node=128):
    node_string = (node).to_bytes(2, byteorder='big').hex()[2:]
    string = f':06{node_string}0401210120\r\n'
    string_bytes = string.encode('ascii')
    return string_bytes

def get_measure(serial, node=128, max_flow=100):
    string_bytes = get_measure_message(node)
    serial.write(string_bytes)
    string = serial.read_until()
    measure_hex = string[-6:-2]
    measure = int(measure_hex, 16)
    measure = max_flow*measure/32000
    return measure    

def setpoint_write_message(setpoint, node=128, max_flow=100):
    node_string = (node).to_bytes(2, byteorder='big').hex()[2:]
    setpoint_int = int(setpoint*32000/max_flow)
    sp_string = (setpoint_int).to_bytes(2, byteorder='big').hex()
    string = f':06{node_string}010121{sp_string}\r\n'
    string_bytes = string.encode('ascii')
    return string_bytes

def setpoint_write(serial, setpoint, node=128, max_flow=100):
    string_bytes = setpoint_write_message(setpoint, node, max_flow)
    serial.write(string_bytes)
    serial.read_until()
