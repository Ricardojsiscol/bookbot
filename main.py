def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        character_tracker = count_characters(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(character_tracker)} words found in the document")
        for c in character_tracker:
            print(f"The '{c}' character was found {character_tracker[c]} times")
        print("--- End report ---")


def count_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    character_tracker = {}
    for c in file_contents.lower():
        ascii_value = ord(c)
        if (64 < ascii_value < 90) or (96 < ascii_value < 123):
            character_tracker[c] = character_tracker.get(c, 0) + 1
    return character_tracker



main()
