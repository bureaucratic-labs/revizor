# revizor [![Test & Lint](https://github.com/bureaucratic-labs/revizor/actions/workflows/test-and-lint.yml/badge.svg)](https://github.com/bureaucratic-labs/revizor) [![codecov](https://codecov.io/gh/bureaucratic-labs/revizor/branch/main/graph/badge.svg?token=YHND3N25LI)](https://codecov.io/gh/bureaucratic-labs/revizor)

This package solves task of splitting product title string into components, like `type`, `brand`, `model` and `vendor_code`.  
Imagine classic named entity recognition, but recognition done on product titles.

## Install

`revizor` requires python **3.8+** version **on Linux or macOS**, Windows **isn't supported** now, but contributions are welcome.

```bash
$ pip install revizor
```

## Usage

```python
from revizor.tagger import ProductTagger

tagger = ProductTagger()
product = tagger.predict("Смартфон Apple iPhone 12 Pro 128 gb Gold (CY.563781.P273)")

assert product.type == "Смартфон"
assert product.brand == "Apple"
assert product.model == "iPhone 12 Pro"
assert product.vendor_code == "CY.563781.P273"
```

## Boring numbers

Actually, just output from flair training log:
```
Corpus: "Corpus: 138959 train + 15440 dev + 51467 test sentences"
Results:
- F1-score (micro) 0.8843
- F1-score (macro) 0.8766

By class:
VENDOR_CODE    tp: 9893 - fp: 1899 - fn: 3268 - precision: 0.8390 - recall: 0.7517 - f1-score: 0.7929
BRAND          tp: 47977 - fp: 2335 - fn: 514 - precision: 0.9536 - recall: 0.9894 - f1-score: 0.9712
MODEL          tp: 35187 - fp: 11824 - fn: 9995 - precision: 0.7485 - recall: 0.7788 - f1-score: 0.7633
TYPE           tp: 25044 - fp: 637 - fn: 443 - precision: 0.9752 - recall: 0.9826 - f1-score: 0.9789
```

## Dataset

Model was trained on automatically annotated corpus. Since it may be affected by DMCA, we'll not publish it.  
But we can give hint on how to obtain it, don't we?  
Dataset can be created by scrapping any large marketplace, like goods, yandex.market or ozon.  
We extract product title and table with product info, then we parse brand and model strings from product info table.  
Now we have product title, brand and model. Then we can split product title by brand string, e.g.:

```python
product_title = "Смартфон Apple iPhone 12 Pro 128 Gb Space Gray"
brand = "Apple"
model = "iPhone 12 Pro"

product_type, product_model_plus_some_random_info = product_title.split(brand)

product_type # => 'Смартфон'
product_model_plus_some_random_info # => 'iPhone 12 Pro 128 Gb Space Gray'
```

## License

This package is licensed under MIT license.
