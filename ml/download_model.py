from transformers import GPT2Tokenizer, GPT2Model

from config.gpt2_config import models_dir, gpt2_size


def get_and_save_models():
    tokenizer = GPT2Tokenizer.from_pretrained(gpt2_size.x)
    model = GPT2Model.from_pretrained(gpt2_size.x)

    model.save_pretrained(f'{models_dir}/{gpt2_size.x}')
    tokenizer.save_pretrained(f'{models_dir}/{gpt2_size.x}')


if __name__ == "__main__":
    get_and_save_models()
