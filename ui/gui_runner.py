import threading
import tkinter as tk
from pathlib import Path
from tkinter import *
from tkinter import ttk

from config.gui_config import *
from config.gpt2_config import gpt2_models, gpt2_size, output_length
from ml.ml_functions import run_sentence_completion
from ml.download_model import get_and_save_models


class GUIController:
    def __init__(self):
        """
        Initializes the GUI.
        """
        self.root = Tk()

        self.root.title(window_title)

        self.root.configure(bg=window_background_colour)

        self.root.wm_state(window_setting)

        self.root.geometry(resolution)

        self.style = ttk.Style(self.root)

        self.style.theme_use("clam")

        self.person_reply = tk.StringVar()

        self.ui_output_length = tk.IntVar()

        self.ui_output_length.set(output_length.x)

        self.updates = []

        self.ind = 0
        self.prev_ind = 0

        self.frame_style = ttk.Style()
        self.frame_style.configure('TLabelframe', background=window_background_colour)

        self.main_frame = ttk.LabelFrame(self.root)
        self.main_frame.pack(side="bottom", fill="both", expand="yes")
        self.main_frame.config(text="Enter Text to Complete")

        self.text_output = Text(self.root, height=100, width=200)
        self.text_output.pack(side="top")
        self.text_output.configure(background=item_colours, foreground=text_colour)

        self.text_entry = ttk.Entry(self.main_frame, textvariable=self.person_reply)
        self.text_entry.pack(side="bottom")
        self.text_entry.configure(width=100)
        self.text_entry.focus()

        self.validate_cmd = (self.main_frame.register(self.validate),
                             '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.length_entry = ttk.Entry(self.main_frame, textvariable=self.ui_output_length, validate='key',
                                      validatecommand=self.validate_cmd)
        self.length_entry.pack(side="bottom")
        self.length_entry.configure(width=5)

        self.model_option = StringVar(self.main_frame)

        self.model_option_drop = ttk.OptionMenu(self.main_frame, self.model_option, gpt2_size.x,
                                                command=self.change_model,
                                                *gpt2_models)
        self.model_option_drop.pack(side="right")

        self.generate_button = ttk.Button(self.main_frame, text="Generate",
                                          command=self.generate_button_threader)
        self.generate_button.pack(side="left")

        self.download_button = ttk.Button(self.main_frame, text="Download",
                                          command=self.download_button_threader)
        self.download_button.pack(side="right")

        self.progress_bar = ttk.Progressbar(self.main_frame, orient="horizontal", length=500,
                                            mode="indeterminate")
        self.progress_bar.pack(side="top")

        self.root.bind('<Return>', lambda event: self.generate_button_threader())

        self.path = Path(__file__).parent / "../images"

        self.label = Label(self.root)

    # thanks to https://stackoverflow.com/questions/8959815/restricting-the-value-in-tkinter-entry-widget
    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        """
        Validates the input of the text output length entry.
        :param action:
        :param index:
        :param value_if_allowed:
        :param prior_value:
        :param text:
        :param validation_type:
        :param trigger_type:
        :param widget_name:
        :return:
        """
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def generate_button_threader(self):
        """
        Runs the sentence completion function in a thread.
        :return:
        """
        threading.Thread(target=self.generate_text, daemon=True).start()

    def download_button_threader(self):
        """
        Runs the download model function in a thread.
        :return:
        """
        threading.Thread(target=self.download_model, daemon=True).start()

    def download_model(self):
        """
        Downloads the GPT-2 model.
        :return:
        """
        self.lock_interface()
        self.main_frame.config(text="Downloading...")
        self.progress_bar.start()
        get_and_save_models()
        self.progress_bar.stop()
        self.main_frame.config(text="Enter Text to Complete")
        self.unlock_interface()

    def change_model(self, event):
        """
        Changes the model size.
        :param event:
        :return:
        """
        gpt2_size.x = self.model_option.get()

    def lock_interface(self):
        """
        Locks all parts of the interface to prevent the user clicking and typing while it is working.
        :return:
        """
        self.generate_button.configure(state=DISABLED)
        self.download_button.configure(state=DISABLED)
        self.text_entry.configure(state=DISABLED)
        self.length_entry.configure(state=DISABLED)
        self.model_option_drop.configure(state=DISABLED)

    def unlock_interface(self):
        """
        Unlocks all parts of the interface to allow the user to click and type again.
        :return:
        """
        self.generate_button.configure(state=NORMAL)
        self.download_button.configure(state=NORMAL)
        self.text_entry.configure(state=NORMAL)
        self.length_entry.configure(state=NORMAL)
        self.model_option_drop.configure(state=NORMAL)

    def generate_text(self):
        """
        Generates the text and outputs it to the GUI.
        :return:
        """
        self.lock_interface()
        output_length.x = self.ui_output_length.get()
        self.main_frame.config(text="Generating...")
        self.text_output.delete('1.0', END)
        self.progress_bar.start()

        try:
            generated_output = run_sentence_completion(self.person_reply.get())
        except OSError:
            get_and_save_models()
            try:
                generated_output = run_sentence_completion(self.person_reply.get())
            except OSError:
                raise Exception(f"Model {gpt2_size.x} not available, please check internet connection.")

        self.progress_bar.stop()
        self.text_output.insert(tk.END, f"{generated_output[1]}")
        self.main_frame.config(text="Enter Text to Complete")
        self.unlock_interface()
        self.text_entry.delete(0, END)

    def begin(self):
        """
        Starts the GUI.
        :return:
        """
        self.label.pack()

        self.root.mainloop()


if __name__ == "__main__":
    gui_control = GUIController()
    gui_control.begin()
