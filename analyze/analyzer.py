import MeCab


def morph(name, job, text):
    pass


def morph_analyze(text):

    tagger = MeCab.Tagger(
        '-Ochasen -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
    tagger.parse("")
    node = tagger.parseToNode(text)

    while node:
        hinshi = node.feature.split(",")[0]
        output = node.surface
        if hinshi == "名詞":
            pass
        elif hinshi == "動詞":
            output = node.feature.split(",")[6]
        elif hinshi == "助動詞":
            output = node.feature.split(",")[6]
        else:
            output = None
        if output != None:
            print(hinshi + ": " + output)

        node = node.next
