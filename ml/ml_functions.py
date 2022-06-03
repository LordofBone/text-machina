from config.gpt2_config import dataset_dir
from ml.run_sentence_completion import sentence_completer
from utils.load_bar_non_iterable import progress_bar


@progress_bar(expected_time=120, description="Generating Sentence...")
def generate_morning_updates_from_seed():
    updates = []

    with open(f'{dataset_dir}/updates.txt') as f:
        lines = f.readlines()

    for line in lines:
        updates.append(sentence_completer(prefix_text=line, sample=True))

    return updates


def run_sentence_completion(input_text):
    updates = [input_text, sentence_completer(prefix_text=input_text, sample=True)]

    return updates
