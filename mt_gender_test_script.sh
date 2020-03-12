#!/usr/bin/env bash
#
# Adapted from https://github.com/facebookresearch/MIXER/blob/master/prepareData.sh

SCRIPTS=/home/christine/Phd/Cristina_cooperation/joint/mosesdecoder/scripts
TOKENIZER=$SCRIPTS/tokenizer/tokenizer.perl
LC=$SCRIPTS/tokenizer/lowercase.perl
CLEAN=$SCRIPTS/training/clean-corpus-n.perl
BPEROOT=/home/christine/Phd/Cristina_cooperation/joint/subword-nmt
BPE_TOKENS=31000

#####load the scripts to call later easier######
. $SCRIPTS/generic.sh

src=en
tgt=es
#INPUT_DIR=Gebiotoolkit-master/gebiocorpus_v2
#OUTPUT_DIR=Gebiotoolkit-master/gebiocorpus_v2/output
INPUT_DIR=mt_gender
OUTPUT_DIR=mt_gender/output
tmp=$OUTPUT_DIR
truecase_code_folder=Europarl_talks_Eva/EN_ES_original
split_no=2000

mkdir $OUTPUT_DIR mt_gender

BPE_CODE=$truecase_code_folder/code

test_file=test_
#############take care of the inputs formats ########################################
####we just need the train files to be train.en and train.es for example######
####we just need the train files to be test_.en and test_.es for example######
############## tokenize, truecase, clean##############################################

########tokenize, truecase test, valid##############
#test file before splitting
file=en-winogender
LANG=en

log "Processing dev/test [$LANG] data..."

tokenize $LANG < $INPUT_DIR/$file > $OUTPUT_DIR/$file.tok
#rm $INPUT_DIR/$test_file.$LANG
####using the same truecasing we used in tokenization######

truecase $truecase_code_folder/truecasing.$LANG < $OUTPUT_DIR/$file.tok > $OUTPUT_DIR/$file.tok.tc
rm  $$OUTPUT_DIR/$file.tok
echo "apply_bpe.py to ${f}..."
python $BPEROOT/apply_bpe.py -c $BPE_CODE < $OUTPUT_DIR/$file.tok.tc > $OUTPUT_DIR/$file.tok.tc.bpe






