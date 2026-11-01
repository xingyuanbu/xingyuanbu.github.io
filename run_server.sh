#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"
bundle exec jekyll serve --livereload --host 127.0.0.1 "$@"
