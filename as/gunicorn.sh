# personal gunicorn script
# runs a daemon process
# see processes with ps -<something>


SETTINGS=personal.settings
WSGI=personal.wsgi
SOCK=/opt/proc/personal-gunicorn.sock
PID=/opt/proc/personal-gunicorn.pid
WORKERS=3
NAME=personal_webapp
LOGFILE=/opt/proc/personal-gunicorn.log

gunicorn \
    --env DJANGO_SETTINGS_MODULE=$SETTINGS \
    $WSGI:application \
    --pid $PID \
    --bind unix:$SOCK \
    --workers $WORKERS \
    --name $NAME \
    --daemon \
    --log-file=$LOGFILE
