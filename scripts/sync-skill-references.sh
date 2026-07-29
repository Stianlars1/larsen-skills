#!/usr/bin/env bash

set -euo pipefail

script_directory="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
repository_root="$(CDPATH= cd -- "${script_directory}/.." && pwd)"
plugin_root="${repository_root}/plugins/larsen-skills"
shared_references_root="${plugin_root}/references"
skills_root="${plugin_root}/skills"
mode="${1:-sync}"

if [[ "${mode}" != "sync" && "${mode}" != "--check" ]]; then
  echo "Usage: $0 [--check]" >&2
  exit 1
fi

status=0

for skill_directory in "${skills_root}"/*; do
  [[ -d "${skill_directory}" ]] || continue

  skill_file="${skill_directory}/SKILL.md"
  skill_references_root="${skill_directory}/references"

  if [[ ! -f "${skill_file}" ]]; then
    echo "Missing skill entrypoint: ${skill_file}" >&2
    status=1
    continue
  fi

  if grep -q '\.\./\.\./references/' "${skill_file}"; then
    echo "Non-portable shared reference in ${skill_file}" >&2
    status=1
  fi

  for shared_reference in "${shared_references_root}"/*.md; do
    reference_name="$(basename "${shared_reference}")"
    target_reference="${skill_references_root}/${reference_name}"

    if grep -Fq "references/${reference_name}" "${skill_file}"; then
      if [[ "${mode}" == "--check" ]]; then
        if [[ ! -f "${target_reference}" ]]; then
          echo "Missing generated reference: ${target_reference}" >&2
          status=1
        elif ! cmp -s "${shared_reference}" "${target_reference}"; then
          echo "Stale generated reference: ${target_reference}" >&2
          status=1
        fi
      else
        mkdir -p "${skill_references_root}"
        cp "${shared_reference}" "${target_reference}"
      fi
    elif [[ -f "${target_reference}" ]]; then
      if [[ "${mode}" == "--check" ]]; then
        echo "Unreferenced generated reference: ${target_reference}" >&2
        status=1
      else
        rm "${target_reference}"
      fi
    fi
  done
done

if [[ "${mode}" == "--check" && "${status}" -eq 0 ]]; then
  echo "Skill-local shared references are current."
fi

exit "${status}"
