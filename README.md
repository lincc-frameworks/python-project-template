# python-project-template

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

After providing answers to the prompts, Copier will hydrate a project template and save it in the specified location.

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

## Register pre-commit hooks

The tool `pre-commit` is an industry standard that will execute a set of tests prior to completing a git commit action. For instance, pre-commit can run unit tests to verify code coverage or linters to ensure adherence to style guides. Pre-commit documentation can be found [here](https://pre-commit.com/index.html).

```
>> pre-commit install
```

## Add local version control to your project

The process of setting up _local_ version control will look something like this:

```
>> git init[^1]
Initialized empty Git repository in /path/to/destination/.git/
>> git checkout -b initial_branch
Switched to a new branch 'initial_branch'
>> git add .
>> git commit -m 'Initial commit'
```

[^1]: If you haven't already, you can run `git config --global init.defaultBranch <name>` so that your default branch name isn't `master`.

## Extra Credit - Push your work to GitHub

Create a new repository in GitHub: ([GitHub How-to](https://docs.github.com/en/get-started/quickstart/create-a-repo))

```
>> git remote add origin https://github.com/<the_remote_project>/<the_remote_repository>
>> git push origin <local_branch_name>
```

Notice that when you create a PR in GitHub, a set of tests for Continuous Integration starts up to verify that the project can build successfully and that all the unit tests pass. Neato!


# Some nifty things you get for free

## Keep your project up to date as the original template evolves

Once your project is under version control you'll be able to keep your project up to date by running `copier update`.

Copier will automatically check to see if a newer version of the original template is available and if so the changes will be automatically applied. Neato!

And of course, because your project is under version control, if you don't like the new changes, you can always revert back to the previous state. :)

## GitHub CI is ready out of the box

Notice that this template contains a `.github/workflows` directory with a `python-package.yml` file. Because of this, any project created from this template that uses GitHub as a repository will automatically have CI enabled.

GitHub workflows are extremely useful, for more information, check out the [About workflows](https://docs.github.com/en/actions/using-workflows/about-workflows) page.

## Pre-commit is part of it too

No one wants the embarrassment of committing a .py file without a trailing blank line :scream: You'll immediately have access to [pre-commit](https://pre-commit.com/), an industry standard third-party tool.

Using pre-commit before GitHub workflows start allows you to do a quick check of your code before it's committed. This cuts down on code feedback time, and allows for faster development.

# Contributing to the Template

## Find (or make) a new GitHub issue

Add yourself as the assignee on an existing issue so that we know who's working on what. ( If you're not actively working on an issue, unassign yourself :wink: ) 

If there isn't an issue for the work you want to do, please create one and include a description - it's just polite.

## Create a branch

It is preferable that you create a new branch with a name like `issue/##/<short-description>`. GitHub makes it pretty easy to associate branches and tickets, but it's just easier when it's in the name.

## Testing the template

Testing can be tricky. The current best way is to clone this repository locally, and use Copier to generate a test project locally, then verify your expected results.

Copier will look for git tags to determine which version of the template to use. You probably don't want to create new tags while you're working template. Create test project using this signature to let Copier know to use the latest local version. See the [Copier documentation](https://copier.readthedocs.io/en/latest/generating/#regenerating-a-project) for more information.

```
>> copier --vcs-ref HEAD </local/path/to/template> </test/project/directory>
```
Notes:
1) Any changes to the template will need to be committed (**not pushed**) to be picked up by Copier.
2) If there's an opportunity for introducing an automated test, please take it.

## Create your PR

To be able to move quickly, there aren't many guardrails right now to prevent merging bad code. This will change as the project becomes more mature. For now, please use PR best practices, and get someone to review your code.

## Optional - Release a new version

Once you've tested the updates you should create a new release to make them available. GitHub's [instructions](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) for doing so are here. Use your best judgement when incrementing the version. i.e. is this a major, minor, or 
