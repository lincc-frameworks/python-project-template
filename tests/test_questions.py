"""Test basic validation of questions and answers."""


def test_questions_default_answers(copie):
    """Create the project directory using copier"""
    # run copier to hydrate a temporary project
    result = copie.copy()
    assert result.exit_code == 0

    answer_dict = result.answers
    assert answer_dict["enforce_style"] != ""
    assert answer_dict["create_example_module"]


def test_questions_retrofit_answers(copie):
    """Create the project directory using copier"""
    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers={"custom_install": "retrofit"})
    assert result.exit_code == 0

    answer_dict = result.answers
    assert "enforce_style" not in answer_dict
    assert "create_example_module" not in answer_dict


def test_questions_invalid_project_name(copie):
    """Create the project directory using copier"""
    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers={"project_name": "this is bad"})
    assert result.exit_code != 0
    assert "Validation error for question 'project_name'" in str(result.exception)


def test_questions_ok_project_name(copie):
    """Create the project directory using copier"""
    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers={"project_name": "PhotoD"})
    assert result.exit_code == 0


def test_questions_invalid_package_name(copie):
    """Create the project directory using copier"""
    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers={"package_name": "this is bad"})
    assert result.exit_code != 0
    assert "Validation error for question 'package_name'" in str(result.exception)


def test_questions_ok_package_name(copie):
    """Create the project directory using copier"""
    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers={"package_name": "photoD"})
    assert result.exit_code == 0


def test_questions_invalid_project_organization(copie):
    """Create the project directory using copier"""
    # run copier to hydrate a temporary project
    result = copie.copy(extra_answers={"project_organization": "this is bad"})
    assert result.exit_code != 0
    assert "Validation error for question 'project_organization'" in str(result.exception)
