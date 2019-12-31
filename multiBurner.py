#!/usr/bin/python3
import pyudev
import subprocess

def device():
    context = pyudev.Context()
    dev_name = []
    for device in context.list_devices(DEVTYPE='disk'):
        major = device.properties['MAJOR']
        if major == '8' or major == '3':
            #print (f"{device.device_node}, ({device.device_type}), {major}, {device}")
            if "usb" in device.device_path:
                print(f"{device.device_node}")
                dev_name.append(device.device_node)

    last_letter = []
    of_string = ""
    for i in range(len(dev_name)):
        last_letter.append(dev_name[i][-1:])
    for i in range(len(last_letter)):
        of_string += "of=/dev/sd" + last_letter[i] + " "

    subprocess.Popen("dcfldd if=IMAGE_NAME.img " + of_string, stdout=subprocess.PIPE, shell=True).wait()


if __name__ == "__main__":
    device()