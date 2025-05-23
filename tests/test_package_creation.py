"""Verify package creation using `pytest-copie`"""

import subprocess

import pytest


def successfully_created_project(result):
    """Basic assertions that indicate the copier was able to create a project"""
    return result.exit_code == 0 and result.exception is None and result.project_dir.is_dir()


def contains_required_files(result):
    """Utility method to confirm that the required project files exist in the
    copier result."""
    required_files = [
        ".copier-answers.yml",
        ".git_archival.txt",
        ".gitattributes",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".setup_dev.sh",
        "LICENSE",
        "pyproject.toml",
        "README.md",
    ]
    all_found = True
    for file in required_files:
        if not (result.project_dir / file).is_file():
            all_found = False
            print("Required file not generated:", file)
    return all_found


def directory_structure_is_correct(result, package_name="example_package"):
    """Test to ensure that the default directory structure ws created correctly"""
    return (result.project_dir / f"src/{package_name}").is_dir() and (
        result.project_dir / f"tests/{package_name}"
    ).is_dir()


def black_runs_successfully(result):
    """Test to ensure that the black linter runs successfully on the project"""
    # run black with `--check` to look for lint errors, but don't fix them.
    black_results = subprocess.run(
        ["python", "-m", "black", "--check", (result.project_dir / "src")],
        cwd=result.project_dir,
        check=False,
    )

    return black_results.returncode == 0


def pylint_runs_successfully(result):
    """Test to ensure that the pylint linter runs successfully on the project"""
    # run pylint to ensure that the hydrated files are linted correctly
    pylint_results = subprocess.run(
        [
            "python",
            "-m",
            "pylint",
            "--recursive=y",
            "--rcfile=./src/.pylintrc",
            (result.project_dir / "src"),
        ],
        cwd=result.project_dir,
        check=False,
    )

    return pylint_results.returncode == 0


def unit_tests_in_project_run_successfully(result):
    """Test to ensure that the unit tests run successfully on the project

    !!! NOTE - This doesn't currently work because we need to `pip install` the hydrated
    project before running the tests. And we don't have a way to create a temporary
    virtual environment for the project.
    """
    pytest_results = subprocess.run(["python", "-m", "pytest"], cwd=result.project_dir, check=False)

    return pytest_results.returncode == 0


def docs_build_successfully(result):
    """Test that we can build the doc tree.

    !!! NOTE - This doesn't currently work because we need to `pip install` the hydrated
    project before running the tests. And we don't have a way to create a temporary
    virtual environment for the project.
    """

    required_files = [
        ".readthedocs.yml",
    ]
    all_found = True
    for file in required_files:
        if not (result.project_dir / file).is_file():
            all_found = False
            print("Required file not generated:", file)
    return all_found

    # sphinx_results = subprocess.run(
    #     ["make", "html"],
    #     cwd=(result.project_dir / "docs"),
    # )

    # return sphinx_results.returncode == 0


def github_workflows_are_valid(result):
    """Test to ensure that the GitHub workflows are valid"""
    workflows_results = subprocess.run(
        ["pre-commit", "run", "check-github-workflows"], cwd=result.project_dir, check=False
    )
    return workflows_results.returncode == 0


def initialize_git_project(result):
    """Initializes local git repository (required to run pre-commit)"""
    subprocess.call(["git", "init", "."], cwd=result.project_dir)


def test_all_defaults(copie):
    """Test that the default values are used when no arguments are given.
    Ensure that the project is created and that the basic files exist.
    """

    # run copier to hydrate a temporary project
    result = copie.copy()

    assert successfully_created_project(result)
    assert directory_structure_is_correct(result)
    assert not pylint_runs_successfully(result)
    assert contains_required_files(result)

    # check to see if the README file was hydrated with copier answers.
    found_line = False
    with open(result.project_dir / "README.md", encoding="utf-8") as f:
        for line in f:
            if "example_project" in line:
                found_line = True
                break
    assert found_line


def test_use_black_and_no_example_modules(copie):
    """We want to provide non-default arguments for the linter and example modules
    copier questions and ensure that the pyproject.toml file is created with Black
    and that no example modules are created.
    """

    # provide a dictionary of the non-default answers to use
    extra_answers = {
        "enforce_style": ["black", "pylint", "isort"],
        "create_example_module": False,
    }

    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers=extra_answers)

    assert successfully_created_project(result)
    assert directory_structure_is_correct(result)
    assert pylint_runs_successfully(result)
    assert contains_required_files(result)

    # make sure that the files that were not requested were not created
    assert not (result.project_dir / "src/example_package/example_module.py").is_file()

    # check to see if the pyproject.toml file has the expected dependencies
    found_line = False
    with open(result.project_dir / "pyproject.toml", encoding="utf-8") as f:
        for line in f:
            if '"black", # Used for static linting of files' in line:
                found_line = True
                break
    assert found_line

    assert black_runs_successfully(result)


@pytest.mark.parametrize(
    "enforce_style",
    [
        [],
        ["ruff_lint"],
        ["ruff_format"],
        ["ruff_lint", "pylint"],
        ["ruff_format", "black"],
        ["black", "pylint", "isort"],
        ["ruff_lint", "ruff_format"],
        ["black", "pylint", "isort", "ruff_lint", "ruff_format"],
    ],
)
def test_code_style_combinations(copie, enforce_style):
    """Test that various combinations of code style enforcement will
    still result in a valid project being created."""

    # provide a dictionary of the non-default answers to use
    extra_answers = {
        "enforce_style": enforce_style,
    }
    result = copie.copy(extra_answers=extra_answers)
    assert successfully_created_project(result)
    assert directory_structure_is_correct(result)
    assert contains_required_files(result)
    # black would still run successfully.
    assert black_runs_successfully(result)


@pytest.mark.parametrize(
    "notification",
    [
        [],
        ["slack"],
        ["email"],
        ["email", "slack"],
    ],
)
def test_smoke_test_notification(copie, notification):
    """Confirm we can generate a "smoke_test.yaml" file, with all
    notification mechanisms selected."""

    # provide a dictionary of the non-default answers to use
    extra_answers = {
        "failure_notification": notification,
    }

    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers=extra_answers)

    assert successfully_created_project(result)
    assert directory_structure_is_correct(result)
    assert black_runs_successfully(result)
    assert contains_required_files(result)


@pytest.mark.parametrize(
    "doc_answers",
    [
        {
            "include_docs": True,
            "include_notebooks": True,
        },
        {
            "include_docs": True,
            "include_notebooks": False,
        },
    ],
)
def test_doc_combinations(copie, doc_answers):
    """Confirm the docs directory is well-formed, when including docs."""

    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers=doc_answers)

    assert successfully_created_project(result)
    assert directory_structure_is_correct(result)
    assert black_runs_successfully(result)
    assert contains_required_files(result)
    assert docs_build_successfully(result)
    assert (result.project_dir / "docs").is_dir()


@pytest.mark.parametrize(
    "doc_answers",
    [
        {
            "include_docs": False,
            "include_notebooks": False,
        },
        {
            "include_docs": False,
            "include_notebooks": True,
        },
    ],
)
def test_doc_combinations_no_docs(copie, doc_answers):
    """Confirm there is no 'docs' directory, if not including docs."""

    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers=doc_answers)

    assert successfully_created_project(result)
    assert directory_structure_is_correct(result)
    assert black_runs_successfully(result)
    assert contains_required_files(result)
    assert not (result.project_dir / "docs").is_dir()


@pytest.mark.parametrize("test_lowest_version", ["none", "direct", "all"])
def test_test_lowest_version(copie, test_lowest_version):
    """Confirm we can generate a "testing_and_coverage.yaml" file, with all
    test_lowest_version mechanisms selected."""

    # provide a dictionary of the non-default answers to use
    extra_answers = {
        "test_lowest_version": test_lowest_version,
    }

    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers=extra_answers)

    assert successfully_created_project(result)
    assert directory_structure_is_correct(result)
    assert black_runs_successfully(result)
    assert contains_required_files(result)


def test_github_workflows_schema(copie):
    """Confirm the current GitHub workflows have valid schemas."""
    extra_answers = {
        "include_benchmarks": True,
        "include_docs": True,
    }
    result = copie.copy(extra_answers=extra_answers)
    initialize_git_project(result)
    assert github_workflows_are_valid(result)
    assert contains_required_files(result)
