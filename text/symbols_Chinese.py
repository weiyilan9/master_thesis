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
'@%k', '@%t', '@%i3', '@%ang2', '@%r', '@%ie4', '@%uai4', '@%an4', '@sp', '@%x', '@%j', '@%iao1', '@%u4', '@%e2', '@%zh', '@%uan2', '@%l', '@%ia1', '@%uen3', '@%b', '@%sh', '@%i4', '@%h', '@%g', '@%uen2',
'@%ch', '@%d', '@%ai4', '@%iang4', '@%f', '@%u1', '@%i2', '@%z', '@%u3', '@%uan3', '@%an3', '@%ing5', '@%en4', '@%ing1', '@%a4', '@%in4', '@%iii4', '@%e5', '@*p', '@*ve4', '@*en1', '@*uo4', '@*i2',
'@*z', '@*ch', '@*iang2', '@*g', '@*c', '@*d', '@*in3', '@*uang1', '@*ing3', '@*l', '@*u1', '@*h', '@*ian4', '@*eng2', '@*zh', '@*iou4', '@*ian3', '@*ao3', '@*e2', '@uo3', '@a5', '@ang3', '@d', '@uei4',
'@l', '@ang4', '@ou4', '@ou5', '@m', '@sh', '@ian3', '@ao2', '@en2', '@zh', '@e5', '@%eng1', '@%n', '@%ao1', '@%van4', '@%ei2', '@%ai2', '@%c', '@%uo1', '@%v4', '@%m', '@%ao4', '@%eng2', '@%ing4', '@%iou3', 
'@%an2', '@%i1', '@%uo2', '@%ian3', '@%ou1', '@*a4', '@*m', '@*t', '@*u3', '@*uan1', '@*ao1', '@*j', '@*uo3', '@*q', '@*in1', '@*iao2', '@*ian1', '@*i3', '@*iou2', '@*eng1', '@*f', '@*ua1', '@*vn2', '@*x',
'@*k', '@*ai2', '@*er4', '@*sh', '@*ong1', '@*u4', '@*iii4', '@*van2', '@*ii4', '@*ai1', '@*s', '@*e4', '@*uan3', '@*u2', '@ian4', '@h', '@uai3', '@z', '@ai4', '@ei4', '@j', '@an1', '@iou3', '@in4', '@uen3', 
'@e2', '@ii4', '@ch', '@i1', '@b', '@uo4', '@i2', '@q', '@ei2', '@s', '@i4', '@e4', '@iii4', '@c', '@uai4', '@iao1', '@a4', '@ao3', '@x', '@ing2', '@ii1', '@n', '@iao4', '@en4', '@k', '@uan3', '@iii2', '@u5',
'@eng4', '@in1', '@ai1', '@g', '@ia1', '@%ang4', '@%an1', '@%s', '@%q', '@%van3', '@%iou2', '@%ong1', '@%ong4', '@%v2', '@%a2', '@*n', '@*ai4', '@*uang2', '@*uo1', '@*ing4', '@*iong4', '@*uang3', '@*v3', '@*a3',
'@*uai4', '@*ia4', '@*ang4', '@uo1', '@er2', '@ing4', '@uang2', '@t', '@f', '@ong1', '@ie3', '@u3', '@an3', '@e1', '@uei2', '@eng1', '@ou1', '@a1', '@u4', '@an5', '@u2', '@ie1', '@an4', '@an2', '@p', '@en3', 
'@o5', '@u1', '@v4', '@i3', '@%in2', '@%ian2', '@e3', '@ing1', '@ia2', '@iou2', '@eng2', '@ong3', '@a2', '@%ii5', '@%iii2', '@%ei4', '@%uo3', '@%a5', '@%ao3', '@%p', '@ian1', '@ian2', '@a3', '@uang1', '@ve4',
'@ing3', '@%e4', '@%a3', '@%ong2', '@%ong3', '@%uo4', '@%ing2', '@%v1', '@%uei2', '@%ian4', '@%ia4', '@%a1', '@%in1', '@%ie3', '@%iao4', '@%iao2', '@%iou4', '@%v3', '@%uai1', '@%ai3', '@%ii3', '@%uang4', '@v1', 
'@uen4', '@r', '@iang1', '@ua2', '@van2', '@van1', '@en1', '@uei1', '@uan1', '@ao4', '@*ei1', '@*ang1', '@*i4', '@*ii1', '@*en2', '@*v2', '@*ai3', '@*r', '@*uo2', '@*e1', '@*iao1', '@ang2', '@v3', '@uei3', '@ou2',
'@ong2', '@*an4', '@*uan2', '@*ou2', '@*e3', '@*van1', '@*b', '@uan2', '@iou4', '@ou3', '@ai2', '@ang1', '@iao2', '@ua4', '@*er2', '@*uei4', '@*ian2', '@*en5', '@*a1', '@iou1', '@ia4', '@uan4', '@iao3', '@in3', 
'@uang4', '@%ei3', '@ie2', '@iong4', '@uen1', '@*iii1', '@*iii2', '@*i1', '@*ing1', '@*uen3', '@*uen4', '@*e5', '@*ao4', '@*uei1', '@*an3', '@*ong4', '@*ang2', '@*ve2', '@*iou5', '@*ao2', '@*iou1', '@*uei3', 
'@*iang3', '@*ou3', '@*an1', '@ing5', '@ua1', '@iii3', '@in2', '@ei3', '@%ang3', '@%ve4', '@%ii4', '@%uei3', '@en5', '@van3', '@iii1', '@%ai1', '@%er4', '@%ian1', '@*ei2', '@*uang4', '@ong4', '@%uan4', '@%ao2', 
'@%en1', '@vn4', '@ii3', '@ve3', '@ie5', '@%eng4', '@*ia1', '@*in2', '@*ie4', '@%en2', '@%uen4', '@%van2', '@%uei4', '@%ang1', '@%ou2', '@%iang3', '@%u2', '@%ie2', '@*ie3', '@*ong2', '@*iang4', '@*v1', '@*iao4',
'@*ei4', '@*ou4', '@*uan4', '@*o4', '@*eng4', '@*uei2', '@%uang3', '@%ii2', '@%ou4', '@ai3', '@er4', '@iang4', '@ve1', '@o1', '@*ing2', '@*en3', '@ie4', '@iang3', '@%iao3', '@%iii1', '@vn2', '@%iong1', '@%o5', 
'@%iong4', '@%in3', '@uen2', '@uo2', '@uanr2', '@%ua1', '@%iii3', '@v2', '@*u5', '@ua3', '@o2', '@%iang2', '@%ou5', '@%ua4', '@%ie1', '@%iou1', '@%ong5', '@%e1', '@%uei1', '@ei1', '@ia5', '@ao1', '@*iao3', '@*an5', 
'@*ii5', '@*ie2', '@*ai5', '@iang2', '@*iii5', '@*iong3', '@*iang1', '@*in4', '@*ia3', '@*ua4', '@%en3', '@*a2', '@*uen1', '@*ang3', '@*iou3', '@%ueir4', '@%ou3', '@ve2', '@ao5', '@iii5', '@*v4', '@*ve1', '@*o5',
'@*ii3', '@*en4', '@%er2', '@%vn1', '@%eng3', '@ii2', '@iong3', '@%er5', '@o3', '@iir2', '@inr4', '@*eng5', '@vn1', '@%uang2', '@%uen1', '@uang3', '@%in5', '@%vn4', '@*uai1', '@*ou1', '@*ing5', '@*eng3', '@%uan1', 
'@%ii1', '@*enr4', '@iang5', '@van4', '@i5', '@ai5', '@*vn1', '@*a5', '@*ii2', '@%er3', '@%u5', '@%uo5', '@uo5', '@%ua3', '@%iong2', '@iong1', '@%i5', '@*ei3', '@o4', '@%vn2', '@%uang1', '@%o2', '@*iii3', '@*an2', 
'@ang5', '@*iong1', '@ii5', '@%eng5', '@*van4', '@eng3', '@*er5', '@*ao5', '@*ie5', '@*uen2', '@%iang1', '@iou5', '@*iang5', '@%en5', '@*o2', '@*er3', '@*ong3', '@%ve2', '@*o1', '@%e3', '@*uen5', '@ia3', '@*uai2', 
'@*enr5', '@%o1', '@*ia5', '@%ia5', '@%iii5', '@*ua2', '@*ie1', '@%anr1', '@*iong5', '@*vn4', '@uan5', '@ar4', '@%ei1', '@%ve3', '@*ua3', '@ianr3', '@uen5', '@*uan5', '@*uai3', '@*iiir4', '@%ing3', '@%iiir4', 
'@uai1', '@*ueir4', '@*enr1', '@*ianr3', '@iong2', '@%ao5', '@%uai2', '@*uo5', '@*iong2', '@*van3', '@%van1', '@%an5', '@uor3', '@%io5', '@*ou5', '@%o4', '@io5', '@%ia3', '@%iang5', '@%ve1', '@ueng4', '@%o3', 
'@%ie5', '@%ua2', '@%ai5', '@*ar4', '@*ir2', '@in5', '@ur4', '@*uai5', '@*ong5', '@er3', '@ua5', '@*van5', '@v5', '@eng5', '@*ia2', '@ueir4', '@*uang5', '@uei5', '@van5', '@%ian5', '@*i5', '@iong5', '@ueng3', 
'@%ur3', '@uai2', '@%iong3', '@%ia2', '@%ueng4', '@*o3', '@*ve3', '@*ua5', '@*air2', '@*ar2', '@*anr4', '@%ang5', '@%uai3', '@*ir3', '@%van5', '@*in5', '@*ei5', '@*vn3', '@*uei5', '@%ir4', '@%iou5', '@ei5',
'@%uan5', '@uenr3', '@%iangr4', '@%ua5', '@*io5', '@%ar4', '@%iao5', '@ong5', '@%uanr2', '@%air2', '@iao5', '@*ur4', '@%ei5', '@%ianr2', '@spn', '@*v5', '@*ang5', '@*ian5', '@*ueng4', '@%uang5', '@uang5', '@*ueng1', 
'@*ingr2', '@%ingr3', '@er5', '@*vn5', '@*ianr2', '@%anr4', '@vn3', '@*aor3', '@ir3', '@*iir2', '@ueng2', '@*uenr3', '@ir4', '@%ianr3', '@anr4', '@ar3', '@%vn3', '@*iao5', '@%v5', '@ueng1', '@%uen5', '@%ingr2',
'@*uanr2', '@anr1', '@%ueng1', '@%uair4', '@uanr1', '@*uenr4', '@%iong5', '@%iar3', '@*ir4', '@*ingr3', '@ueir3', '@air2', '@*uanr1', '@ian5', '@*aor4', '@*inr4', '@enr2', '@ar2', '@ianr1', '@%vanr4', '@aor4', '@*io1', '@*ar3', '@ir5', '@*ir1', '@%ar2', 
'@%ar3', '@%iir2', '@%vn5', '@*ve5', '@%ongr4', '@*uor3', '@uair4', '@ianr2', '@*iar3', '@*uair4', '@%uor2', '@io1', '@%air4', '@%enr5', '@*enr2', '@iiir4', '@*anr3', '@*ueir1', '@*vanr4', '@*our2'
]

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
