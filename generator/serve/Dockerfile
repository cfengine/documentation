# Serves a locally built docs site together with a working search,
# mirroring production docs.cfengine.com: nginx serves the static site and
# proxies /docs/search to the search server (see nginx.conf), the same way
# Apache does in production. The search server itself is the server.js
# from NorthernTechHQ/infra.
#
# Expected build context (see serve_site in build-locally.sh):
#   search-deps         nt-docs scripts/search/server (package.json + lock)
#
# Expected mounts (see serve_site in build-locally.sh):
#   /site               built _site (nginx root)
#   /docs/<branch>      the same _site, where server.js looks for
#                       <branch>/assets/searchIndex under DOCS_PATH=/docs
#   /search/server.js   search server from the infra repo
FROM nginx:alpine

RUN apk add --no-cache nodejs npm

COPY --from=search-deps package.json package-lock.json /search/
RUN npm ci --prefix /search --omit=dev

COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["sh", "-c", "node /search/server.js & exec nginx -g 'daemon off;'"]
