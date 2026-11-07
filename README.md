# Bravos security gate

A GitHub Action that gates pull requests on the repository's
[GuardLink](https://docs.bugb.io/guardlink/) threat model. It makes the same rulings
as the pre-PR gate in [Bravos](https://docs.bugb.io/bravos/):

1. **The threat model parses and resolves:** `guardlink validate .`
2. **New claims meet the evidence bar:** `guardlink lint . --since <merge base>`
3. **No undisclosed new exposure:** each new unmitigated `@exposes` must be named in
   the pull request description by its threat and asset id, for example
   `#cmdi on #api`.
4. **No confirmed exploit on a changed file**, unless that file carries an
   `@ticket` for it.

It also writes `guardlink.sarif` for code scanning.

It runs guardlink only: no model, no secret and no licence. A gate input that fails
or does not parse fails the step as unknown; it never passes.

## Use

```yaml
name: security gate
on:
  pull_request:
    types: [opened, synchronize, reopened, edited]

permissions:
  contents: read
  security-events: write
  actions: read

jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - id: bravos
        uses: Bugb-Technologies/bravos-action@v1
      - if: always() && steps.bravos.outputs.sarif-file && github.event.pull_request.head.repo.full_name == github.repository
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: ${{ steps.bravos.outputs.sarif-file }}
          category: guardlink
```

`fetch-depth: 0` is required: the gate compares against the merge base. `edited`
re-runs the gate when the description is changed to disclose an exposure.

## Inputs

| Input | Default | What it is |
| --- | --- | --- |
| `base-ref` | the pull request's base branch | the branch to compare against |
| `pr-body` | the pull request description | where new exposures must be named |
| `working-directory` | `.` | the folder that holds `.guardlink/` |
| `guardlink-version` | `2.5.0` | the guardlink version installed from npm |
| `sarif` | `true` | write `guardlink.sarif` |

## Outputs

| Output | What it is |
| --- | --- |
| `sarif-file` | the path of `guardlink.sarif` |
| `new-exposures` | how many new unmitigated exposures the pull request adds |

## The threat model

The annotations come from your team or your coding agent. With Bravos
(`npm install -g @bugb-technologies/bravos`), `bravos init` sets a repository up and
its skills write the annotations; `bravos sync --ci` writes this gate and a nightly
workflow as plain workflow files instead of this action. See
[Run Bravos in CI/CD](https://docs.bugb.io/bravos/guides/run-bravos-in-cicd/).

## Licence

Bravos Software Licence: see [LICENSE](LICENSE).
