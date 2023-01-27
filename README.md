## How to use this Copier template:

1) Install Python 3.7 or newer. (Check with `python --version`)
2) Install Git 2.27 or new. (Check with `git --version`)
3) Install `copier` like so: `pipx install copier`. (`pip` works fine too, but `pipx` is what the cool kids use)
4) Create a new project using this template like so: `copier gh:lincc-frameworks/python-project-template <path/to/destination>`
5) Provide answers to the prompts
6) Enjoy pure, uncut euphoria.

## Post-euphoria
Ok, ok, calm down. I know, it's really great. 
You should go ahead and `pip install` your new project, just to make sure that you have all the dependencies.
1) Create a new environment with your choice of environment managers (conda, virtualenv, etc.).
2) Install the base dependencies: `pip install .`
3) Install the extra developer dependencies: `pip install '.[dev]'` (Note - the single quotes around '.[dev]' may not be required for your system.)

## Keep your project up to date
To appreciate the full power of Copier, push your newly created project into a github repository.
Once the project is under version control you'll be able to keep your project up to date with: `copier update`.

If a newer version of this template has been released the changes will then be automatically applied to your project. Neato!

## CI is part of it
Notice that this template contains a `.github/workflows` directory with a `python-package.yml` file. So any project created from this template that uses github as a repository will automatically have CI enabled.

## Pre-commit is part of it too
Once you have run `pip install '.[dev]'`, the next thing you should do is run `pre-commit install`.
This will register all the pre-commit git hooks defined in .pre-commit-config.yaml with git so that
they are run before a `git commit` is completed.
