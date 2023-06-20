# spacyspellcheck

Spell check using spacy vocab and in-built Levenshtein distance.

```bash
pip install -U spacyspellcheck
```

## Implementation

```python
from spacyspellcheck import spellcheck

spacyspell = spellcheck.SpellCorrector("Gret work taks more time")
spacyspell.get_possible_misspelt()
```
