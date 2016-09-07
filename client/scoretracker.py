class ScoreTracker:

    __default = None

    @classmethod
    def default(cls):
        """
        Creates an instance based on default settings.
        :return         ScoreTracker instance
        """
        if cls.__default is None:
            cls.__default = ScoreTracker(1200, 5, 1000)

        return cls.__default

    def complete_station(self, station_number):
        """
        Marks a station as complete
        station_number  int     number of the station to mark complete
        :return         bool    whether the entire game is complete
        """
        self.stations[station_number - 1] = self.timer
        self.drain_rate -= 1
        return self.drain_rate <= 0

    def get_lap_times(self):
        """
        Returns a list of lap times for each completed station. Incomplete times are marked as None.
        :return         int[]   list of the lap times for each completed station.
        """
        return self.timer

    def get_completed(self):
        """
        Returns a list of completed stations.
        :return         bool[]  list of completed stations
        """
        return [time > -1 for time in self.timer]

    def get_score(self, as_str=False):
        """
        Gets the current score.
        as_str          bool    whether to return as a string or not
        :return         int/str current score
        """
        return str(self.score) if as_str else self.score

    def get_time(self):
        """
        Gets the current time
        :return         str     current time formatted as mm:ss
        """
        return "{0!s:02d}:{1!s:02d}".format(self.timer // 60, self.timer % 60)

    def tick(self):
        """
        Advances everything by 1 second.
        :return         bool    whether the game is up.
        """
        self.score -= self.drain_rate
        self.timer -= 1
        return self.timer <= 0

    def __init__(self, time_limit, stations, multiplier, start_override=None):
        """
        Creates an instance of a custom score tracker.
        time_limit      int     time limit in seconds
        stations        int     number of stations
        multiplier      int     multiply the number of points
        start_override  None    use the default number of points
                        int     start with this number instead
        """
        self.initial_score = start_override if start_override else time_limit * stations
        self.score = self.initial_score

        self.drain_rate = stations
        self.stations = [None,] * stations
        self.timer = time_limit