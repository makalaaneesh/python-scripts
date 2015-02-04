import uinput
import time
device = uinput.Device([
        uinput.KEY_E,
        uinput.KEY_H,
        uinput.KEY_L,
        uinput.KEY_O,
        uinput.KEY_TAB,
        uinput.KEY_ENTER,
        ])

time.sleep(5)
for x in range(0,8):
	device.emit_click(uinput.KEY_TAB)
device.emit_click(uinput.KEY_ENTER)
	
# device.emit_click(uinput.KEY_H)
# device.emit_click(uinput.KEY_E)
# device.emit_click(uinput.KEY_L)
# device.emit_click(uinput.KEY_L)
# device.emit_click(uinput.KEY_O)

