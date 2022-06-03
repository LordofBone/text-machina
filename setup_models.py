from ml.download_model import get_and_save_models
from config.gpt2_config import gpt2_models, gpt2_size


def get_and_save_all_models():
    """
    Downloads the GPT2 models if they don't already exist.
    """
    for model in gpt2_models:
        gpt2_size.x = model
        get_and_save_models()


if __name__ == "__main__":
    get_and_save_all_models()
