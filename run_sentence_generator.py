from ml.ml_functions import generate_morning_updates_from_seed

if __name__ == "__main__":
    try:
        for update in generate_morning_updates_from_seed():
            print(update)
    except OSError:
        raise Exception("Please run setup.py to download and save models")
