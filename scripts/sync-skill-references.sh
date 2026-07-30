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

  # Resolve the transitive closure of shared references the skill needs: the
  # ones its SKILL.md cites, plus everything those cite in turn. Without this a
  # standalone package ships a reference that points at a file it does not
  # contain.
  required_references=()
  pending=()

  for shared_reference in "${shared_references_root}"/*.md; do
    reference_name="$(basename "${shared_reference}")"
    if grep -Fq "references/${reference_name}" "${skill_file}"; then
      required_references+=("${reference_name}")
      pending+=("${reference_name}")
    fi
  done

  while ((${#pending[@]})); do
    current="${pending[0]}"
    pending=("${pending[@]:1}")
    current_path="${shared_references_root}/${current}"
    [[ -f "${current_path}" ]] || continue

    while read -r dependency; do
      [[ -n "${dependency}" ]] || continue
      [[ -f "${shared_references_root}/${dependency}" ]] || continue

      for seen in ${required_references[@]+"${required_references[@]}"}; do
        [[ "${seen}" == "${dependency}" ]] && continue 2
      done

      required_references+=("${dependency}")
      pending+=("${dependency}")
    done < <(grep -oE '`references/[a-z0-9-]+\.md`' "${current_path}" |
      sed 's|`references/||; s|`||' | sort -u)
  done

  for shared_reference in "${shared_references_root}"/*.md; do
    reference_name="$(basename "${shared_reference}")"
    target_reference="${skill_references_root}/${reference_name}"

    is_required=0
    for required in ${required_references[@]+"${required_references[@]}"}; do
      if [[ "${required}" == "${reference_name}" ]]; then
        is_required=1
        break
      fi
    done

    if ((is_required)); then
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

  # Every shipped reference must be reachable from its SKILL.md, directly or
  # through another reference. This also prunes copies orphaned when a shared
  # reference is renamed or deleted, which the loop above cannot see because it
  # iterates the shared directory.
  for existing_reference in "${skill_references_root}"/*.md; do
    [[ -f "${existing_reference}" ]] || continue

    reference_name="$(basename "${existing_reference}")"
    grep -Fq "references/${reference_name}" "${skill_file}" && continue

    is_required=0
    for required in ${required_references[@]+"${required_references[@]}"}; do
      if [[ "${required}" == "${reference_name}" ]]; then
        is_required=1
        break
      fi
    done
    ((is_required)) && continue

    if [[ "${mode}" == "--check" ]]; then
      echo "Uncited reference: ${existing_reference}" >&2
      status=1
    else
      rm "${existing_reference}"
    fi
  done

  if [[ -d "${skill_references_root}" ]]; then
    rmdir "${skill_references_root}" 2>/dev/null || true
  fi
done

if [[ "${mode}" == "--check" && "${status}" -eq 0 ]]; then
  echo "Skill-local shared references are current."
fi

exit "${status}"
