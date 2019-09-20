
import argparse
import io



#split line by line...but before using ..check its suitability to ur file
def read_biased_words(file, biased_file):
    file_to_write = open(biased_file, 'w', encoding='utf8')
    with open(file) as f:
        for line in f:
            print(line)
            word=line.replace(',', '\n')
            word=word.replace('[\'','')
            word=word.replace('\']', '')
            word = word.replace(' ', '')
            word = word.replace('[', '')
            word = word.replace(']', '')
            word=word.lower()
            file_to_write.write(word)
            print (word)


read_biased_words('/home/christine/Phd/Cristina_cooperation/ContextEmbeddingsEvaluations/latest_experiments/biased.txt','/home/christine/Phd/Cristina_cooperation/ContextEmbeddingsEvaluations/latest_experiments/biased_5000_grammar_female.txt')
