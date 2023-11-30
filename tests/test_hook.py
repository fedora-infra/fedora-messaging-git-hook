import re
import tomli_w
def _make_config(tmp_path, **kwargs):
    config_path = tmp_path / "config.toml"
    with open(tmp_path / "config.toml", "wb") as fmconfig:
        tomli_w.dump({"consumer_config": kwargs}, fmconfig)
    return config_path.as_posix()


def _get_commit_id(git_dir, refspec="main"):
        ["git", "rev-list", "-1", refspec],
        last_commit_id = _get_commit_id(git_dir)
    config_path = _make_config(
        tmp_path, url_template="http://example.com/{repo_fullname}/c/{rev}?branch={branch}"
    )
        result = run_hook(git_repo / ".git", args=["--config", config_path])
        # print(result.stdout, result.exc_info)
    assert all(m.body["commit"]["branch"] == "main" for m in sent_messages)
    # Summary
    # Stats
    # Rev
    revs = (
        run(
            ["git", "rev-list", "--reverse", "main"],
            stdout=PIPE,
            cwd=git_repo,
            check=True,
            universal_newlines=True,
        )
        .stdout.strip()
        .splitlines()
    )
    assert [m.body["commit"]["rev"] for m in sent_messages] == revs
    # Date
    assert all(
        re.match(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[+-]\d\d:\d\d", m.body["commit"]["date"])
        is not None
        for m in sent_messages
    )
    # Patch
    assert sent_messages[1].body["commit"]["patch"] == (
        "diff --git a/something.txt b/something.txt\n"
        "new file mode 100644\n"
        "index 0000000..e69de29\n"
        "--- /dev/null\n"
        "+++ b/something.txt\n"
    )
    # URL
    for index, msg in enumerate(sent_messages):
        refspec = "main" + ((1 - index) * "^")
        commit_id = _get_commit_id(git_repo, refspec=refspec)
        assert msg.body["commit"]["url"] == "http://example.com/repo/c/{}?branch=main".format(
            commit_id
        )
        # print(result.stdout, result.exc_info)
    config_path = _make_config(tmp_path, with_namespace=True)
        result = run_hook(git_repo / ".git", ["--config", config_path])
        # print(result.stdout, result.exc_info)
        last_commit_id = _get_commit_id(git_repo)
        # print(result.stdout, result.exc_info)