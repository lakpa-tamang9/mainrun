#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --job-name=mainex
#SBATCH -w legolas
#SBATCH --output=mainrun/logs/%x_%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=l.tamang@deakin.edu.au
source activate gpt2
# Environment setup
nvidia-smi
export NCCL_P2P_DISABLE=1
lscpu | grep "^CPU(s):"
export OMP_NUM_THREADS=1

cd /home/tamangld/llm/mainrun/mainrun
python train.py cr cyclic
python train.py cr edge
python train.py cr token
python train.py no_cr cyclic
python train.py no_cr edge
python train.py no_cr token

