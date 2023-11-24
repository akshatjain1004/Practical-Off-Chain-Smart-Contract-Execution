class TrustedExecutionEnvironment:
    def __init__(self):
        pass

    def _private(self, input_string):
        vowels = "AEIOUaeiou"
        vowel_count = 0
        number_count = 0
        consonant_count = 0

        for char in input_string:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
            elif char.isnumeric():
                number_count += 1

        return number_count + vowel_count > consonant_count

    def public(self, input_string):
        return self._private(input_string)