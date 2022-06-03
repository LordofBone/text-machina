from config.gpt2_config import dataset_dir
from ml.run_sentence_completion import sentence_completer
from utils.load_bar_non_iterable import progress_bar


@progress_bar(expected_time=120, description="Generating Sentence...")
def run_sentence_completion_from_file():
    """
    Generate text from seed data.
    This will go through the sentences under data/seeds/seed_sentences.txt and generate a new sentence for each.
    :return:
    """
    output_string = ""

    with open(f'{dataset_dir}/seed_sentences.txt') as f:
        lines = f.readlines()

    for line in lines:
        output_string = output_string + f"{(sentence_completer(prefix_text=line))}\n"

    return output_string


def run_sentence_completion(input_text):
    """
    Generate text from input text.
    :param input_text:
    :return:
    """
    updates = [input_text, sentence_completer(prefix_text=input_text)]

    return updates
