import os
import subprocess

def forget_device():
    # Device instance path could be found in the device's properties on Device Manager
    # It should be replaced with the actual path of your Google Pixel Buds Pro
    device_instance_id = 'BTHENUM\DEV_242934B43969\8&376E68D0&0&BLUETOOTHDEVICE_242934B43969'


    # Disabling the device
    subprocess.run('devcon disable "{}"'.format(device_instance_id), shell=True)

    # Enabling the device again which simulates the forget process
    # subprocess.run('devcon enable "{}"'.format(device_instance_id), shell=True)

def open_bluetooth_settings():
    # Opening the Bluetooth & Devices settings menu
    os.system('start ms-settings:bluetooth')

if __name__ == "__main__":
    forget_device()
    open_bluetooth_settings()
