# issue-from-pytest-log

Create an issue for failed tests from a pytest-reportlog file

## Usage

To use the `issue-from-pytest-log` action in workflows, simply add a new step:
```yaml
jobs:
  my-job:
    ...

    - uses: keewis/issue-from-pytest-log@version
      with:
        ...
```
