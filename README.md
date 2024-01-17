# Bunya Jobs

**⚠️This repo is still under ACTIVE development.**

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
