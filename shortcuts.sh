#!/bin/bash
set -euo pipefail

vscode_tests() {
    uv run python \
        -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:9292 --wait-for-client -m pytest \
        --log-level=ERROR "$@"
}
test() {
    uv run python -m pytest --log-level=ERROR "$@"
}

cmd="${1:-}"
shift || true

case "$cmd" in
    vscode_tests)
        vscode_tests "$@"
        ;;
    test)
        test "$@"
        ;;
    *)
        uv run "$cmd" "$@"
        ;;
esac
