#!/bin/bash

#SBATCH --account=rrg-vincentw
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000M       # Memory proportional to GPUs: 32000 Cedar, 64000 Graham.
#SBATCH --time=00-1:00:00
#SBATCH --job-name=jun22_test
#SBATCH --output=%x-%j.out

module load python/3.8.10
module load scipy-stack

python parallel_VI.py



