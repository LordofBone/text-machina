from transformers import pipeline

from config.gpt2_config import models_dir, gpt2_size, output_length


def sentence_completer(prefix_text="this is an example sentence", sample=True):
    text_generation = pipeline(task="text-generation", model=f"{models_dir}/{gpt2_size.x}",
                               tokenizer=f"{models_dir}/{gpt2_size.x}")
    generated_text = text_generation(prefix_text, max_length=output_length.x, do_sample=sample)[0]
    return generated_text['generated_text']


if __name__ == "__main__":
    print(sentence_completer())
