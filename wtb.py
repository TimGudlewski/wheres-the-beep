from evdev import InputDevice, UInput, list_devices, ecodes as e


def device_write_pcspkr(d):
    d.write(e.EV_SND, e.SND_BELL, 1)
    d.write(e.EV_SYN, e.SYN_REPORT, 0)
    d.close()


def ui_write_pcspkr(d):
    ui = UInput.from_device(d)
    ui.write(e.EV_SND, e.SND_BELL, 1)
    ui.syn()
    ui.close()


def main():
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
        print_string = "NAME: {}\n\nPATH: {}\n\nFD: {}\n\nINFO: {}\n"
        print(print_string.format(device.name,
                                  device.path,
                                  device.fd,
                                  device.info))
    pcspkr = InputDevice('/dev/input/event7')
    device_write_pcspkr(pcspkr)


main()
