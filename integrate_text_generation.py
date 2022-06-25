from ml.ml_functions import run_text_generation
from ml.ml_functions import run_text_generation_from_file
from config.gpt2_config import gpt2_models, gpt2_size


def change_gpt2_model(model_name='gpt2'):
    if model_name not in gpt2_models:
        raise ValueError("Invalid model. Expected one of: %s" % gpt2_models)
    else:
        gpt2_size.x = model_name


def use_text_generation(input_text):
    return run_text_generation(input_text)


def use_text_generation_from_file():
    return run_text_generation_from_file()


if __name__ == "__main__":
    change_gpt2_model('gpt2-medium')
    print(use_text_generation('this is an example sentence')[1])
