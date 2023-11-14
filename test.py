import linknlink as llk

ip = "192.168.2.104"
code_ehub = 0x520B 
code_eths = 0xAC7C
code_motion = 0xAC7B

dev = llk.hello(ip)
print("device:", dev)

device = llk.gendevice(
    code_ehub,
    dev.host,
    dev.mac,
)

ee = llk.ehub(
    device.host,
    device.mac,
    device.devtype,
    device.timeout,
    device.name,
    device.model,
    device.manufacturer,
    device.is_locked,
)
print(ee.auth())
print(ee.check_sensors())
# print(ee.check_pir())