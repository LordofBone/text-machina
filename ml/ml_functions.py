from config.gpt2_config import dataset_dir
from ml.run_text_completion import text_generator
from utils.load_bar_non_iterable import progress_bar


@progress_bar(expected_time=120, description="Generating Sentence...")
def run_text_generation_from_file():
    """
    Generate text from seed data.
    This will go through the sentences under data/seeds/seed_sentences.txt and generate a new sentence for each.
    :return:
    """
    output_string = ""

    with open(f'{dataset_dir}/seed_sentences.txt') as f:
        lines = f.readlines()

    for line in lines:
        output_string = output_string + f"{(text_generator(prefix_text=line))}\n"

    return output_string


def run_text_generation(input_text):
    """
    Generate text from input text.
    :param input_text:
    :return:
    """
    updates = [input_text, text_generator(prefix_text=input_text)]

    return updates
