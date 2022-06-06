#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)

    if (len_sentence == 0):
        tuple = (len_sentence, None)
    else:
        tuple = (len_sentence, sentence[0])

    return (tuple)
