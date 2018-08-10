from gpiozero import RGBLED
from time import sleep

colors = [(1,0,0),(0,1,0),(0,0,1),
          (1,1,0),(1,0,1),(1,1,1)
          ];
if __name__ == "__main__":
    rgbled = RGBLED(17, 27, 22);
    while True:
       for color in colors:
           rgbled.color = color;
           sleep(0.1);
           rgbled.off();
           sleep(0.1);
