def sentence(word , part_of_sentence):
    if part_of_sentence == 0:
        print(f'im excited to add this {word} to the sentence')
    elif part_of_sentence == 1:
        print(f'added this {word} to the sentence')
    elif part_of_sentence == 2:
        print(f'now the sentence is: {word}')
    else:
        print('invalid input')

def main():
    word = input("Enter a word: ")
    part_of_sentence = int(input("Enter the part of the sentence (0-2): "))
    sentence(word, part_of_sentence)
    return

if __name__ == "__main__":
    main()
