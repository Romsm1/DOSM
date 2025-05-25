class Seconds:
    def __init__(self, seconds):
        self._seconds = seconds

    def __str__(self):
        return f'{self._seconds}s.'

    def __int__(self):
        return self._seconds


class Minutes:
    def __init__(self, minutes):
        self._minutes = minutes

    def __str__(self):
        return f'{self._minutes}m.'

    def __int__(self):
        return self._minutes


class Hours:
    def __init__(self, hours):
        self._hours = hours

    def __str__(self):
        return f'{self._hours}h.'

    def __int__(self):
        return self._hours 

class Time(Seconds, Minutes, Hours):
    def __init__(self, hours=0, minutes=0, seconds=0):
        Seconds.__init__(self, seconds)
        Minutes.__init__(self, minutes)
        Hours.__init__(self, hours)

    def __str__(self):
        return f"{self._hours}h {self._minutes}m {self._seconds}s"

    def __add__(self, other):
        total_seconds = self.total_seconds() + other.total_seconds()
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

    def __sub__(self, other):
        total_seconds = self.total_seconds() - other.total_seconds()
        total_seconds = max(total_seconds, 0)
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

    def __eq__(self, other):
        return self.total_seconds() == other.total_seconds()

    def total_seconds(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds