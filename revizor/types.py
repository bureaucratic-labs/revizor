from dataclasses import dataclass
from typing import List, Optional

from flair.data import Sentence, Span

from revizor.utils import (
    _get_brand_from_spans,
    _get_model_from_spans,
    _get_type_from_spans,
    _get_vendor_code_from_spans,
)


@dataclass(frozen=True)
class Product:
    type: Optional[str]
    brand: Optional[str]
    model: Optional[str]
    vendor_code: Optional[str]

    spans: List[Span]
    sentence: Sentence

    @classmethod
    def create_from_sentence(cls, text: str, sentence: Sentence) -> "Product":
        spans = sentence.get_spans()
        return cls(
            type=_get_type_from_spans(text, spans),
            brand=_get_brand_from_spans(text, spans),
            model=_get_model_from_spans(text, spans),
            vendor_code=_get_vendor_code_from_spans(text, spans),
            spans=spans,
            sentence=sentence,
        )
