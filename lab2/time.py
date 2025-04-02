class Seconds:
    def __init__(self, seconds):
        self._seconds = seconds

    def __str__(self):
        return f'{self._seconds}s.'

    def __int__(self):
        return self._seconds

class Minutes:
    def __init__(self, minutes):
        self.minutes = minutes

    def __str__(self):
        return f'{self.minutes}m.'

    def __int__(self):
        return self.minutes

class  Hours:
    def __init__(self, hours):
        self._hours = hours

    def __str__(self):
        return f'{self._hours}h.'

    def __int__(self):
        return {self._hours}


class Time(Seconds, Minutes, Hours):
    def __init__(self, hours=0, minutes=0, seconds=0):
        Seconds.__init__(self, seconds)
        Minutes.__init__(self, minutes)
        Hours.__init__(self, hours)

    def __str__(self):
        return