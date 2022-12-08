#!/usr/bin/bash
#
# Submit with something like:
# > sbatch -o slurm-job.out -N<num_links> -c<num_omp_threads> -t<run_time_limit> slurm-job.sh

# Make sure everything in work/ is prepared!
cd work

set -x

export OASIS_BUILD_PATH=<PATH_TO_OASIS_BUILD_DIR>
export LD_LIBRARY_PATH=${OASIS_BUILD_PATH}/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

time \
srun -n ${SLURM_NNODES} r2c ece-namcouple.yml
