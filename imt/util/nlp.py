import en_core_web_md
import wmd

_spacy_cache = None
_spacy_wmd_cache = None


def get_spacy_model():
    global _spacy_cache
    if _spacy_cache is None:
        _spacy_cache = en_core_web_md.load()

    return _spacy_cache


def _get_spacy_wmd_model():
    global _spacy_wmd_cache
    if _spacy_wmd_cache is None:
        _spacy_wmd_cache = en_core_web_md.load()
        _spacy_wmd_cache.add_pipe(wmd.WMD.SpacySimilarityHook(_spacy_wmd_cache), last=True)

    return _spacy_wmd_cache


def get_word_mover_dist(sentence1, sentence2):
    nlp = _get_spacy_wmd_model()

    try:
        docs = list(nlp.pipe([sentence1, sentence2]))
        return docs[0].similarity(docs[1])
    except RuntimeError:
        return float('inf')
