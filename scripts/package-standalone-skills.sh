#!/usr/bin/env bash

set -euo pipefail

script_directory="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
repository_root="$(CDPATH= cd -- "${script_directory}/.." && pwd)"
plugin_root="${repository_root}/plugins/larsen-skills"
manifest_path="${plugin_root}/.codex-plugin/plugin.json"
version="$(awk -F'"' '/"version"/ { print $4; exit }' "${manifest_path}")"
output_root="${1:-${repository_root}/dist/larsen-skills-${version}}"
skills_output="${output_root}/skills"
archives_output="${output_root}/zips"
reference_sync_script="${script_directory}/sync-skill-references.sh"

if [[ -z "${version}" ]]; then
  echo "Could not read the plugin version from ${manifest_path}." >&2
  exit 1
fi

if [[ -e "${output_root}" ]]; then
  echo "Output already exists: ${output_root}" >&2
  echo "Choose a new output path or remove the existing build deliberately." >&2
  exit 1
fi

for required_command in zip shasum; do
  if ! command -v "${required_command}" >/dev/null 2>&1; then
    echo "Required command is unavailable: ${required_command}" >&2
    exit 1
  fi
done

"${reference_sync_script}" --check

mkdir -p "${skills_output}" "${archives_output}"

for source_skill in "${plugin_root}"/skills/*; do
  [[ -d "${source_skill}" ]] || continue

  skill_name="$(basename "${source_skill}")"
  packaged_skill="${skills_output}/${skill_name}"
  packaged_skill_file="${packaged_skill}/SKILL.md"

  cp -R "${source_skill}" "${packaged_skill}"

  if grep -q '\.\./\.\./references/' "${packaged_skill_file}"; then
    echo "Non-portable reference found in ${packaged_skill_file}." >&2
    exit 1
  fi

  cp "${repository_root}/LICENSE" "${packaged_skill}/LICENSE"

  (
    cd "${skills_output}"
    zip -qry "${archives_output}/${skill_name}.zip" "${skill_name}"
  )
done

(
  cd "${archives_output}"
  shasum -a 256 ./*.zip > SHA256SUMS
)

echo "Standalone skill folders: ${skills_output}"
echo "Upload-ready ZIP files: ${archives_output}"
