


def make_new_corpus_of_two_lines(file):
    file_read = open(file, 'r')
    keep_second_line = ''
    line1 = file_read.readline().strip().replace('\n','')
    line = file_read.readline().strip().replace('\n','')
    print(line1+' <sep> '+line)
    while True:
        keep_last_line= line

        line = file_read.readline().strip().replace('\n','')

        print(keep_last_line + ' <sep> '+ line)
        if not line: break  # EOF




make_new_corpus_of_two_lines('news-original.en')