# RAIL Python Project Template
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/LSSTDESC/RAIL-project-template/ci.yml)
[![Forked](https://img.shields.io/badge/Forked-LINCC%20Frameworks%20Python%20Project%20Template-brightgreen)](https://github.com/LINCC-Frameworks/python-project-template)

This project borrows from the LINCC Frameworks' template of best practices for
python code organization, testing, and automation. It is meant to help new RAIL
projects use the same standards, and be interoperable with other packages in
the RAIL-iverse.

Notable differences from the original template include:

- support for namespaced packages
- remove sphinx documentation generation
- keep pylint configuration in the pyproject.toml (instead of creating
pylint.rc files)

[Copier](https://copier.readthedocs.io/en/latest/) is required to use this
template. Copier is an open source tool that hydrates projects from templates 
and natively supports updating projects as the original template matures.

Our template works best with Copier v8.0 and above. 

## Getting started

Choose where you would like to create your new project, and call copier with the template.

```
>$ copier copy gh:LSSTDESC/RAIL-project-template <path/to/destination>
<Answer the questions>
>$ git init
>$ pip install -e .[dev]
```

## Configuring your repository

After you've created a project with this template and pushed it to GitHub, a small
amount of additional set up in the repository will allow you to take full advantage
of the features that the template offers.

### Enable Codecov reporting

The Continuous Integration tests built into the template will automatically generate
the code coverage files that Codecov needs for reporting. All you need to do is
enable Codecov for your repository.

Go here: https://github.com/apps/codecov and configure it for your repository

### Publish to PyPI automatically

A GitHub action has been created that will automatically publish a package to PyPI.
To make use of that, you'll need to create an API key and save it your new repo.
Follow these instructions to get started: https://lincc-ppt.readthedocs.io/en/latest/practices/pypi.html#set-up

### Automatically Add issues to the Project Tracker

To easily track issues across many repositories, we can make use of GitHub's projects.
A GitHub action is included in template that will automatically add new issues to
the primary RAIL project tracker, however, you'll need to setup a Person Access Token
and save it as repository secret for it to work. 

These instructions explain how to create a Personal Access Token: https://github.com/actions/add-to-project#creating-a-pat-and-adding-it-to-your-repository

Once your token is created save it as a **repository secret** with the name: ``ADD_TO_PROJECT_PAT``.

### Utilize pre-commit hooks

Pre-commit runs various tests against your code.
These checks are mostly the same as those that are run in continuous integration,
but by running them locally it's possible to reduce the amount of time between committing
and finding errors in the code.

It is not required to use pre-commit if you use this template, but it is available
if you would like. To enable it, simply run ``pre-commit install``.

## Contributing to the Template

### WARNING:

When creating a pull request in this fork, make sure to set the
`base repository` to `LSSTDESC/RAIL-project-template` (it will 
default to the upstream of `lincc-frameworks:main`).

[![GitHub issue custom search in repo](https://img.shields.io/github/issues-search/LSSTDESC/RAIL-project-template?color=purple&label=Good%20first%20issues&query=is%3Aopen%20label%3A%22good%20first%20issue%22)](https://github.com/LSSTDESC/RAIL-project-template/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

See full documentation at LINCC's [readthedocs](https://lincc-ppt.readthedocs.io/en/latest/source/contributing.html)
