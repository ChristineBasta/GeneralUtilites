import argparse
import re
import random
import os
import io
from bs4 import BeautifulSoup


# experiments for EuroParl...the training corpus is Europarl and the tesing is the GebioToolKit

def make_new_corpus_of_two_lines(file, file_path_to_write, id_list):
    file_read = open(file, 'r', encoding='utf8')
    file_to_write = open(file_path_to_write, 'w', encoding='utf8')
    id = id_list[0]
    index = 1
    new_document = True
    line1 = file_read.readline().strip().replace('\n', '')
    while True:
        line2 = file_read.readline().strip().replace('\n', '')
        if (index < len(id_list)):
            if id != id_list[index]:
                id = id_list[index]
                line1 = line2

            else:
                file_to_write.write(line1 + ' <sep> ' + line2 + '\n')
                line1 = line2

        index = index + 1
        if not line2: break  # EOF

#most probably this method does not handle the documents with one sentence
def make_extended_gendered(file, file_path_to_write, id_list, gender_list):
    file_read = open(file, 'r', encoding='utf8')
    file_to_write = open(file_path_to_write, 'w', encoding='utf8')
    id = id_list[0]
    index = 1
    new_document = True
    gender=gender_list[0]
    line1 = file_read.readline().strip().replace('\n', '')
    while True:
        line2 = file_read.readline().strip().replace('\n', '')
        if (index < len(id_list)):
            #new document
            if id != id_list[index]:
                id = id_list[index]
                line1 = line2
                gender=gender_list[index]

            #old document
            else:
                file_to_write.write(gender+' '+line1 + ' <sep> ' + line2 + '\n')
                line1 = line2

        index = index + 1
        if not line2: break  # EOF


def add_tag_to_file(file_to_read, file_to_write, gender_list):
    file_read = open(file_to_read, 'r', encoding='utf8')
    file_write = open(file_to_write, 'w', encoding='utf8')
    keep_second_line = ''
    index = 0
    while True:

        line = file_read.readline().strip().replace('\n', '')
        if (index < len(gender_list)):
            file_write.write(gender_list[index] + ' ' + line + '\n')

        index += 1
        if not line: break  # EOF

def sortFirst(val):
    return val[0]
def read_gender_indices(file):
    file_read = open(file, 'r', encoding='utf8')
    gender_list = []
    id_list = []
    while True:

        line_read = file_read.readline().strip().replace('\n', '')

        m = re.search(r"(?<=gender=).*?(?=\s)", line_read.lower())
        if (m is not None):
            # print(m[0])

            gender_list.append(m[0].replace("\"", "").upper())

        m = re.search(r"(?<=euroid=).*?(?=\s)", line_read.lower())

        if (m is not None):
            # print(m[0])

            id_list.append(m[0].replace("\"", "").upper())

        if not line_read:
            break

    print(len(gender_list))

    print(len(id_list))
    return gender_list, id_list


# get number of random tokens
def get_random_test_valid_src_trg(file_src, file_trg, no_lines_to_include, no_random_sentences, src, trg,
                                  train_file_name, test_file_name, ):
    random_list = random.sample(range(no_lines_to_include), no_random_sentences)
    get_test_valid(file_src, random_list, src, test_file_name, train_file_name)
    get_test_valid(file_trg, random_list, trg, test_file_name, train_file_name)


def get_test_valid(file, random_list, lg, test_file_name, train_file_name):
    print(random_list)
    path, file_name = os.path.split(file)
    read_file = open(file, 'r', encoding='utf8')
    file_to_write_testing = open(path + '/' + test_file_name + '.' + lg, 'w', encoding='utf8')
    file_to_write_training = open(path + '/' + train_file_name + '.' + lg, 'w', encoding='utf8')
    index = 0
    random_token_embeddings = []
    for line in read_file:
        if line and line.strip():
            if (index in random_list):
                file_to_write_testing.write(line)
            else:
                file_to_write_training.write(line)

        index += 1

    file_to_write_testing.close()
    file_to_write_training.close()
    read_file.close()


# reading the GEbio text file

# this method reads the corpus if it follows the format of wmt test
# mode_of_work=1 if gendered
# mode_of_work=2 if normal
# mode_of_work=3 if extended
# mode_of_work=4 if extended with gender

def make_new_corpus_of_two_lines_seg_file(file, mode_of_work=1, ln='en'):
    file_read = open(file, 'r', encoding='utf8')
    path, file_name = os.path.split(file)
    file_start=file_name[0: file_name.find('.')]
    write_gender = False
    normal = False

    if mode_of_work == 1:
        write_gender = True
        file_to_write = open(path +'/'+file_start+'_gebio_gendered.'+ln, 'w', encoding='utf8')

    if mode_of_work == 2:
        file_to_write = open(path +'/'+file_start+'_gebio_original.'+ln, 'w', encoding='utf8')
        normal = True

    if mode_of_work==3:

        file_to_write = open(path +'/'+file_start+'_gebio_extended.'+ln, 'w', encoding='utf8')

    if mode_of_work == 4:
        write_gender = True
        file_to_write = open(path +'/'+file_start+'_gebio_extended_gendered.'+ln, 'w', encoding='utf8')

    keep_second_line = ''
    new_document = True
    no_sentences_per_doc=0
    while True:
        if (not new_document):
            keep_sentence = line1

        line_read = file_read.readline().strip().replace('\n', '')
        soup = BeautifulSoup(line_read, features="html5lib")

        for seg in soup.find_all('seg'):
            no_sentences_per_doc+=1
            if seg.has_attr('id'):
                line1 = seg.string
                line1 = line1.replace('<\seg>', '')
                print(line1)
                new_document = False

            if mode_of_work == 4 or mode_of_work == 3:

                if (keep_sentence and write_gender):

                    print('<' + gender + '> ' + keep_sentence + ' <sep> ' + line1 + '\n')
                    file_to_write.write( gender + ' ' + keep_sentence + ' <sep> ' + line1 + '\n')
                elif (keep_sentence):
                    print(keep_sentence + ' <sep> ' + line1 + '\n')

                    file_to_write.write(keep_sentence + ' <sep> ' + line1 + '\n')
            else:
                if (write_gender):

                    print('<' + gender + '> ' + line1 + '\n')
                    file_to_write.write( gender + ' ' + line1 + '\n')

                if (normal):
                    print(line1)
                    file_to_write.write(line1+ '\n')

        for seg in soup.find_all('doc'):
            if seg.has_attr('docid'):
                print('new document')
                new_document = True
                # the previous doc had only one sentence and not written in case of extended context
                if (no_sentences_per_doc == 1):
                    if mode_of_work == 3:
                        file_to_write.write(keep_sentence + '\n')
                    elif mode_of_work == 4:
                        file_to_write.write(gender + ' '+keep_sentence + '\n')
                no_sentences_per_doc = 0
                keep_sentence = ''
            if seg.has_attr('gender'):
                gender = seg.get('gender')
                print(gender)

        if not line_read: break  # EOF


if __name__ == "__main__":
    #preparing the test gebio
    #make_new_corpus_of_two_lines_seg_file('/home/christine/Phd/Gebiotoolkit-master/gebiocorpus_v2/he.1000.doc.es',1,'es')

    # get_random_test_valid_src_trg('Europarl_talks_Eva/EN_ES_extended_gendered/EN.en-es.txt', 'Europarl_talks_Eva/EN_ES_extended_gendered/ES.en-es.txt', len(gender_list), 4000, 'en', 'es', 'test_', 'train')




    # add_tag_to_file('Europarl_talks_Eva/EN_ES_original/train.en', 'Europarl_talks_Eva/EN_ES_gendered/train.en', gender_list)

    # make_new_corpus_of_two_lines('Europarl_talks_Eva/EN_ES_original/train.en', 'Europarl_talks_Eva/EN_ES_extended/train.en', id_list)

    parser = argparse.ArgumentParser()
    parser.add_argument("--src_file", help="The file of the source language")
    parser.add_argument("--src_file_prepared", help="The file of the source language after preparation")
    parser.add_argument("--trg_file", help="The file of the target language")
    parser.add_argument("--trg_file_prepared", help="The file of the source language after preparation")
    parser.add_argument("--src", help="the src language")
    parser.add_argument("--trg", help="the trg language")
    parser.add_argument("--train_file_name", help="the train file name")
    parser.add_argument("--test_file_name", help="the test file name")
    parser.add_argument("--tag_file", help="the tag file path")
    parser.add_argument("--add_tag", default=False, help="add tag or extend.")

    args = parser.parse_args()
    '''
    src_file = args.src_file
    src_file_prepared = args.src_file_prepared
    trg_file = args.trg_file
    trg_file_prepared = args.trg_file_prepared
    src= args.src
    trg=args.trg
    train_file_name=args.train_file_name
    test_file_name=args.test_file_name
    if(args.add_tag is not None):
        add_tag=args.add_tag
    tag_file = args.tag_file
    '''

    # preparing the Eurparl trainging set

    tag_file = 'Europarl_talks_Eva/EN_ES_original/Tags.en-es.txt'
    src_file = 'Europarl_talks_Eva/EN_ES_original/EN.en-es.txt'
    src_file_prepared = 'Europarl_talks_Eva/EN_ES_extended_gendered/train_.en'
    trg_file = 'Europarl_talks_Eva/EN_ES_original/ES.en-es.txt'
    trg_file_prepared = 'Europarl_talks_Eva/EN_ES_extended_gendered/train_.es'
    src = 'en'
    trg = 'es'
    train_file_name = 'train'
    test_file_name = 'test_'
    add_tag=False
    add_tag_extended=True
    [gender_list, id_list] = read_gender_indices(tag_file)
    #adding tags

    if add_tag:
        add_tag_to_file(src_file, src_file_prepared, gender_list)
        add_tag_to_file(trg_file, trg_file_prepared, gender_list)

        #get the random test,valid set
        get_random_test_valid_src_trg(src_file_prepared, trg_file_prepared,len(gender_list), 4000, src, trg, train_file_name, test_file_name)
    elif add_tag_extended:
        make_extended_gendered(src_file, src_file_prepared, id_list, gender_list)
        make_extended_gendered(trg_file, trg_file_prepared, id_list, gender_list)
        # get the random test,valid set
        get_random_test_valid_src_trg(src_file_prepared, trg_file_prepared, len(gender_list), 4000, src, trg, train_file_name, test_file_name)

    else:
        make_new_corpus_of_two_lines(src_file, src_file_prepared,id_list)
        make_new_corpus_of_two_lines(trg_file, trg_file_prepared, id_list)
        # get the random test,valid set
        get_random_test_valid_src_trg(src_file_prepared, trg_file_prepared,len(gender_list), 4000, src, trg, train_file_name, test_file_name)


    '''
    src_file = 'Europarl_talks_Eva/EN_ES_extended_gendered/EN.en-es.txt'
    trg_file = 'Europarl_talks_Eva/EN_ES_extended_gendered/ES.en-es.txt'

    get_random_test_valid_src_trg(src_file, trg_file,len(gender_list), 4000, src, trg, train_file_name, test_file_name)
    '''
