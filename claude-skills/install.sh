#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: claude-skills/install.sh [--dry-run | --apply] [--skills-dir DIRECTORY]

Default: dry-run. Link skills into $HOME/.claude/skills.
Existing files and links to different targets are never replaced.
Any conflict aborts the entire installation before creating links.
Run as the intended user, without sudo. No state directory is created.
EOF
}

if [[ -n ${SUDO_USER-} ]]; then
  printf 'Refusing to run under sudo; run as the intended user.\n' >&2
  exit 1
fi

apply=false
skills_dir="$HOME/.claude/skills"
while (($#)); do
  case "$1" in
    --dry-run) apply=false ;;
    --apply) apply=true ;;
    --skills-dir)
      if (($# < 2)) || [[ -z $2 || $2 == --* ]]; then
        usage >&2
        exit 2
      fi
      skills_dir=$2
      shift
      ;;
    -h|--help) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

# Reject obstructed parent paths before creating any skill links.
check_directory() {
  local path=$1 parent
  while [[ ! -e $path && ! -L $path ]]; do
    parent=$(dirname -- "$path")
    [[ $parent != "$path" ]] || break
    path=$parent
  done
  [[ -d $path ]] || {
    printf 'conflict: %s is not a usable directory\n' "$path" >&2
    return 1
  }
}
check_directory "$skills_dir"

source_dir=$(cd "$(dirname "$0")" && pwd -P)
skills_path=$(realpath -m -- "$skills_dir")
skills_dir=$skills_path
sources=()
destinations=()
conflicts=0
for skill_file in "$source_dir"/*/SKILL.md; do
  [[ -f $skill_file ]] || continue
  source=$(dirname "$skill_file")
  destination="$skills_dir/$(basename "$source")"
  # Never link into a registry or skill tree, including through aliases.
  for tree in "$source_dir" "$(dirname -- "$(realpath -- "$source")")"; do
    if [[ $skills_path == "$tree" || $skills_path == "$tree"/* ]]; then
      printf 'conflict: skills destination %s is inside source tree %s\n' "$skills_dir" "$tree" >&2
      exit 1
    fi
  done
  if [[ -L $destination && $(readlink -- "$destination") == "$source" ]]; then
    printf 'ok: %s -> %s\n' "$destination" "$source"
  elif [[ -L $destination && $destination -ef $source ]]; then
    # ponytail: legacy chains (e.g. via ~/.claude/skills/geo) break when the
    # intermediate link is retired; report them instead of migrating.
    printf 'conflict: %s reaches %s only via %s; after review, unlink it and re-run\n' \
      "$destination" "$source" "$(readlink -- "$destination")" >&2
    conflicts=1
  elif [[ -e $destination || -L $destination ]]; then
    printf 'conflict: %s already exists; inspect it manually\n' "$destination" >&2
    conflicts=1
  else
    sources+=("$source")
    destinations+=("$destination")
  fi
done

((conflicts == 0)) || exit 1
for i in "${!sources[@]}"; do
  if $apply; then
    mkdir -p -- "$(dirname -- "${destinations[$i]}")"
    ln -sT -- "${sources[$i]}" "${destinations[$i]}"
    printf 'apply: %s -> %s\n' "${destinations[$i]}" "${sources[$i]}"
  else
    printf 'dry-run: ln -sT %q %q\n' "${sources[$i]}" "${destinations[$i]}"
  fi
done

if $apply; then
  printf 'Install complete. Start a new Claude Code session to reload skills.\n'
else
  printf 'Dry run only. Re-run with --apply after reviewing every destination.\n'
fi
