from revizor.tagger import ProductTagger


def test_predict(tagger: ProductTagger) -> None:
    product = tagger.predict(
        "Смартфон Apple iPhone 12 Pro 128 gb Gold (CY.563781.P273)"
    )

    assert product.type == "Смартфон"
    assert product.brand == "Apple"
    assert product.model == "iPhone 12 Pro"
    assert product.article == "CY.563781.P273"


def test_predict_optional_field(tagger: ProductTagger) -> None:
    product = tagger.predict("Смартфон Apple iPhone 12 Pro 128 gb Gold")

    assert product.type == "Смартфон"
    assert product.brand == "Apple"
    assert product.model == "iPhone 12 Pro"
    assert product.article is None
