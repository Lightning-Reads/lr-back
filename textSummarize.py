from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def summarize(text, SENTENCES_COUNT = 3,LANGUAGE = "english"):
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = LexRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    output = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        output.append(sentence._text+' ')
    return ''.join(output)

if __name__ == '__main__':
    print(summarize("Frankfurt, a central German city on the river Main, is a major financial hub that's home to the European Central Bank. It's the birthplace of famed writer Johann Wolfgang von Goethe, whose former home is now the Goethe House Museum. Like much of the city, it was damaged during World War II and later rebuilt. The reconstructed Altstadt (Old Town) is the site of Roemerberg, a square that hosts an annual Christmas market."))