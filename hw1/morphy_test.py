import pymorphy2
morph = pymorphy2.MorphAnalyzer()
first = morph.parse('эту')[0]
print(first.tag.case)
second = morph.parse('минута')[0]
if first.tag.case != None:
    print(second.inflect({first.tag.case})[0])
else:
    print(second.inflect({'gent'})[0])

