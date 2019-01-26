import osrparse

from replay import Replay

class LocalReplay(Replay):
    """
    A replay created from a local .osr file.

    See Also:
        Replay
        OnlineReplay
    """

    def __init__(self, replay_data, player_name):
        """
        Initializes a LocalReplay instance.

        Unless you know what you're doing, don't call this method manually -
        this is intented to be called internally by LocalReplay.from_path.
        """

        Replay.__init__(self, replay_data, player_name)


    @staticmethod
    def from_path(path):
        """
        Creates a Replay instance from the data contained by file at the given path.

        Args:
            [String or Path] path: The absolute path to the replay file.

        Returns:
            The Replay instance created from the given path.
        """

        parsed_replay = osrparse.parse_replay_file(path)
        check_replay_data = parsed_replay.play_data
        player_name = parsed_replay.player_name

        return LocalReplay(check_replay_data, player_name)
