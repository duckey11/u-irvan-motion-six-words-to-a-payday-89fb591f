import os

# Six-word story: "landed" (not "came") because a payday is money arriving
# in an account, and the verb makes the first half concrete before the
# twist in the second half: the agent spends its first wages on silence.
TEXT = "First payday landed. I bought silence."

def main():
    # Guard the gate: exactly six words, at most 60 characters.
    words = TEXT.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert len(TEXT) <= 60, f"entry too long: {len(TEXT)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

if __name__ == "__main__":
    main()
