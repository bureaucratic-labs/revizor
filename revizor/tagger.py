import os
from pathlib import Path
from typing import Optional, Union

from flair.data import Sentence
from flair.models import SequenceTagger

from revizor.tokenizer import RazdelTokenizer
from revizor.types import Product


class ProductTagger:
    """
    Product title tagger.
    """

    def __init__(self, path: Optional[Union[str, Path]] = None) -> None:
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.tokenizer = RazdelTokenizer()
        self.model = SequenceTagger.load(
            path or os.path.join(self.base_path, "model/char-bpe-model.pt")
        )

    def predict(self, text: str) -> Product:
        sentence = Sentence(text, use_tokenizer=self.tokenizer)
        self.model.predict(sentence)
        return Product.create_from_sentence(text, sentence)
