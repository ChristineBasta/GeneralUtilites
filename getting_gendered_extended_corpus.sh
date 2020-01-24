#!/usr/bin/env bash

tag_file='Europarl_talks_Eva/EN_ES_original/Tags.en-es.txt'
src_file='Europarl_talks_Eva/EN_ES_extended_gendered/EN.en-es.txt'
src_file_prepared='Europarl_talks_Eva/EN_ES_gendered/train.en'
trg_file='Europarl_talks_Eva/EN_ES_extended_gendered/ES.en-es.txt'
trg_file_prepared='Europarl_talks_Eva/EN_ES_gendered/train_.es'
src='en'
trg='es'
train_file_name='train'
test_file_name='test'

python read_gendered_corpus.py --tag_file $tag_file --src_file $src_file --src_file_prepared $src_file_prepared --trg_file $trg_file \
--trg_file_prepared $trg_file_prepared  --src $src --trg $trg  --train_file_name $train_file_name --test_file_name $test_file_name