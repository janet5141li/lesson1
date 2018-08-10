from gpiozero import RGBLED
from time import sleep


if __name__== "__main__":
    rgbled = RGBLED(17, 27, 22);
    while True:
        print("run");
        rgbled.color = (1,0,0);
        sleep(0.1);
        rgbled.off();
        sleep(0.1);
        rgbled.color = (0,1,0);
        sleep(0.1);
        rgbled.off();
        sleep(0.1);
        rgbled.color = (0,0,1);
        sleep(0.1);
        rgbled.off();
        sleep(0.1);
