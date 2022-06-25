from transformers import pipeline

from config.gpt2_config import *


# https://huggingface.co/blog/how-to-generate
def text_generator(prefix_text="this is an example sentence"):
    """
    Sets up a text-generation pipeline.
    Uses the GPT2 model to generate text.
    :param prefix_text:
    :return:
    """
    text_generation = pipeline(task="text-generation", model=f"{models_dir}/{gpt2_size.x}",
                               tokenizer=f"{models_dir}/{gpt2_size.x}")
    generated_text = text_generation(prefix_text,
                                     max_length=output_length.x,
                                     do_sample=sampling_enable,
                                     top_k=top_k_setting,
                                     top_p=top_p_setting,
                                     random_seed=random_seed_setting,
                                     temperature=temperature_setting,
                                     no_repeat_ngram_size=no_repeat_ngram_size_setting,
                                     num_return_sequences=num_return_sequences_setting)[0]
    return generated_text['generated_text']


if __name__ == "__main__":
    print(text_generator())
