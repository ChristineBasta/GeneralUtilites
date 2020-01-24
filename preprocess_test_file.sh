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
lang=en-es
INPUT_DIR=Gebiotoolkit-master/gebiocorpus_v2
OUTPUT_DIR=Gebiotoolkit-master/gebiocorpus_v2/output
type=original
tmp=$OUTPUT_DIR
truecase_code_folder=Europarl_talks_Eva/EN_ES_
split_no=2000

mkdir $OUTPUT_DIR

BPE_CODE=$truecase_code_folder$type/code

test_file=test_
#############take care of the inputs formats ########################################
####we just need the train files to be train.en and train.es for example######
####we just need the train files to be test_.en and test_.es for example######
############## tokenize, truecase, clean##############################################

########tokenize, truecase test, valid##############
#test file before splitting
gender1=he_gebio_
gender2=she_gebio_
for g in $gender1 $gender2; do
  for LANG in $src $tgt
  do
    log "Processing dev/test [$LANG] data..."
    echo $g$type.$LANG
    echo $g
    tokenize $LANG < $INPUT_DIR/$g$type.$LANG > $OUTPUT_DIR/$g$type.tok.$LANG
    #rm $INPUT_DIR/$test_file.$LANG
    ####using the same truecasing we used in tokenization######
    echo $truecase_code_folder$type/truecasing.$LANG
    truecase $truecase_code_folder$type/truecasing.$LANG < $OUTPUT_DIR/$g$type.tok.$LANG > $INPUT_DIR/$g$type.tok.tc.$LANG
    rm  $OUTPUT_DIR/$g$type.tok.$LANG
  done
done





####learning byte code on byte learnt in training######
for g in $gender1 $gender2; do
  for L in $src $tgt; do
      for f in  $g$type.tok.tc.$L ; do
          echo "apply_bpe.py to ${f}..."
          python $BPEROOT/apply_bpe.py -c $BPE_CODE < $INPUT_DIR/$f > $OUTPUT_DIR/$f
      done
  done
done




