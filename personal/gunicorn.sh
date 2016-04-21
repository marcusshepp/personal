# django gunicorn script
# Generates a Daemon process with Gunicorn.
# see processes with ps -aux
# tested on: Ubuntu 14.04.3 LTS (GNU/Linux 3.13.0-74-generic x86_64), aws ec2
# Runs on apps built with Django==1.9
# Marcus Shepherd <marcusshepdotcom@gmail.com>
# 3-12-16


NAME=personal
SETTINGS=$NAME.settings
SOCK=/opt/proc/$NAME-gunicorn.sock
PID=/opt/proc/$NAME-gunicorn.pid
LOGFILE=/opt/proc/$NAME-gunicorn.log
WORKERS=3


DIRECT=/opt/proc/
echo 'Creating Daemon process for: '$NAME
echo 'LOGFILE: '$LOGFILE


DIRECT=/opt/proc/
echo "does $DIRECT exist?"
if ! [[ -d $DIRECT ]]; then
    ls -la /opt/
    echo $DIRECT" does not exist.. creating.."
    sudo mkdir $DIRECT
    ls -la /opt/
else
    echo "Yes it does."
    echo "removing /opt/proc/$NAME*"
    rm -rf /opt/proc/$NAME*
fi

gunicorn \
    --env DJANGO_SETTINGS_MODULE=$SETTINGS \
    $NAME.wsgi:application \
    --pid $PID \
    --bind unix:$SOCK \
    --workers $WORKERS \
    --name $NAME \
    --daemon \
    --log-file=$LOGFILE

# run from /opt/dollars
