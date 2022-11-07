import re
import sys

import hypothesis.strategies as st
from hypothesis import given, note

import parse_logs

directory_re = r"(\w|-)+"
path_re = re.compile(rf"/?({directory_re}(/{directory_re})*/)?test_[A-Za-z0-9_]+\.py")
filepaths = st.from_regex(path_re, fullmatch=True)

group_re = r"Test[A-Za-z0-9_]+"
name_re = re.compile(rf"({group_re}::)*test_[A-Za-z0-9_]+")
names = st.from_regex(name_re, fullmatch=True)

variants = st.from_regex(re.compile(r"(\w+-)*\w+"), fullmatch=True)

messages = st.text()


def preformatted_reports():
    return st.tuples(filepaths, names, variants | st.none(), messages).map(
        lambda x: parse_logs.PreformattedReport(*x)
    )


@given(filepaths, names, variants)
def test_parse_nodeid(path, name, variant):
    if variant is not None:
        nodeid = f"{path}::{name}[{variant}]"
    else:
        nodeid = f"{path}::{name}"

    note(f"nodeid: {nodeid}")

    expected = {"filepath": path, "name": name, "variant": variant}
    actual = parse_logs.parse_nodeid(nodeid)

    assert actual == expected


@given(st.lists(preformatted_reports()), st.integers(min_value=0))
def test_truncate(reports, max_chars):
    py_version = ".".join(str(part) for part in sys.version_info[:3])

    formatted = parse_logs.truncate(reports, max_chars=max_chars, py_version=py_version)

    assert formatted is None or len(formatted) <= max_chars
