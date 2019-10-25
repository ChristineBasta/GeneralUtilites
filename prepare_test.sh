#!/bin/bash



MOSES_BIN=/veu4/usuaris31/xtrans/mosesdecoder/bin
SCRIPTS_ROOTDIR=/veu4/usuaris31/xtrans/mosesdecoder/scripts/
SCRIPTS=/veu4/usuaris31/moses/mosesdecoder/scripts/
TOKENIZER=$SCRIPTS/tokenizer/tokenizer.perl
CLEAN=$SCRIPTS/training/clean-corpus-n.perl
NORM_PUNC=$SCRIPTS/tokenizer/normalize-punctuation.perl
REM_NON_PRINT_CHAR=$SCRIPTS/tokenizer/remove-non-printing-char.perl
BPEROOT=subword-nmt
BPE_TOKENS=32000
BPE_CODE=/joint/wmt16_en_de_bpe32k/bpe.32000
#tokenizing
$TOKENIZER -threads 8 -a -l en \
    < test_wmt14_ende.en \
    > test_wmt14_ende.tok.en

#subwording

python $BPEROOT/apply_bpe.py -c $BPE_CODE < test_wmt14_ende.tok.en > test_wmt14_ende.bp.32000.tok.en

