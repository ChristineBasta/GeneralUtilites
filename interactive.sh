#!/bin/bash
#SBATCH -p veu # Partition to submit to
#SBATCH --gres=gpu:1
#SBATCH --mem=10G # Memory
#SBATCH --ignore-pbs
#SBATCH --output=interlactive-multi-enru-big2.log

SRC="src"
TGT="tgt"

CP_DIR="save/europarl_extended_joint_attention"

DEST_DIR="data-bin/Europarl_extended"


CP="checkpoint_best.pt"

MULTI_BLEU='/veu4/usuaris31/moses/mosesdecoder/scripts/generic/multi-bleu.perl'

input="/home/usuaris/veu/christine.raouf.saad/joint/Europarl_talks_Eva/gebio_test_files/she_gebio_original.tok.tc.en"
reference="/home/usuaris/veu/christine.raouf.saad/joint/Europarl_talks_Eva/gebio_test_files/she_gebio_original.tok.tc.es"
pair="enru"
output="Europarl_talks_Eva/gebio_test_files/translation_extended"
#Apply multilingual source codes to the data
mkdir -p tmp
#interactive
CUDA_VISIBLE_DEVICES="" fairseq-interactive $DEST_DIR --path $CP_DIR/$CP \
   --beam 5 --batch-size 1 --task translation --remove-bpe < $input > $output
#clean
python clean-output.py < $output > $output.cl
#remove bpe
sed -r 's/(@@ )|(@@ ?$)//g' < $reference > $reference.nobpe

#compute blue score
fairseq-score --sys $output.cl -r $reference.nobpe

#for extended

#sed 's/<sep>.*//' test.tok.tc.es > test.tok.tc.es.nosep
