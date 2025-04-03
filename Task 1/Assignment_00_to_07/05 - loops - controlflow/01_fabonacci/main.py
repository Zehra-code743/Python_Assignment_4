Max_term = 10000

def fabionci_sequence_():
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] < Max_term:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    sequence = fabionci_sequence_()
    print(sequence)
    return sequence

if __name__ == "__main__":
    main()