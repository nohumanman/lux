# credit to https://stackoverflow.com/questions/878600/how-to-create-a-cron-job-using-bash-automatically-without-the-interactive-editor
# write out current crontab
crontab -l > mycron
# echo new cron into cron file
echo "$1" >> mycron
# install new cron file
crontab mycron
rm mycron
