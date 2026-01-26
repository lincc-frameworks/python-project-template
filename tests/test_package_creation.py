"""Verify package creation using `pytest-copie`"""

import os
import subprocess

import pytest

os.environ["SKIP"] = "no-commit-to-branch"


def create_project_with_basic_checks(copie, extra_answers, package_name="example_package"):
    """Create the project using copier. Perform a handful of basic checks on the created directory."""
    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers=extra_answers)

    ## Initializes local git repository (required to run pre-commit)
    subprocess.call(["git", "init", "."], cwd=result.project_dir)

    # successfully_created_project
    assert (
        result.exit_code == 0 and result.exception is None and result.project_dir.is_dir()
    ), "Did not successfully create project"

    # install the `example_package` into the existing python environment.
    build_results = subprocess.run(
        ["python", "-m", "pip", "install", "--no-deps", "."], cwd=result.project_dir, check=False
    )
    assert build_results.returncode == 0

    # directory_structure_is_correct
    assert (result.project_dir / f"src/{package_name}").is_dir() and (
        result.project_dir / f"tests/{package_name}"
    ).is_dir(), "Directory structure is incorrect"

    # contains_required_files
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
    assert all_found

    ## Initialize local git repository and add ALL new files to it.
    git_results = subprocess.run(["git", "init", "."], cwd=result.project_dir, check=False)
    assert git_results.returncode == 0
    git_results = subprocess.run(["git", "add", "."], cwd=result.project_dir, check=False)
    assert git_results.returncode == 0

    ## This will run ALL of the relevant pre-commits (excludes only "no-commit-to-branch,check-added-large-files")
    precommit_results = subprocess.run(["pre-commit", "run", "-a"], cwd=result.project_dir, check=False)
    assert precommit_results.returncode == 0

    return result


def test_all_defaults(copie, default_answers):
    """Test that the default values are used when no arguments are given.
    Ensure that the project is created and that the basic files exist.
    """
    result = create_project_with_basic_checks(copie, default_answers)

    # uses ruff instead of (black/isort/pylint)
    assert not (result.project_dir / "src/.pylintrc").is_file()
    assert not (result.project_dir / "tests/.pylintrc").is_file()

    # check to see if the README file was hydrated with copier answers.
    found_line = False
    with open(result.project_dir / "README.md", encoding="utf-8") as f:
        for line in f:
            if "example_project" in line:
                found_line = True
                break
    assert found_line


def test_use_black_and_no_example_modules(copie, default_answers):
    """We want to provide non-default arguments for the linter and example modules
    copier questions and ensure that the pyproject.toml file is created with Black
    and that no example modules are created.
    """
    extra_answers = default_answers | {
        "enforce_style": ["black", "pylint", "isort"],
        "create_example_module": False,
    }
    result = create_project_with_basic_checks(copie, extra_answers)

    assert (result.project_dir / "src/.pylintrc").is_file()
    assert (result.project_dir / "tests/.pylintrc").is_file()

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
def test_code_style_combinations(copie, enforce_style, default_answers):
    """Test that various combinations of code style enforcement will
    still result in a valid project being created."""
    extra_answers = default_answers | {
        "enforce_style": enforce_style,
    }
    create_project_with_basic_checks(copie, extra_answers)


@pytest.mark.parametrize(
    "notification",
    [
        [],
        ["slack"],
        ["email"],
        ["email", "slack"],
    ],
)
def test_smoke_test_notification(copie, notification, default_answers):
    """Confirm we can generate a "smoke_test.yaml" file, with all
    notification mechanisms selected."""
    extra_answers = default_answers | {
        "failure_notification": notification,
    }

    create_project_with_basic_checks(copie, extra_answers)


@pytest.mark.parametrize(
    "license_option",
    [
        [],
        ["MIT"],
        ["BSD"],
        ["GPL3"],
        ["none"],
    ],
)
def test_license(copie, license_option, default_answers):
    """Confirm we get a valid project for different license options."""
    extra_answers = default_answers | {"license": license_option}

    create_project_with_basic_checks(copie, extra_answers)


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
def test_doc_combinations(copie, doc_answers, default_answers):
    """Confirm the docs directory is well-formed, when including docs."""
    extra_answers = default_answers | doc_answers
    result = create_project_with_basic_checks(copie, extra_answers)

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
def test_doc_combinations_no_docs(copie, doc_answers, default_answers):
    """Confirm there is no 'docs' directory, if not including docs."""
    extra_answers = default_answers | doc_answers

    result = create_project_with_basic_checks(copie, extra_answers)

    assert not (result.project_dir / "docs").is_dir()


@pytest.mark.parametrize("test_lowest_version", ["none", "direct", "all"])
def test_test_lowest_version(copie, test_lowest_version, default_answers):
    """Confirm we can generate a "testing_and_coverage.yaml" file, with all
    test_lowest_version mechanisms selected."""
    extra_answers = default_answers | {
        "test_lowest_version": test_lowest_version,
    }

    create_project_with_basic_checks(copie, extra_answers)


def test_github_workflows_schema(copie, default_answers):
    """Confirm the current GitHub workflows have valid schemas."""
    extra_answers = default_answers | {
        "include_benchmarks": True,
        "include_docs": True,
    }
    create_project_with_basic_checks(copie, extra_answers)
