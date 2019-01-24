import re

#split line by line and replace the tokens in the lines
def read_file_line_by_line(file, file_es, file_en):
    file_es = open(file_es, 'w')
    file_en = open(file_en, 'w')
    with open(file) as f:
        for line in f:

            lan=line.split('\t')
            print (lan [0])
            file_es.write(lan[0]+'\n')
            print(lan[1])
            #replace a regex
            print(re.sub("<b_crf>.*?<e_crf> ", "", lan[1]))
            en_line = re.sub("<b_crf>.*?<e_crf> ", "", lan[1])
            file_en.write(en_line+'\n')
            print ('**')


#split line by line...but before using ..check its suitability to ur file
def read_file_line_by_line(file, file_es, file_en):
    file_es = open(file_es, 'w')
    file_en = open(file_en, 'w')
    with open(file) as f:
        for line in f:

            lan=line.split('\t')
            print (lan [0])
            file_es.write(lan[0]+'\n')
            print(lan[1])

            file_en.write(lan[1])
            print ('**')


read_file_line_by_line('/home/christine/DocTrans_2/training1/training.en-es.sorted.tc.60.both','/home/christine/DocTrans_2/training1/training.en-es.sorted.tc.60.both.es','/home/christine/DocTrans_2/training1/training.en-es.sorted.tc.60.both.en')
