# spacyspellcheck

Spell check using spacy vocab and in-built Levenshtein distance.

```bash
pip install -U spacyspellcheck
```

## Implementation

```python
spacyspell = SpellCorrector('word')
spacyspell.get_candidates(3) # get top three candidates
spacyspell.get_best() # gets the top corrected word
```
