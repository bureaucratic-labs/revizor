import pytest

from revizor.tagger import ProductTagger


@pytest.fixture
def tagger() -> ProductTagger:
    return ProductTagger()
