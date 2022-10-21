# issue-from-pytest-log

Create or update an issue for failed tests from a pytest-reportlog file.

## Usage

To use the `issue-from-pytest-log` action in workflows, simply add a new step:
```yaml
jobs:
  my-job:
    ...

    - uses: xarray-contrib/issue-from-pytest-log@version
      if: |
        failure()
        && github.event_name == 'schedule'
        && ...
      with:
        log_path: pytest-log.jsonl
```
