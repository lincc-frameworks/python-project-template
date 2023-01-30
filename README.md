# python-project-template

## What is this?

This template codifies LINCC-Framework's best practices for python code organization, testing, documentation, and automation.

## How to use this Copier template:

1) Install Python 3.7 or newer. (Check with `python --version`)
2) Install Git 2.27 or new. (Check with `git --version`)
3) Install `copier` like so: `pipx install copier`. (`pip` works fine too, but `pipx` is what the cool kids use)
4) Create a new project using this template like so: `copier gh:lincc-frameworks/python-project-template <path/to/destination>`
5) Provide answers to the prompts
6) Enjoy pure, uncut euphoria.

## Post-euphoria - Install your new package

Ok, ok, calm down. I know, it's really great. 
You should go ahead and install your new project using these instructions:
1) Create a new environment with your choice of environment managers (conda, virtualenv, etc.)
2) Install the base dependencies: `pip install .`
3) Install the extra developer dependencies: `pip install '.[dev]'` (Note - the single quotes around '.[dev]' may not be required for your system.)

## Version control and keeping your project up to date

### Setup version control for your newly created project

To appreciate the full power of Copier, push your newly created project into a github repository. There are lots of ways to do this, and but every environment is a snowflake.
Fortunately, there are several how-to's available. Roughly speaking, the sequence of commands is:
1) Run `git init`[^1] in your newly created project
2) Run `git add .` to add all your new files and directories.
3) Run `git commit` with a nice message.
4) Create a new remote repository ([GitHub How-to](https://docs.github.com/en/get-started/quickstart/create-a-repo))
5) Run `git remote ad origin https://github.com/<the_remote_project>/<the_remote_repository>`
6) Run `git push origin <local_branch_name>`

[^1]: If you haven't already, you can run `git config --global init.defaultBranch <name>` so that your default branch name isn't `master`.

### Keep your project up to date with changes to the original template.

Once the project is under version control you'll be able to keep your project up to date by running `copier update`. 
Copier will automatically check to see if a newer version of the original template is available and if so the changes will then be automatically applied to your project. Neato!

And of course, because your project is under version control, if you don't like the new changes, you can always revert back to the previous state. :)

## Other neat peices that come for free

### GitHub CI is ready out of the box

Notice that this template contains a `.github/workflows` directory with a `python-package.yml` file. So any project created from this template that uses github as a repository will automatically have CI enabled. GitHub workflows are extremely useful, for more information, check out the [About workflows](https://docs.github.com/en/actions/using-workflows/about-workflows) page.

### Pre-commit is part of it too

Once you have created a new project from the template, and start coding, you can save yourself from the embarassment of say, not including a blank line at the end of your .py file, by using pre-commit checks.
After you have successfully run `pip install '.[dev]'` as part of the "Post-euphoria - Install your new package" step, run `pre-commit install`.
This will register all the pre-commit git hooks defined in .pre-commit-config.yaml with git so that they are run before a `git commit` is completed.

This functionality relies on a the third-party tool, [pre-commit](https://pre-commit.com/). It's a very useful tool when paired with Github workflows. Since the workflows will typically prevent code merging if certain tests fail, by using pre-commit, the user can verify that their code will pass all the workflow checks prior to completing a git commit.

# Developement of the template

## Making updates to the template

Feel free to make updates to this template. Once you've tested the updates you should create a new release to make them available. GitHub's [instructions](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) for doing so are here. Use your best judgement when incrementing the version.

## Testing the template

Testing can be tricky. The current best way is to clone this repository locally, and generate test projects locally, and verify your expected results. To be clear though, if there's an opportunity for automated tests, please take advantage of it.