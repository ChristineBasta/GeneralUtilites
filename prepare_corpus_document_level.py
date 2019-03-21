import argparse

def make_new_corpus_of_two_lines(file, file_path_to_write):
    file_read = open(file, 'r')
    file_to_write = open(file_path_to_write, 'w')
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


if __name__ == "__main__":

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