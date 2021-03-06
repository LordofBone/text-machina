### Setup

Standard pip install should work for most platforms and OSes.

`pip install -r requirements.txt`

### Usage

###### Warning

Using GPT-2 to generate text may result in some offensive language or some strange things, so please be aware of that.

Go here to read more:
https://huggingface.co/gpt2#limitations-and-bias

So I can't be responsible for any strange things generated by these pre-trained models.

You should also not use this to do anything other than generate text for fun/robots, don't use it for serious things!

###### Using the GUI

Simply run:
`python run_text_generator_gui.py`

From here you will be able to select models and generate text.

Selecting a model will generate text from that model and also download it.

If you select a model that is currently not downloaded, it will be downloaded automatically.

###### Using text generator from file

Run `python run_text_generator_from_file.py` and it will print out the results of all text generation by using the 
sentences in the text files under the `data/seeds` directory.

###### Integrating with other systems

You can pull down the repo into the folder of the project you are working on, then append the system path of the
text machina folder to the system path of the project.

`text_machina_dir = os.path.join( path_to_text_machina )`

`sys.path.append(text_machina_dir)`

You will also need to install everything in requirements.txt and/or add the requirements to your project's requirements.txt

Then just import everything in
`integrate_text_generation` and call `use_text_generation` with a text input.

Or call `use_text_generation_from_file` to load a text file from the `data/seeds` directory and generate text from the
sentences within the text files there.

###### Configuration

The GUI can be configured by editing the `gui_config.py` file, this allows for resolution etc. to be changed.

The text generator can be configured by editing the `gpt2_config.py` file, this allows for the text generator to be
fine-tuned; you can find out more about the settings here: https://huggingface.co/blog/how-to-generate

### System Requirements

###### CPU
A pretty good quad-core processor is recommended (generally models from 2016 onwards).

I have run this on a Raspberry Pi 4, and it works fine; although it does take a little while to generate.
It may run on older Raspberry Pi's, but I doubt it would run on anything less than a Pi 3.

###### RAM
From what I've observed here is the approximate max RAM usages of the different models:
Small - 1G
Medium - 3G
Large - 6G
Extra Large - 12G>

So please be aware of this when selecting models.

On my Pi400 (4GB RAM) I've been able to run small and medium fine, but large requires some swap configuration to allow 
for the extra memory use. Using a Pi 4 with 8GB RAM should be able to run large models ok without swap though.