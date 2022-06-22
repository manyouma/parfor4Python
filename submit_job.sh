#!/bin/bash

#SBATCH --account=rrg-vincentw
#SBATCH --cpus-per-task=24
#SBATCH --mem=128000M       # Memory proportional to GPUs: 32000 Cedar, 64000 Graham.
#SBATCH --time=00-24:00:00
#SBATCH --job-name=jun22_test
#SBATCH --output=%x-%j.out

module load python/3.8.10
#source /home/manyouma/projects/def-vincentw/manyouma/WhittleLearn/new_env/bin/activate


# if gpu is to be used
python parallel_VI.py



