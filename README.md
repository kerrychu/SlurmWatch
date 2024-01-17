# SlurmWatch

**⚠️This repo is still under ACTIVE development.**

## Huh?
- **Slurm** is a robust open-source workload manager designed for high-performance computing clusters. It efficiently allocates resources, manages job submissions, and optimizes task execution. With commands like `sbatch` and `squeue`, Slurm provides a flexible and scalable solution for seamless task control and monitoring, making it a preferred choice in academic and research settings. Various research centers and universities have unique names for their Slurm clusters. At the University of Queensland, our clusters go by the distinctive name "Bunya."

## SlurmWatch

Introducing **SlurmWatch** - a tool meticulously crafted for effortless monitoring of sbatch jobs. Say goodbye to uncertainties; experience prompt notifications, ensuring you stay informed and in control.

## Scheduling

- For the moment, you can fork it, or just clone it and use crontab to run `monitor.py`
- Follow the `dot_env_template` to create your own `.env` file
- then do `crontab -e`
- and add `* * * * * your-python-path complete-file-path-to-monitor.py` to your cronjob
  - for example, `* * * * * ~/anaconda3/bin/python /scratch/user/your-username/bunya_jobs/monitor.py`
- then your jobs will be monitored at an 1 minute interval
- if you wish to have a different interval, check this [page](https://www.atatus.com/tools/cron).

## Slack Integration

- follow [slack webhook tutorial](https://api.slack.com/messaging/webhooks) to create a slack app for your slack workspace and add it to appropriate channels
- remember to replace the `.env` webhook to your own

## Future Features
- notification when job status change
- enable capability to monitor multiple users jobs instead of the signed in user
- flexible configuration


## Future Integrations

Currently, the future integrations considered are
- email

Feel free to create an issue or contact me at `xiaoran.chu@uq.edu.au` (call me kerry please)

or

Simply fork the repo and create a pull request and let's crunch some code together.

## Useful links

- [Slurm official site](https://slurm.schedmd.com/)
- [Slurm GitHub](https://github.com/SchedMD/slurm)
- [sbatch command](https://slurm.schedmd.com/sbatch.html)