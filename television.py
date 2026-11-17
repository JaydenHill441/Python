class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Initializes Television class
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self):
        """
        Will change self.__status variable to False if True
        or True if False
        """
        if self.__status:
            self.__status: bool = False
        else:
            self.__status: bool = True

    def mute(self):
        """
        Will only work if self.__status is True
        Will change self.__muted variable to False if True
        or True if False
        """
        if self.__status:
            if self.__muted:
                self.__muted: bool = False
            else:
                self.__muted: bool = True

    def channel_up(self):
        """
        Will only work if self.__status is True
        This will switch channel up unless channel is self.MAX_CHANNEL
        """
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel: int = self.MIN_CHANNEL

    def channel_down(self):
        """
        Will only work if self.__status is True
        This will switch channel down unless channel is self.MIN_CHANNEL
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel: int = self.MAX_CHANNEL

    def volume_up(self):
        """
        Will only work if self.__status is True
        This will turn volume up unless volume is self.MAX_VOLUME
        Will automatically unmute if volume is increased
        """
        if self.__status:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
                if self.__muted:
                    self.mute()

    def volume_down(self):
        """
        Will only work if self.__status is True
        This will turn volume down unless volume is self.MIN_VOLUME
        Will automatically unmute if volume is lowered
        """
        if self.__status:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
                if self.__muted:
                    self.mute()

    def __str__(self) -> str:
        """
        :return: A string containing the current power status, channel, and volume.
        """
        if self.__muted:
            return f"Power - {self.__status}, Channel - {self.__channel}, Volume - 0"
        else:
            return f"Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}"