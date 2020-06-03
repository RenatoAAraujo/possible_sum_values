from datetime import datetime
import pickle


def save_file(ls: list, name: str):
    print(f"[{datetime.now()}] Saving {name} pickle file")
    with open(f"temp/{name}.pkl", "wb") as f:
        pickle.dump(ls, f, pickle.HIGHEST_PROTOCOL)


def load_file(name: str):
    print(f"[{datetime.now()}] Loading {name} pickle file")
    with open(f"temp/{name}.pkl", "rb") as f:
        return pickle.load(f)
