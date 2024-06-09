""" from https://github.com/keithito/tacotron """

"""
The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
"""

from text import cmudict, pinyin

_pad = "_"
_punctuation = "!'(),.:;? "
_special = "-"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Prepend "@" to additional phonemes to ensure uniqueness
_additional_phonemes = [
'@*ð', '@*n', '@*l', '@*ç', '@*u', '@*b', '@*d̪', '@*ʝ', '@*β', '@*i', '@*s', '@*ɾ', '@*w', '@*m', '@*a', '@*c', '@*k', '@*o', '@*ɣ', '@*f', '@*t̪', '@sil', '@*j', '@*p', '@*θ', '@*e', '@ð', '@ɟʝ', '@w', '@j', '@p', '@k', '@s', '@i', '@d̪', '@e', '@o', '@m', '@u', '@ɾ', '@a', '@n', '@l', '@x', '@θ', '@β', '@ʝ', '@spn', '@t̪', '@*r', '@*x', '@*ɟʝ', '@%d̪', '@%ɣ', '@%t̪', '@%l', '@%ç', '@%ɾ', '@%c', '@%ɲ', '@%r', '@%a', '@%β', '@%u', '@%i', '@%j', '@%b', '@%f', '@%w', '@%ð', '@%n', '@%e', '@%s', '@%ʎ', '@%m', '@%p', '@%θ', '@%o', '@ɣ', '@b', '@ʎ', '@c', '@r', '@%k', '@%tʃ', '@%ʃ', '@%x', '@%ʝ', '@*ʎ', '@f', '@%ŋ', '@*tʃ', '@*ɡ', '@*ɲ', '@ɡ', '@ɲ', '@*ŋ', '@ç', '@tʃ', '@%ɡ', '@%ɟ', '@%ɟʝ', '@ŋ', '@*ʃ', '@ɟ', '@ʃ', '@*ɟ']

_silences = ["@sp", "@spn", "@sil"]

# Prepend "@" to ARPAbet symbols to ensure uniqueness
_arpabet = ["@" + s for s in cmudict.valid_symbols]
_pinyin = ["@" + s for s in pinyin.valid_symbols]

# Export all symbols:
symbols = (
    [_pad]
    + list(_special)
    + list(_punctuation)
    + list(_letters)
    + _arpabet
    + _pinyin
    + _silences
    + _additional_phonemes
)
