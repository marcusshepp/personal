# personal gunicorn script
# runs a daemon process
# see processes with ps -aux
# tested on: Ubuntu 14.04.3 LTS (GNU/Linux 3.13.0-74-generic x86_64), aws ec2

# Marcus Shepherd
# 3-12-16

DIRECT=/opt/proc/
if ! [[ -d $DIRECT ]]; then
    ls -la /opt/
    echo $DIRECT" does not exist.. creating.."
    sudo mkdir $DIRECT
    ls -la /opt/
fi

SETTINGS=personal.settings
SOCK=/opt/proc/personal-gunicorn.sock
PID=/opt/proc/personal-gunicorn.pid
WORKERS=3
NAME=personal_webapp
LOGFILE=/opt/proc/personal-gunicorn.log

gunicorn \
    --env DJANGO_SETTINGS_MODULE=$SETTINGS \
    personal.wsgi:application \
    --pid $PID \
    --bind unix:$SOCK \
    --workers $WORKERS \
    --name $NAME \
    --daemon \
    --log-file=$LOGFILE
