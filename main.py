def main():
    path_to_file = "books/frankenstein.txt"
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
            # print(file_contents)

            # count the number of words
            word_count = count_words(file_contents)
            # print(f"\n{word_count} words found in the document.")

            # Count the nubmer of chars
            char_count = count_chars(file_contents)
            # print(f"\nCharacter counts in the document:\n {char_count}")

            # Print report
            print_report(path_to_file, word_count, char_count)

    except FileNotFoundError:
        print(f"Error: The file '{path_to_file}' does not exists.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts
        
def print_report(file_path, word_count, char_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        print(f"The '{char} character was found {count} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
    