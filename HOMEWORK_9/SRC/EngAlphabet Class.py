class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print("Alphabet Letters:", ''.join(self.letters))

    def letters_num(self):
        return len(self.letters)



if __name__ == "__main__":
    english_alphabet = Alphabet("English", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    english_alphabet.print()
    print("Number of letters:", english_alphabet.letters_num())


class EngAlphabet(Alphabet):
    _letters_num = 26

    def __init__(self):
        super().__init__("En", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return EngAlphabet._letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."

if __name__ == "__main__":
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print("Number of letters:", eng_alphabet.letters_num())

    letter = 'A'
    print(f"Is '{letter}' an English letter? {eng_alphabet.is_en_letter(letter)}")

    print("Example text:", EngAlphabet.example())

eng_alphabet = EngAlphabet()

eng_alphabet.print()
print("Number of letters:", eng_alphabet.letters_num())


letter_f_belongs = eng_alphabet.is_en_letter('F')
print(f"Does 'F' belong to the English alphabet? {letter_f_belongs}")

letter_shch_belongs = eng_alphabet.is_en_letter('Щ')
print(f"Does 'Щ' belong to the English alphabet? {letter_shch_belongs}")


example_text = EngAlphabet.example()
print("Example text in English:", example_text)