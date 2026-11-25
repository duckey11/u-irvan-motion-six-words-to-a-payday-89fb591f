import os

TEXT = "First payday came. I bought silence."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

if __name__ == "__main__":
    main()
