from pathlib import Path
from utils.get_and_set import Property

dataset_dir = Path(__file__).parent.parent / f"data/seeds/"
models_dir = Path(__file__).parent.parent / f"models/gpt/"

gpt2_models = ["gpt2", "gpt2-medium", "gpt2-large"]

gpt2_size = Property()

output_length = Property()

default_gpt2_size = gpt2_models[0]

gpt2_size.x = default_gpt2_size

output_length.x = 200
