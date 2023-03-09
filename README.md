# python-project-template
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/lincc-frameworks/python-project-template)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/lincc-frameworks/python-project-template/ci.yml)
![Read the Docs](https://img.shields.io/readthedocs/lincc-ppt)

## What is this?

This project template codifies LINCC-Framework's best practices for python code organization, testing, documentation, and automation. It is meant to help new python projects get started quickly, letting the user focus on writing code. The template takes care of the minutia of directory structures, tool configurations, and automated testing until the user is ready to take over.

[Copier](https://copier.readthedocs.io/en/latest/) is required to use this template. Copier is an open source tool that hydrates projects from templates and natively supports updating projects as the original template matures. It's really neat!


# Getting started

## Prerequisites

These prerequisites for Copier are defined [here](https://copier.readthedocs.io/en/latest/#installation).
1) Python > 3.7
2) Git > 2.27
3) pipx (nice to have, conda and pip work too, but can be more difficult to reason about later)

```
>> python --version
Python 3.10.9

>> git --version
git version 2.34.1

>> which pipx
/usr/bin/pipx
```

## Install Copier

Given that you have all the prerequisites satisfied, go ahead and install Copier.
```
>> pipx install copier
```

## Create a new project from the template

Choose where you would like to create your new project, and call copier with the template.
```
>> copier gh:lincc-frameworks/python-project-template <path/to/destination>
```

After providing answers to the prompts, Copier will hydrate a project template and save it in the specified location. Additionally Copier will run `git init` in the new project directory to initialize it as a local repository.

## Create a new environment and install your new package

Create a new environment with your choice of environment tools (virtualenv, conda, etc.). Activate it, and change into the package directory.

Install the newly created python package. Use `pip` to install both the standard set of dependencies as well as the `[dev]` dependencies. (Note: depending on your system, you may not need the single quotes about '.[dev]')
```
>> pip install -e .
...
Lots of output
...

>> pip install '.[dev]'
...
Lots more output
...
```

## You _could_ stop here

At this point, your new project is hydrated and ready for you to start coding. But there's a lot more that this template has to offer. Keep reading to find out more about built in pre-commit hooks, GitHub CI, automatic documentation, and more.

## Commit your new project locally

:shushing-face:  If you're interested in using pre-commit hooks to crosscheck your code before you commit it, now is a good time to set that up (it's just one command) - check out ["Helpful pre-commit hooks"](https://github.com/lincc-frameworks/python-project-template#helpful-pre-commit-hooks).

Commit the project to your _local_ version control like so to see the pre-commit checks run.

```
>> git checkout -b initial_branch
Switched to a new branch 'initial_branch'
>> git add .
>> git commit -m 'Initial commit'
```

## Push your work to GitHub

Create a new repository in GitHub: ([GitHub How-to](https://docs.github.com/en/get-started/quickstart/create-a-repo))

```
>> git remote add origin https://github.com/<the_remote_project>/<the_remote_repository>
>> git push origin <local_branch_name>
```

Notice that when you create a PR in GitHub, a set of tests for Continuous Integration starts up to verify that the project can build successfully and that all the unit tests pass. Neato!

# Optional - but Awesome

## Helpful pre-commit hooks

`pre-commit` is installed when running `pip install '.[dev]'`. It's an industry standard tool that executes a set of tests prior to completing a `git commit` action. Using pre-commit enables a quick check of your code before it's committed and checked by GitHub workflows. This cuts down on code feedback time, and allows for faster development. Additional documentation can be found [here](https://pre-commit.com/index.html).

To configure pre-commit for your project, run the following command register pre-commit hooks with .git/hooks/pre-commit.

```
>> pre-commit install
```

## GitHub CI is ready out of the box

Notice that this template contains a `.github/workflows` directory with a `python-package.yml` file. Because of this, any project created from this template that uses GitHub as a repository will automatically have CI enabled.

GitHub workflows are extremely useful, for more information, check out the [About workflows](https://docs.github.com/en/actions/using-workflows/about-workflows) page.

## Unit test coverage

The GitHub workflow that runs when a new commit is pushed to a pull request, will automatically run unit tests and output code coverage into an xml file. To easily see if code coverage is changing as a result of new work, you should install the GitHub app, Codecov.

- Go to the Codecov app page - https://github.com/apps/codecov
- Click "Configure"
- Select your repository and follow the instructions

Future pull requests and commits will now include code coverage information. Neato!

## Automatic publishing to ReadTheDocs

If you have connected your GitHub account to [ReadTheDocs](https://readthedocs.org/) you should be able to automatically import the documentation from your project. To connect your GitHub account to ReadTheDocs, simply sign in to ReadTheDocs using your GitHub account.

On your dashboard, you'll see an "Import a Project" button that will take you to a list of repositories that can be [automatically imported](https://docs.readthedocs.io/en/stable/intro/import-guide.html#automatically-import-your-docs). If you don't see the repository you expect, it is possible that you do not have sufficient permissions configured in your GitHub organization. Talk to an administrator of the organization, and let them know what you're trying to do.

## Publishing to PyPI

A GitHub workflow is included that will automatically publish the packaged work to [PyPI](https://pypi.org/) when a new release is created. To support this, you'll need to configure your repository.

- Create and verify an account on PyPI - https://pypi.org/account/register/
- Create a PyPI API token - https://pypi.org/help/#apitoken
- Save the API token in your new repository following [these instructions](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-encrypted-secrets-for-your-repository-and-organization-for-github-codespaces#adding-secrets-for-a-repository). Save your secret API token with the name: PYPI_API_TOKEN

Now, when you [create a new release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) from your repository, a workflow will run that will package and deploy the code to PyPI.

## Keep your project up to date as the original template evolves

Once your project is under version control you'll be able to keep your project up to date by running `copier update`.

Copier will automatically check to see if a newer version of the original template is available and if so the changes will be automatically applied. Neato!

And of course, because your project is under version control, if you don't like the new changes, you can always revert back to the previous state. :grinning:

# Contributing to the Template

[![GitHub issue custom search in repo](https://img.shields.io/github/issues-search/lincc-frameworks/python-project-template?color=purple&label=Good%20first%20issues&query=is%3Aopen%20label%3A%22good%20first%20issue%22)](https://github.com/lincc-frameworks/python-project-template/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

## Find (or make) a new GitHub issue

Add yourself as the assignee on an existing issue so that we know who's working on what. ( If you're not actively working on an issue, unassign yourself :wink: ) 

If there isn't an issue for the work you want to do, please create one and include a description - it's just polite.

## Create a branch

It is preferable that you create a new branch with a name like `issue/##/<short-description>`. GitHub makes it pretty easy to associate branches and tickets, but it's nice when it's in the name.

## Testing the template

Testing can be tricky. The current best way is to clone this repository locally, and use Copier to generate a test project locally, then verify your expected results.

Copier will look for git tags to determine which version of the template to use. You probably don't want to create new tags while you're working on the template. Create a test project using the following command to let Copier know to use the latest local version. 
```
>> copier --vcs-ref HEAD </local/path/to/template> </test/project/directory>
```
Notes:
1) Any changes to the template will need to be committed (**not pushed**) to be picked up by Copier.
2) If there's an opportunity for introducing an automated test, please take it.
3) This project has some automated testing, to ensure that the template can hydrate a reasonable output project - feel free to extend that if it's reasonable.
4) See the [Copier documentation](https://copier.readthedocs.io/en/latest/generating/#regenerating-a-project) for more information.

## Create your PR

Please use PR best practices, and get someone to review your code.

## Optional - Release a new version

Once your PR is merged you should create a new release to make your changes available. GitHub's [instructions](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) for doing so are here. Use your best judgement when incrementing the version. i.e. is this a major, minor, or patch fix.
