Sentence_start = '''
Panaversity is the fun knowledgeable platform to keep our programming skills to next level
'''

def main():
    '''
    promts the user for an adjective ,noun and verb and returns a sentence
    '''
    adj = input("Enter an Adjective: ")
    noun = input("Enter a Noun: ")
    verb = input("Enter a Verb: ")
    return f"Panaversity is the {adj} {noun} platform to {verb} our programming skills to next level"


if __name__ == "__main__":
    print(main())