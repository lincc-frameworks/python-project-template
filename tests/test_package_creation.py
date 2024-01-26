import pytest
import pytest_copie
import subprocess

def assert_successful_project_creation(result):
    """Basic assertions that indicate the copier was able to create a project"""
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()


def assert_directory_structure(result, package_name = "example_package"):
    """Test to ensure that the default directory structure ws created correctly"""
    assert (result.project_dir / f"src/{package_name}").is_dir()
    assert (result.project_dir / f"tests/{package_name}").is_dir()


def assert_black_runs_successfully(result):
    """Test to ensure that the black linter runs successfully on the project"""
    # run black with `--check` to look for lint errors, but don't fix them.
    black_results = subprocess.run(
        ["python", "-m", "black", "--check", (result.project_dir / "src")],
        cwd=result.project_dir
    )

    assert black_results.returncode == 0


def assert_pylint_runs_successfully(result):
    """Test to ensure that the pylint linter runs successfully on the project"""
    # run pylint to ensure that the hydrated files are linted correctly
    pylint_results = subprocess.run(
        ["python", "-m", "pylint",
         "--recursive=y",
         "--rcfile=./src/.pylintrc",
         (result.project_dir / "src")],
        cwd=result.project_dir
    )

    assert pylint_results.returncode == 0

def test_all_defaults(copie):
    """Test that the default values are used when no arguments are given.
    Ensure that the project is created and that the basic files exist.
    """

    # run copier to hydrate a temporary project
    result = copie.copy()

    assert_successful_project_creation(result)

    assert_directory_structure(result)

    assert_pylint_runs_successfully(result)

    # make sure that some basic files were created
    assert (result.project_dir / "README.md").is_file()
    assert (result.project_dir / "pyproject.toml").is_file()

    # check to see if the README file was hydrated with copier answers.
    found_line = False
    with open(result.project_dir / "README.md") as f:
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
        "preferred_linter": "black",
        "create_example_module": False,
    }

    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers=extra_answers)

    assert_successful_project_creation(result)

    assert_directory_structure(result)

    # make sure that the files that were not requested were not created
    assert not (result.project_dir / "src/example_package/example_module.py").is_file()

    # check to see if the pyproject.toml file has the expected dependencies
    found_line = False
    with open(result.project_dir / "pyproject.toml") as f:
       for line in f:
           if "\"black\", # Used for static linting of files" in line:
               found_line = True
               break
    assert found_line

    assert_black_runs_successfully(result)
