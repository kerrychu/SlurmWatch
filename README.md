# SlurmWatch

**⚠️This repo is still under ACTIVE development.**

## Python Version Compatibility
python version `>= 3.9`

## Huh?
**Slurm** is a robust open-source workload manager designed for high-performance computing clusters. It efficiently allocates resources, manages job submissions, and optimizes task execution. With commands like `sbatch` and `squeue`, Slurm provides a flexible and scalable solution for seamless task control and monitoring, making it a preferred choice in academic and research settings. Various research centers and universities have unique names for their Slurm clusters. At the University of Queensland, our clusters go by the distinctive name "Bunya."

## SlurmWatch

Introducing **SlurmWatch** - a tool meticulously crafted for effortless monitoring of sbatch jobs. Say goodbye to uncertainties; experience prompt notifications, ensuring you stay informed and in control.

### Current Capabilities

- monitor a single user's (the user signed in) Slurm job(s) -> `src/my_jobs.py`
- monitor multiple users' Slurm GPU job(s) -> `src/gpu_jobs.py`
- monitor resource(GPU) usage of multiple FileSet(s)  -> `src/quota.py`
- monitor resource(Nodes) availability -> `src/available_nodes.py`

### Scheduling

- For the moment, you can fork it, or just clone it and use crontab to run `monitor.py`
- Follow the `dot_env_template` to create your own `.env` file
- then do `crontab -e`
- and add a schedule of your preference
  - for example, `* * * * * ~/anaconda3/bin/python /scratch/user/your-username/SlurmWatch/src/quota.py`
- to choose a schedule of your preference, check this helpful [crontab expression page](https://www.atatus.com/tools/cron).

### Integration

#### Slack

- follow [slack webhook tutorial](https://api.slack.com/messaging/webhooks) to create a slack app for your slack workspace and add it to appropriate channels
- remember to replace the `.env` webhook to your own

### Future Features & Integrations

Currently, the future integrations considered are
- email

Feel free to create an issue or contact me at `xiaoran.chu@uq.edu.au` (call me kerry please)

or

Simply fork the repo and create a pull request and let's crunch some code together.

## Useful links

- [Slurm official site](https://slurm.schedmd.com/)
- [Slurm GitHub](https://github.com/SchedMD/slurm)
- [sbatch command](https://slurm.schedmd.com/sbatch.html)