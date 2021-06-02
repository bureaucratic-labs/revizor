from typing import List

import razdel
from flair.tokenization import Token, Tokenizer


class RazdelTokenizer(Tokenizer):
    """
    Special tokenizer for flair, that uses razdel package.
    """

    def tokenize(self, text: str) -> List[Token]:
        spans = razdel.tokenize(text)
        return [Token(text=span.text, start_position=span.start) for span in spans]
