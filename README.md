![Banner Image for LINCC Frameworks Python Project Template](https://github.com/user-attachments/assets/8977125e-b4c7-4f12-8f63-f3feb70a3ac6)
# LINCC Frameworks Python Project Template

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/lincc-frameworks/python-project-template)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/lincc-frameworks/python-project-template/ci.yml)](https://github.com/lincc-frameworks/python-project-template/ci.yml)
[![Read the Docs](https://img.shields.io/readthedocs/lincc-ppt)](https://lincc-ppt.readthedocs.io/)

[![DOI:10.3847/2515-5172/ad4da1](https://zenodo.org/badge/DOI/10.3847/2515-5172/ad4da1.svg)](https://ui.adsabs.harvard.edu/abs/2024RNAAS...8..141O)

This project template codifies LINCC-Framework's best practices for python code organization, testing, documentation, and automation. It is meant to help new python projects get started quickly, letting the user focus on writing code. The template takes care of the minutia of directory structures, tool configurations, and automated testing until the user is ready to take over. You can read more in the [PPT research note](https://iopscience.iop.org/article/10.3847/2515-5172/ad4da1).

[Copier](https://copier.readthedocs.io/en/latest/) is required to use this template. Copier is an open source tool that hydrates projects from templates and natively supports updating projects as the original template matures. It's really neat!

Our template works best with Copier v9.1 and above. 
For all the information, see the detailed user guide in
[readthedocs](https://lincc-ppt.readthedocs.io/)

## Getting started

Choose where you would like to create your new project, and call copier with the template.

```sh
copier copy gh:lincc-frameworks/python-project-template <path/to/destination>
cd <path/to/destination>
# Create a virtual environment, feel free to use conda, pyenv or your favorite tool
python3 -mvenv ~/.virtualenvs/<env_name>
source ~/.virtualenvs/<env_name>/bin/activate
bash .initialize_new_project.sh
```

## Contributing to the Template

[![GitHub issue custom search in repo](https://img.shields.io/github/issues-search/lincc-frameworks/python-project-template?color=purple&label=Good%20first%20issues&query=is%3Aopen%20label%3A%22good%20first%20issue%22)](https://github.com/lincc-frameworks/python-project-template/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

See full documentation at [readthedocs](https://lincc-ppt.readthedocs.io/en/latest/source/contributing.html)

## Citation

If you use Python Project Template in your work, we ask the you cite the ["A Python Project Template for Healthy Scientific Software" research note](https://iopscience.iop.org/article/10.3847/2515-5172/ad4da1) [full citation](./CITATION.bib):


## Acknowledgements

This project is supported by Schmidt Sciences.
