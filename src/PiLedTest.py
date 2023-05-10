import time
from hal import hal_led as led
from hal import hal_input_switch as switch


def blink_led(delay):
    # Led Blink
    for i in range(5):
        led.set_output(0, 1)
        time.sleep(delay)

        led.set_output(0, 0)
        time.sleep(delay)


def main():
    switch.init()
    led.init()
    while True:
        if switch.read_slide_switch():
            print("Left, 5Hz")
            blink_led(0.2)
        else:
            blink_led(2)
           

if __name__ == "__main__":
    main()

