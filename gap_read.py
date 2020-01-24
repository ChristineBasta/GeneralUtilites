
import re

def read_gap(file, file_gap_write, file_gap_write_tsv):
    file_read = open(file, 'r', encoding='utf8')
    file_write= open(file_gap_write, 'a+')
    file_write_tsv=open(file_gap_write_tsv, 'a+')
    index = 1
    new_document = True

    while True:

        line2 = file_read.readline().strip().replace('\n', '')

        info=line2.split('\t')
        if(line2):
            length_words=len(re.findall(r'\w+', info[1]))
            if( length_words >100):
                print(info[1])
                file_write.write(info[1]+'\n')
                file_write_tsv.write(line2+'\n')


        index = index + 1
        if not line2: break  # EOF



read_gap('/home/christine/Documents/gap-coreference-master/gap-test.tsv','/home/christine/Documents/gap-coreference-master/long_sentences_file.txt', '/home/christine/Documents/gap-coreference-master/long_sentences_file.tsv')