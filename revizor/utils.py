from functools import partial
from typing import List, Optional

from flair.data import Span


def _get_text_from_spans(text: str, spans: List[Span], tag: str) -> Optional[str]:
    for span in spans:
        if span.tag == tag:
            return text[span.start_pos : span.end_pos]
    return None


_get_type_from_spans = partial(_get_text_from_spans, tag="TYPE")
_get_brand_from_spans = partial(_get_text_from_spans, tag="BRAND")
_get_model_from_spans = partial(_get_text_from_spans, tag="MODEL")
_get_vendor_code_from_spans = partial(_get_text_from_spans, tag="ARTICLE")
