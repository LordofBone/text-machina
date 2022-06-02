from ml.download_model import get_and_save_models
from config.gpt2_config import gpt2_models, gpt2_size

if __name__ == "__main__":
    for model in gpt2_models:
        gpt2_size.x = model
        get_and_save_models()
