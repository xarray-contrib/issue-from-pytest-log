# issue-from-pytest-log

Create or update an issue for failed tests from a pytest-reportlog file.

## Usage

To use the `issue-from-pytest-log` action in workflows, simply add a new step:
```yaml
jobs:
  my-job:
    ...
    strategy:
      fail-fast: false
      ...

    ...

    - uses: actions/setup-python@v4
      with:
        python-version: "3.10"
        cache: pip

    ...

    - uses: xarray-contrib/issue-from-pytest-log@main
      if: |
        failure()
        && ...
      with:
        log-path: pytest-log.jsonl
```
