# RAIL Python Project Template
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/LSSTDESC/RAIL-project-template/ci.yml)

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
```

## Contributing to the Template

### WARNING:

When creating a pull request in this fork, make sure to set the
`base repository` to `LSSTDESC/RAIL-project-template` (it will 
default to the upstream of `lincc-frameworks:main`).

[![GitHub issue custom search in repo](https://img.shields.io/github/issues-search/LSSTDESC/RAIL-project-template?color=purple&label=Good%20first%20issues&query=is%3Aopen%20label%3A%22good%20first%20issue%22)](https://github.com/LSSTDESC/RAIL-project-template/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

See full documentation at LINCC's [readthedocs](https://lincc-ppt.readthedocs.io/en/latest/source/contributing.html)