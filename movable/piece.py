from modi import MODI
from modi.module.input_module.gyro import Gyro
from modi.module.output_module.motor import Motor
from modi.module.output_module.led import Led
from modi.module.output_module.speaker import Speaker

import time

#TODO: Gyro Censor
#TODO: Die State
#TODO: Detect Die
#TODO: Revive
#TODO: Diagonal Movement
class Piece():

    def __init__(self, bundle: MODI, column_time: float = 1.0, degree_time: float = 1.02) -> None:
        self.__bundle__: MODI = bundle

        self.__column_time__: float = column_time

        self.__degree_time__: float = degree_time

        self.__motor__: Motor = bundle.motors[0]
        self.__motor__.first_speed = 0
        self.__motor__.second_speed = 0

        self.__led__: Led = bundle.leds[0]
        self.__led__.turn_off()

        self.__speaker__: Speaker = bundle.speakers[0]

        self.__gyro__: Gyro = bundle.gyros[0]

    
    def __forward__(self, length: int = 1) -> None:
        self.__motor__.first_speed = -50
        self.__motor__.second_speed = 55
        time.sleep(self.__column_time__ * length)
        self.__stop__()

    def __backward__(self, length: int = 1) -> None:
        self.__motor__.first_speed = 50
        self.__motor__.second_speed = -55
        time.sleep(self.__column_time__ * length)
        self.__stop__()

    def __left__(self, size: int = 1) -> None:
        self.__motor__.first_speed = 50
        self.__motor__.second_speed = 53
        time.sleep(self.__degree_time__ * size)
        self.__stop__()

    def __right__(self, size: int = 1) -> None:
        self.__motor__.first_speed = -50
        self.__motor__.second_speed = -55
        time.sleep(self.__degree_time__ * size)
        self.__stop__()

    def __stop__(self) -> None:
        self.__motor__.first_speed = 0
        self.__motor__.second_speed = 0

    def move_forward(self, size: int = 1) -> None:
        self.__forward__(size)

    def move_backward(self, size: int = 1) -> None:
        self.__backward__(size)

    def move_left(self, size: int = 1) -> None:
        self.__left__()
        self.__forward__(size)
        self.__right__()

    def move_right(self, size: int = 1) -> None:
        self.__right__()
        self.__forward__(size)
        self.__left__()

    def die(self) -> None:
        self.__led__.red = 100
        self.__speaker__.tune = 880, 50
        time.sleep(0.75)
        self.__led__.turn_off()
        self.__speaker__.turn_off()
        time.sleep(0.25)
        self.__led__.red = 100
        self.__speaker__.tune = 880, 50
        time.sleep(0.75)
        self.__led__.turn_off()
        self.__speaker__.turn_off()
        time.sleep(0.25)
        self.__led__.red = 100
        self.__speaker__.tune = 880, 50
        time.sleep(0.75)
        self.__led__.turn_off()
        self.__speaker__.turn_off()


if __name__ == "__main__":
    piece: Piece = Piece(MODI())
    # 테스트할 코드 입력
