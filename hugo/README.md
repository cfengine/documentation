# Alvaldi Docs

## Local preview

Using docker / podman to build and serve is fairly straight forward:

```
docker build --tag alvaldi-docs -f Containerfile . && docker run -p 80:80 -it --name alvaldi-docs --rm alvaldi-docs
```

If you wish to properly date a content item for the future, such as when drafting
a blog post, you can change the `Containerfile` or your local `hugo` command to
include `-D --buildDrafts` and `-F --buildFuture` so
`hugo --buildDrafts --buildFuture --logLevel info` instead of `hugo --logLevel info`.
