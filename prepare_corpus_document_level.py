


def make_new_corpus_of_two_lines(file, file_path_to_write):
    file_read = open(file, 'r')
    file_to_write = open(file_path_to_write, 'w')
    keep_second_line = ''
    line1 = file_read.readline().strip().replace('\n','')
    line = file_read.readline().strip().replace('\n','')
    file_to_write.write(line1+' <sep> '+line)
    print(line1+' <sep> '+line)
    while True:
        keep_last_line= line

        line = file_read.readline().strip().replace('\n','')

        print(keep_last_line + ' <sep> '+ line)
        file_to_write.write(keep_last_line + ' <sep> '+ line)
        if not line: break  # EOF




make_new_corpus_of_two_lines('/home/usuaris/veu/christine.raouf.saad/corpora/FairSeq_Training/training.en-es.sorted.tc.60.en','/home/usuaris/veu/christine.raouf.saad/corpora/FairSeq_adrian/training.en-es.doubled.en')



make_new_corpus_of_two_lines('/home/usuaris/veu/christine.raouf.saad/corpora/FairSeq_Training/training.en-es.sorted.tc.60.es','/home/usuaris/veu/christine.raouf.saad/corpora/FairSeq_adrian/training.en-es.doubled.es')


