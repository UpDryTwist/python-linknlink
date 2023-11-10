import linknlink as llk

ip = "192.168.2.104"

device = llk.hello(ip)
print(device.host)
print(device.mac)
print(device.devtype)
print(device.is_locked)

# device unlock
device.set_lock(True)
print(device.is_locked)