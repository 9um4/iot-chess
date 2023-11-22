from modi import MODI
from modi.module.input_module.gyro import Gyro
from modi.module.output_module.motor import Motor
from modi.module.output_module.led import Led
from modi.module.output_module.speaker import Speaker

import time
import asyncio

from abc import abstractmethod

#TODO: Revive
#TODO: Diagonal Movement
class Piece():

    def __init__(self, bundle: MODI, column_time: float = 3.3, degree_time: float = 1.02) -> None:
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

        self.__is_alive__: bool = True

        self.__is_moving__: bool = False

        self.__previous_acceleration_x__: float = self.__gyro__.acceleration_x
        self.__previous_acceleration_y__: float = self.__gyro__.acceleration_y
        self.__previous_acceleration_z__: float = self.__gyro__.acceleration_z
        
        time.sleep(0.1)

        self.__previous_acceleration_x__: float = self.__gyro__.acceleration_x
        self.__previous_acceleration_y__: float = self.__gyro__.acceleration_y
        self.__previous_acceleration_z__: float = self.__gyro__.acceleration_z

        self.__diff_factor__ = 1

        # await self.__detect_die()

    async def __detect_die__(self):
        """
        가속도의 변화량이 self.__diff_factor__보다 큰 경우 죽은 것으로 간주 (충격 감지)
        """
        while self.__is_alive__:
            time.sleep(0.05)
            diff_x: float = abs(self.__gyro__.acceleration_x - self.__previous_acceleration_x__)
            diff_y: float = abs(self.__gyro__.acceleration_y - self.__previous_acceleration_y__)
            diff_z: float = abs(self.__gyro__.acceleration_z - self.__previous_acceleration_z__)

            self.__previous_acceleration_x__: float = self.__gyro__.acceleration_x
            self.__previous_acceleration_y__: float = self.__gyro__.acceleration_y
            self.__previous_acceleration_z__: float = self.__gyro__.acceleration_z

            diff_size: float = (diff_x ** 2) + (diff_y ** 2) + (diff_z ** 2)

            if (diff_size >= self.__diff_factor__):
                self.__is_alive__ = False
                self.die()
    
    def __forward__(self, length: int = 1) -> None:
        self.__is_moving__ = True
        self.__motor__.first_speed = -50
        self.__motor__.second_speed = 53
        time.sleep(self.__column_time__ * length)
        self.__stop__()

    def __backward__(self, length: int = 1) -> None:
        self.__is_moving__ = True
        self.__motor__.first_speed = 50
        self.__motor__.second_speed = -53
        time.sleep(self.__column_time__ * length)
        self.__stop__()

    def __left__(self, size: int = 1) -> None:
        self.__is_moving__ = True
        self.__motor__.first_speed = 50
        self.__motor__.second_speed = 53
        time.sleep(self.__degree_time__ * size)
        self.__stop__()

    def __right__(self, size: int = 1) -> None:
        self.__is_moving__ = True
        self.__motor__.first_speed = -50
        self.__motor__.second_speed = -53
        time.sleep(self.__degree_time__ * size)
        self.__stop__()

    def __left_diagonal__(self) -> None:
        self.__is_moving__ = True
        self.__motor__.first_speed = 50
        self.__motor__.second_speed = 53
        time.sleep(self.__degree_time__ * 0.5)
        self.__stop__()

    def __right_diagonal__(self) -> None:
        self.__is_moving__ = True
        self.__motor__.first_speed = -50
        self.__motor__.second_speed = -53
        time.sleep(self.__degree_time__ * 0.5)
        self.__stop__()

    def __stop__(self) -> None:
        self.__is_moving__ = False
        self.__motor__.first_speed = 0
        self.__motor__.second_speed = 0

    def move_forward(self, size: int = 1) -> None:
        """
        module이 바라보는 방향으로 size 만큼 이동
        """
        if (self.__is_alive__): self.__forward__(size)
        

    def move_backward(self, size: int = 1) -> None:
        """
        module이 바라보는 반대 방향으로 size 만큼 이동
        """
        if (self.__is_alive__): self.__backward__(size)

    def move_left(self, size: int = 1) -> None:
        """
        module이 바라보는 방향을 기준으로 왼쪽 방향으로 size 만큼 이동
        """
        if (self.__is_alive__):
            self.__left__()
            self.__forward__(size)
            self.__right__()

    def move_right(self, size: int = 1) -> None:
        """
        module이 바라보는 방향을 기준으로 오른쪽 방향으로 size 만큼 이동
        """
        if (self.__is_alive__):
            self.__right__()
            self.__forward__(size)
            self.__left__()

    def die(self) -> None:
        """
        죽음을 감지하였을 때 실행할 메서드
        """
        # print("died!")
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

    def move_left_up(self, size: float) -> None:
        """
        왼쪽 대각선 위로 이동하는 메서드
        """
        self.__left_diagonal__()
        self.__forward__(self.__column_time__ * (2 ** 0.5) * size)
        self.__right_diagonal__()

    def move_right_up(self, size: float) -> None:
        """
        오른쪽 대각선 위로 이동하는 메서드
        """
        self.__right_diagonal__()
        self.__forward__(self.__column_time__ * (2 ** 0.5) * size)
        self.__left_diagonal__()

    def move_left_down(self, size: float) -> None:
        """
        왼쪽 대각선 아래로 이동하는 메서드
        """
        self.__right_diagonal__()
        self.__backward__(self.__column_time__ * (2 ** 0.5) * size)
        self.__left_diagonal__()

    def move_right_down(self, size: float) -> None:
        """
        오른쪽 대각선 아래로 이동하는 메서드
        """
        self.__left_diagonal__()
        self.__backward__(self.__column_time__ * (2 ** 0.5) * size)
        self.__right_diagonal__()


    @abstractmethod
    def move(self, movement: int = 1) -> None:
        """
        말들의 실제 이동을 구현할 메소드
        """
        # self.do_something()
        pass


if __name__ == "__main__":
    piece: Piece = Piece(MODI())
    piece.__left_up__()
