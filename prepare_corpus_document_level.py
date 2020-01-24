import argparse
import io

from bs4 import BeautifulSoup
import random
def make_new_corpus_of_two_lines(file, file_path_to_write):


    file_read = open(file, 'r', encoding='utf8')
    file_to_write = open(file_path_to_write, 'w', encoding='utf8')
    keep_second_line = ''
    line1 = file_read.readline().strip().replace('\n','')
    line = file_read.readline().strip().replace('\n','')
    file_to_write.write(line1+' <sep> '+line+'\n')
    print(line1+' <sep> '+line)
    while True:
        keep_last_line= line

        line = file_read.readline().strip().replace('\n','')

        print(keep_last_line + ' <sep> '+ line)
        file_to_write.write(keep_last_line + ' <sep> '+ line+'\n')
        if not line: break  # EOF




#this method reads the corpus if it follows the format of wmt test
def make_new_corpus_of_two_lines_seg_file(file, file_path_to_write):


    file_read = open(file, 'r', encoding='utf8')
    file_to_write = open(file_path_to_write, 'w', encoding='utf8')
    keep_second_line = ''
    new_document = True
    while True:
        if (not new_document):
            keep_sentence=line1

        line_read = file_read.readline().strip().replace('\n', '')
        soup = BeautifulSoup(line_read,features="html5lib")
        for seg in soup.find_all('seg'):
            if seg.has_attr('id'):
                line1 = seg.string
                new_document=False

            if(keep_sentence):
                print(keep_sentence + ' <sep> ' + line1 + '\n')
                file_to_write.write(keep_sentence + ' <sep> ' + line1 + '\n')


        for seg in soup.find_all('doc'):
            if seg.has_attr('docid'):
                print ('new document')
                new_document=True
                keep_sentence = ''
        if not line_read: break  # EOF

# get number of random tokens
def get_test_valid_for_two_languages(file_src, file_trg, no_lines_to_include, no_random_sentences):
    random_list = random.sample(range(no_lines_to_include), no_random_sentences)
    get_test_valid_for_two_languages(file_src, random_list)
    get_test_valid_for_two_languages(file_trg, random_list)


# get number of random tokens
def get_test_valid_for_two_languages(file, random_list):

    read_file = open(file, 'r', encoding='utf8')
    file_to_write_testing = open('test-' + file, 'w', encoding='utf8')
    file_to_write_training= open('train-'+file,  'w', encoding='utf8')
    index = 0
    random_token_embeddings = []
    for line in read_file:
        if line and line.strip():
            if (index in random_list):
                file_to_write_testing.write(line)
            else:
                file_to_write_training.write(line)

        index += 1
    #split file in
    with open('test-' + file) as fp:
        data = fp.read()
    out1 = open('test_' + file, 'w')
    out2 = open('valid_' + file, 'w')
    halfway = len(data) / 2
    out1.write(data[0:halfway])
    out2.write(data[halfway + 1:])
    out1.close()
    out2.close()
    file_to_write_testing.close()
    file_to_write_training.close()
    read_file.close()

if __name__ == "__main__":
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--src_file", help="The file of the source language")
    parser.add_argument("--src_file_prepared", help="The file of the source language after preparation")
    parser.add_argument("--trg_file", help="The file of the target language")
    parser.add_argument("--trg_file_prepared", help="The file of the source language after preparation")


    args = parser.parse_args()

    src_file = args.src_file
    src_file_prepared = args.src_file_prepared
    trg_file = args.trg_file
    trg_file_prepared = args.trg_file_prepared

    make_new_corpus_of_two_lines(src_file, src_file_prepared)
    make_new_corpus_of_two_lines(trg_file, trg_file_prepared)
    '''

    make_new_corpus_of_two_lines_seg_file('/home/christine/Downloads/newstest2014-deen-ref.de.sgm','test_wmt14_ende.de')