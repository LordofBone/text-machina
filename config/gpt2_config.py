from pathlib import Path
from utils.get_and_set import Property

dataset_dir = Path(__file__).parent.parent / f"data/seeds/"
models_dir = Path(__file__).parent.parent / f"models/gpt/"

gpt2_models = ["gpt2", "gpt2-medium", "gpt2-large"]

gpt2_size = Property()

sampling_enable = True
top_k_setting = 10
top_p_setting = 0.92
num_return_sequences_setting = 3
# not sure if this works within the text-generation pipeline but adding anyway, '0' should mean no seed set
random_seed_setting = 0
temperature_setting = 0.9

output_length = Property()

default_gpt2_size = gpt2_models[0]

gpt2_size.x = default_gpt2_size

output_length.x = 200
