import datetime as date

# Block Reward


class Utils:
    BLOCK_REWARD = 10

    @staticmethod
    def to_json():
        return {
            "block_reward": Utils.BLOCK_REWARD
            # More settings
        }

    @staticmethod
    def from_json(json_data):
        if "block_reward" in json_data:
            Utils.BLOCK_REWARD = json_data["block_reward"]
