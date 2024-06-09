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
'@%d', '@%b', '@%t', '@spn', '@%z', '@%n', '@%aj', '@%h', '@%ŋ', '@%ɹ', '@%ej', '@%iː', '@%v', '@%ow', '@%ɐ', '@%s', '@%ɲ', '@%ɚ', '@%f', '@%ɟ', '@%ɫ', '@%ɛ', '@sil', '@%ʃ', '@%p', '@%bʲ', '@%æ', '@%tʃ', '@%fʲ', '@%ɒ', '@%d̪', '@%i', '@%l', '@%ɪ', '@%w', '@%ə', '@%c', '@%θ', '@%tʲ', '@%kʰ', '@%ɑ', '@%ʎ', '@%m', '@f', '@v', '@j', '@d̪', '@ɚ', '@tʃ', '@z', '@æ', '@ʉ', '@ʉː', '@dʒ', '@tʲ', '@iː', '@b', '@ɪ', '@m', '@l', '@θ', '@aw', '@tʰ', '@i', '@ɝ', '@ə', '@d', '@ɒ', '@ɐ', '@ɛ', '@s', '@n', '@aj', '@w', '@p', '@t', '@ɹ', '@ɲ', '@ow', '@ç', '@ɫ', '@mʲ', '@bʲ', '@kʰ', '@ɑ', '@h', '@ŋ', '@ʎ', '@ʃ', '@pʰ', '@ej', '@fʲ', '@m̩', '@*p', '@*ɫ', '@*ɪ', '@*ej', '@*ɛ', '@*n', '@*vʲ', '@*w', '@*dʲ', '@*ow', '@*s', '@*ɝ', '@*h', '@*v', '@*dʒ', '@*t', '@*ɲ', '@*d', '@*d̪', '@*ŋ', '@*aj', '@*ə', '@*ɚ', '@*ɡ', '@*tʃ', '@*ɒ', '@*ɹ', '@*z', '@*ɑ', '@*tʲ', '@*iː', '@*ç', '@*k', '@*æ', '@*m', '@*tʰ', '@*i', '@*bʲ', '@*ʃ', '@*m̩', '@*f', '@*pʰ', '@*ɒː', '@*ʊ', '@*ɔj', '@*ʉː', '@%dʲ', '@%k', '@%ɝ', '@%tʰ', '@%ʉː', '@%dʒ', '@%pʰ', '@%t̪', '@*b', '@*l', '@*ɟ', '@*ɐ', '@*j', '@*aw', '@*ʎ', '@*mʲ', '@*ɾ', '@*ɫ̩', '@*ɑː', '@%ʉ', '@%ç', '@%ɔj', '@%ʊ', '@%ɾ', '@%ɫ̩', '@%ɡ', '@%mʲ', '@ɟ', '@t̪', '@k', '@vʲ', '@*cʰ', '@*pʲ', '@*c', '@*kʰ', '@%ɒː', '@cʰ', '@c', '@ʊ', '@tʷ', '@ɒː', '@*t̪', '@*ɾʲ', '@*ð', '@%ʒ', '@%vʲ', '@%pʲ', '@ɑː', '@ɫ̩', '@kʷ', '@ɡ', '@ɾ', '@%j', '@%cʰ', '@%ð', '@*fʲ', '@pʲ', '@%kʷ', '@*ʉ', '@dʲ', '@*n̩', '@cʷ', '@ð', '@%ɑː', '@%aw', '@%ɟʷ', '@*tʷ', '@*ʒ', '@ʒ', '@%cʷ', '@%n̩', '@%tʷ', '@*θ', '@ɾʲ', '@n̩', '@*kʷ', '@*ɟʷ', '@%ɾʲ', '@%ɾ̃', '@*cʷ', '@ɔj', '@ɟʷ', '@%m̩', '@ɾ̃', '@*ɾ̃', '@*aː', '@%ʔ', '@ʔ', '@%aː']


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
