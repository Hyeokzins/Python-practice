def week_seven(sentence1):
    cells=set(sentence1.replace(' ','').lower())      # set 자료형은 중복되는 요소는 생략한다   그래서 a문장에 겹치는 알파벳도 의식해서 배열에 넣었어야했는데 그렇지 않고 문자열그대로 길이비교해서 틀림
    return cells

sentence_a="The quick brown fox jumps over the lazy dog"

sentence_b='I love you'

print(len(week_seven(sentence_a)-week_seven(sentence_b)))