from abc import ABC, abstractmethod
from typing import override


class RemoteControl(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def change_channel(self, channel):
        pass


class BasicRemote(RemoteControl):
    def turn_on(self):
        print("Базовое ДУ: Включение телевизора.")
        self.device.power_on()

    def turn_off(self):
        print("Базовое ДУ: Выключение телевизора.")
        self.device.power_off()

    def volume_up(self):
        print("Базовое ДУ: Увеличение громкости.")
        self.device.increase_volume()

    def volume_down(self):
        print("Базовое ДУ: Уменьшение громкости.")
        self.device.decrease_volume()

    def change_channel(self, channel):
        print(f"Базовое ДУ: Смена канала на {channel}.")
        self.device.set_channel(channel)


class AdvancedRemote(BasicRemote):
    @override
    def turn_on(self):
        print("Продвинутое ДУ: Включение телевизора.")
        self.device.power_on()

    @override
    def turn_off(self):
        print("Продвинутое ДУ: Выключение телевизора.")
        self.device.power_off()

    @override
    def volume_up(self):
        print("Продвинутое ДУ: Увеличение громкости.")
        self.device.increase_volume()

    @override
    def volume_down(self):
        print("Продвинутое ДУ: Уменьшение громкости.")
        self.device.decrease_volume()

    @override
    def change_channel(self, channel):
        print(f"Продвинутое ДУ: Смена канала на {channel}.")
        self.device.set_channel(channel)

    def mute(self):
        print("Продвинутое ДУ: Отключение звука.")
        self.device.mute()


class TV(ABC):
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.volume = 10
        self.channel = 1

    def power_on(self):
        self.is_on = True
        print(f"{self.brand}: Телевизор включен.")

    def power_off(self):
        self.is_on = False
        print(f"{self.brand}: Телевизор выключен.")

    def increase_volume(self):
        if self.is_on:
            self.volume += 1
            print(f"{self.brand}: Громкость увеличена до {self.volume}.")

    def decrease_volume(self):
        if self.is_on and self.volume > 0:
            self.volume -= 1
            print(f"{self.brand}: Громкость уменьшена до {self.volume}.")

    def mute(self):
        if self.is_on and self.volume > 0:
            self.volume = 0
            print(f"{self.brand}: Громкость уменьшена до {self.volume}.")

    def set_channel(self, channel):
        if self.is_on:
            self.channel = channel
            print(f"{self.brand}: Канал переключен на {self.channel}.")


class SamsungTV(TV):
    def __init__(self):
        super().__init__("Samsung")


class SonyTV(TV):
    def __init__(self):
        super().__init__("Sony")


def main():
    samsung_tv = SamsungTV()
    sony_tv = SonyTV()

    basic_remote = BasicRemote(samsung_tv)
    advanced_remote = AdvancedRemote(sony_tv)

    basic_remote.turn_on()
    basic_remote.volume_up()
    basic_remote.change_channel(5)
    basic_remote.turn_off()

    print()

    advanced_remote.turn_on()
    advanced_remote.mute()
    advanced_remote.change_channel(10)
    advanced_remote.turn_off()


if __name__ == "__main__":
    main()
