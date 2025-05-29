#!/bin/sh

mkdir -p /home/proxy/logs/forever
forever start /usr/share/search/server/forever.json

nginx_conf=/etc/nginx/nginx.conf

IS_HTTPS=${IS_HTTPS:-"false"}

if [[ "$IS_HTTPS" == "true" ]]; then
    PROTO_REDIRECT_CONFIG='if ($http_x_forwarded_proto != "https") { rewrite ^(.*)$ https://$host$1 permanent; }'
    sed -i "s~PROTO_REDIRECT_CONFIG~$PROTO_REDIRECT_CONFIG~g" $nginx_conf
else
    sed -i "s~PROTO_REDIRECT_CONFIG~~g" $nginx_conf
fi

nginx -g 'daemon off;'
