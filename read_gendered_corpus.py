import argparse
import re
import random
import os
import io

#experiments for EuroParl

def make_new_corpus_of_two_lines(file, file_path_to_write, id_list):
    file_read = open(file, 'r', encoding='utf8')
    file_to_write = open(file_path_to_write, 'w', encoding='utf8')
    id = id_list[0]
    index = 1
    new_document = True
    line1 = file_read.readline().strip().replace('\n', '')
    while True:
        line2= file_read.readline().strip().replace('\n', '')
        if  (index<len(id_list)):
            if id != id_list[index]:
                id=id_list[index]
                line1=line2

            else:
                file_to_write.write(line1 + ' <sep> ' + line2 + '\n')
                line1=line2


        index = index + 1
        if not line2: break  # EOF


def add_tag_to_file(file_to_read, file_to_write, gender_list):
    file_read = open(file_to_read, 'r', encoding='utf8')
    file_write = open(file_to_write, 'w', encoding='utf8')
    keep_second_line = ''
    index = 0
    while True:

        line = file_read.readline().strip().replace('\n', '')
        if  (index<len(gender_list)):
                file_write.write(gender_list[index] + ' ' + line + '\n')

        index += 1
        if not line: break  # EOF


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
def get_random_test_valid_src_trg(file_src, file_trg, no_lines_to_include, no_random_sentences, src, trg,  train_file_name,test_file_name,):
    random_list = random.sample(range(no_lines_to_include), no_random_sentences)
    get_test_valid(file_src, random_list,src, test_file_name, train_file_name)
    get_test_valid(file_trg, random_list,trg, test_file_name, train_file_name)

def get_test_valid(file, random_list, lg , test_file_name, train_file_name):
    print(random_list)
    path, file_name = os.path.split(file)
    read_file = open(file, 'r', encoding='utf8')
    file_to_write_testing = open(path+'/'+test_file_name+'.' + lg, 'w', encoding='utf8')
    file_to_write_training= open(path+'/'+train_file_name+'.'+lg,  'w', encoding='utf8')
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


if __name__ == "__main__":

    #get_random_test_valid_src_trg('Europarl_talks_Eva/EN_ES_trial/EN.en-es.txt', 'Europarl_talks_Eva/EN_ES_trial/ES.en-es.txt', len(gender_list), 4000, 'en', 'es', 'test_', 'train')


    #[gender_list, id_list]=read_gender_indices('Europarl_talks_Eva/EN_ES/Tags.en-es.txt')
    #add_tag_to_file('Europarl_talks_Eva/EN_ES/train.en', 'Europarl_talks_Eva/EN_ES_gendered/train.en', gender_list)


    #make_new_corpus_of_two_lines('Europarl_talks_Eva/EN_ES/train.en', 'Europarl_talks_Eva/EN_ES_extended/train.en', id_list)

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
    tag_file = 'Europarl_talks_Eva/EN_ES/Tags.en-es.txt'
    src_file = 'Europarl_talks_Eva/EN_ES/EN.en-es.txt'
    src_file_prepared = 'Europarl_talks_Eva/EN_ES_extended/train_.en'
    trg_file = 'Europarl_talks_Eva/EN_ES/ES.en-es.txt'
    trg_file_prepared = 'Europarl_talks_Eva/EN_ES_extended/train_.es'
    src = 'en'
    trg = 'es'
    train_file_name = 'train'
    test_file_name = 'test_'
    add_tag=False

    [gender_list, id_list] = read_gender_indices(tag_file)
    #adding tags

    if add_tag:
        add_tag_to_file(src_file, src_file_prepared, gender_list)
        add_tag_to_file(trg_file, trg_file_prepared, gender_list)

        #get the random test,valid set
        get_random_test_valid_src_trg(src_file_prepared, trg_file_prepared,len(gender_list), 4000, src, trg, train_file_name, test_file_name)
    else:
        make_new_corpus_of_two_lines(src_file, src_file_prepared,id_list)
        make_new_corpus_of_two_lines(trg_file, trg_file_prepared, id_list)
        # get the random test,valid set
        get_random_test_valid_src_trg(src_file_prepared, trg_file_prepared,len(gender_list), 4000, src, trg, train_file_name, test_file_name)

    '''
    src_file = 'Europarl_talks_Eva/EN_ES_trial/EN.en-es.txt'
    trg_file = 'Europarl_talks_Eva/EN_ES_trial/ES.en-es.txt'

    get_random_test_valid_src_trg(src_file, trg_file,len(gender_list), 4000, src, trg, train_file_name, test_file_name)
    '''