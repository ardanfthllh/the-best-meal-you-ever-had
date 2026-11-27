"""The Best Meal You Ever Had — make.fun Mini ($2).
Entry for @ardanfthllh. Run: python3 main.py
"""
import os

ENTRY = 'The best meal I ever had was nasi goreng from a street cart at 2 a.m., eaten on a plastic stool in the rain while the cook laughed and added an extra egg.'

def generate_entry() -> str:
    return ENTRY

if __name__ == "__main__":
    text = generate_entry()
    print(text)
    if os.path.isdir("/output"):
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
