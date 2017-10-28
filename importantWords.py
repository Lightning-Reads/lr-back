import wordcloud

def getWordCloud(text):
    wordc = wordcloud.WordCloud().generate(text)
    return wordc.words_

if __name__ == '__main__':
    print(getWordCloud("When make processes an include directive, it suspends reading of the containing makefile and reads from each listed file in turn. When that is finished, make resumes reading the makefile in which the directive appears."))