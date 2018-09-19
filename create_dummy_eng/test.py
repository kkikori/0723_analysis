# coding: utf-8

"""
json- RPC で，文書を分割して返すサーバ

サーバ側の環境構築 (python 3.5):
pip install json-rpc
pip install werkzeug
"""

import re
import os
import nltk
import MeCab

# ポート番号
PORT = 4649

# RPC アプリ名
APP_NAME = 'splitter_application'

'''
-----------------------------------------------------------------------------------------------------
MeCab
-----------------------------------------------------------------------------------------------------
'''
# neologdの場所候補
PATH_TO_NEOLOGD_LIST = [
    '/usr/local/mecab/lib/mecab/dic/mecab-ipadic-neologd/',  # iMac環境1
    '/usr/local/lib/mecab/dic/mecab-ipadic-neologd/',  # iMac環境2
    '/usr/lib/mecab/dic/mecab-ipadic-neologd',  # Wasa
    os.environ['HOME'] + '/local/lib/mecab/dic/mecab-ipadic-neologd/',  # リモートのLinux環境
]
PATH_TO_NEOLOGD = None
for nlgd_path in PATH_TO_NEOLOGD_LIST:
    if os.path.isdir(nlgd_path):
        PATH_TO_NEOLOGD = nlgd_path
        print('Found dictionary at {}'.format(nlgd_path))
        break
# 辞書が見つからなかった
if PATH_TO_NEOLOGD is None:
    print('MeCab-Neologd is not available at the path. Check config.py.')

# 「」（ ）【】『』
PUNCTUATION = re.compile('[。．\.？！\?!]')
OPEN_BRACKET = ('「', '（', '【', '『')
CLOSE_BRACKET = ('」', '）', '】', '』')

NEWLINE = re.compile('[\r\n]+')


def to_sentences(text, pattern=PUNCTUATION, with_bracket=True):
    sentences = []
    begin = 0
    end = 0

    for ch in text:
        if re.search(pattern, ch):
            # PUNCTUATION が連続するときはスキップ
            if begin == end:
                begin = end + 1
                end += 1
                continue
            sentence = text[begin:end + 1]
            if with_bracket:
                if check_paired_brackets(sentence):
                    sentences.append(sentence)
                    begin = end + 1
            else:
                sentences.append(sentence)
                begin = end + 1
        end += 1

    if end > begin:
        sentence = text[begin:end + 1]
        sentences.append(sentence)

    return sentences


def check_punctuation(text):
    has_punctuation = True
    if re.search(PUNCTUATION, text) is None:
        has_punctuation = False
    return has_punctuation


def check_paired_brackets(text):
    brackets = []

    for ch in text:
        if ch in OPEN_BRACKET:
            brackets.append(ch)
        elif ch in CLOSE_BRACKET:
            if len(brackets) == 0:
                return False
            last_bracket = brackets.pop()
            if OPEN_BRACKET.index(last_bracket) != CLOSE_BRACKET.index(ch):
                return False

    return len(brackets) == 0


# PUNCTUATIONなどによる文分割
def split_text(text):
    has_punctuation = check_punctuation(text)
    has_paired_brackets = check_paired_brackets(text)

    if has_punctuation:
        if has_paired_brackets:
            sentences = to_sentences(text, PUNCTUATION, with_bracket=True)
        else:
            sentences = to_sentences(text, PUNCTUATION, with_bracket=False)
    else:
        if has_paired_brackets:
            sentences = to_sentences(text, NEWLINE, with_bracket=True)
        else:
            sentences = to_sentences(text, NEWLINE, with_bracket=False)

    return sentences


def clean_text(text):
    text = text.strip()
    text = re.sub(NEWLINE, '', text)
    return text


def extract_poses(sentence: str):
    text = nltk.word_tokenize(sentence)
    tagger = nltk.pos_tag(text)

    words = []
    poses = []
    for node in tagger:
        words.append(node[0])
        poses.append(node[1])

    return words, poses


NOUN_POS_TAGS = ["NN", "NNS", "NNP", "NNPS", "PRP", "PRP$", "WP", "WP$"]  # noun
VB_POS_TAGS = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]  # verb
JJ_POS_TAGS = ["JJ", "JJR", "JJS"]  # adjective


def setsu_(words):
    bunsetsu = ""
    for i, w in enumerate(words):
        bunsetsu += w
        if i==len(words)-1:
            break
        if re.match(r"[a-zA-Z]", words[i+1][0]):
            bunsetsu += " "
    return bunsetsu


def split_by_conj_particle(sentence: str):
    words, poses = extract_poses(sentence)

    result_sentences = []
    start_index = 0

    bun_checker = {"subject": 0, "verb": 0, "words": 0}
    for i, (w, pos) in enumerate(zip(words, poses)):
        if pos in NOUN_POS_TAGS or pos in JJ_POS_TAGS:
            bun_checker["subject"] += 1
        elif pos in VB_POS_TAGS:
            bun_checker["verb"] += 1
        bun_checker["words"] += 1

        if i == len(words) - 1:
            # result_sentences.append(' '.join(words[start_index:]))
            result_sentences.append(setsu_(words[start_index:]))
        elif \
                (
                                    bun_checker["subject"] > 1 and \
                                        bun_checker["verb"] > 1 and \
                                    w == ","
                ):
            end_index = i
            while True:
                if end_index + 1 > len(words) - 1:
                    break
                if not re.match(r"[A-Z]", poses[end_index + 1][0]):
                    end_index += 1
                else:
                    break
            #result_sentences.append(' '.join(words[start_index: end_index + 1]))
            result_sentences.append(setsu_(words[start_index: end_index + 1]))
            start_index = end_index + 1
            bun_checker = {"subject": 0, "verb": 0, "words": 0}
    return result_sentences


def engtest():
    sentence = "Such scale, I think it is better way to make decisions.In my opinion, democracy's defect is that participation of large number causes malfunction.If there is a breakthrough way to cover it's defect,referendum may be able to be merely a majority vote. "

    sentence = sentence.replace('\\n', '\n')
    sentences = split_text(sentence)
    sentences = [clean_text(s) for s in sentences]
    resulting_sentences = []
    for sente in sentences:
        print(sente)
        spl_sentences = split_by_conj_particle(sente)
        resulting_sentences += spl_sentences
    resulting_sentences = [s for s in resulting_sentences if s != '']
    return resulting_sentences

def main():
    sentences = engtest()
    for sent in sentences:
        print(sent)

    # sentence = "If there is a breakthrough way to cover it's defect,referendum may be able to be merely a majority vote. "
    #
    # rd_parser = nltk.RecursiveDescentParser(grammar1)
    # sent = sentence.split()
    # for tree in rd_parser.parse(sent):
    #     print(tree)


if __name__ == '__main__':
    main()
