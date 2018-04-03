#!/usr/bin/env python3

"""
Find the frequency of any given word in a book, repeatedly.

Completion time: 15 minutes.

Examples: "this this is some text."

Notes
- Knew tokenization was main problem.
"""
import re


def word_freq_dict(text):
    results = dict()
    for word in re.findall(r'\w+', text):
        word = word.lower()
        results[word] = results.get(word, 0) + 1
    return results


def get_freq(text_dict, word):
    total = sum(text_dict.values())
    return (1.0 * text_dict.get(word, 0)) / total


if __name__ == '__main__':
    text_dict = word_freq_dict('this this is some text.')
    assert text_dict == {'this': 2, 'is': 1, 'some': 1, 'text': 1}, text_dict
    assert get_freq(text_dict, 'this') == 0.4
    assert get_freq(text_dict, 'text') == 0.2
    assert get_freq(text_dict, 'foobar') == 0
    assert get_freq(text_dict, '') == 0
    assert get_freq(text_dict, None) == 0
