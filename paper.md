---
title: 'A Python Project Template for Healthy Scientific Software'
tags:
  - Python
  - template
authors:
  - name: Drew Oldag
    orcid: 0000-0001-6984-8411
    equal-contrib: true
    affiliation: "1, 2"
  - name: Melissa DeLucchi
    orcid: 0000-0002-1074-2900
    equal-contrib: true
    affiliation: "1, 3"
  - name: Wilson Beebe
    orcid: asdfasdf
    affiliation: "1, 2"
  - name: Doug Branton
    orcid: 0009-0009-7822-7110
    affiliation: "1, 2"
  - name: Sandro Campos
    orcid: 0009-0007-9870-9032
    affiliation: "1, 3"
  - name: Carl Christofferson
    orcid: asdfasdf
    affiliation: "1, 2"
  - name: Andrew Connolly <-----------????
    orcid: asdfasdf
    affiliation: "1, 2"
  - name: Jeremy Kubica
    orcid: 0009-0009-2281-7031
    affiliation: "1, 3"
  - name: Olivia Lynn
    orcid: 0000-0001-5028-146X
    affiliation: "1, 3"
  - name: Konstantin Malanchev
    orcid: 0000-0001-7179-7406
    affiliation: "1, 3"
  - name: Alex Malz <----------????
    orcid: 0000-0002-8676-1622
    affiliation: "1, 3"
  - name: Sean McGuire
    orcid: asdfasdf
    affiliation: "1, 3"
  - name: Chris Wenneman
    orcid: asdfasdf
    affiliation: "1, 2"
affiliations:
  - name: LINCC-Frameworks
    index: 1
  - name: DiRAC Institute and the Department of Astronomy, University of Washington, 3910 15th Ave NE, Seattle, WA 98195, USA
    index: 2
  - name: McWilliams Center for Cosmology, Department of Physics, Carnegie Mellon University, Pittsburgh, PA 15213, USA
    index: 3
date: 28 February 2024
bibliography: paper.bib
---

# Summary

The creation of healthy code is vital for its successful long term use in scientific research. To maximize impact throughout the community, software packages must be accurate, usable, and maintainable. Here we discuss several engineering processes that are important for developing healthy software. Unfortunately these processes often require configuration leading to short-term overhead for new projects. We introduce the LINCC-Frameworks Python Project Template, a configurable template designed for scientific software projects that greatly simplifies adopting such practices by automating the setup and configuration of important code health tools.

# Statement of need

Software has long played a vital role in analyzing scientific data and driving new discoveries. As the scientific community continues to build upon established projects and create novel algorithms, there is a need to ensure the accuracy, repeatability, usability, and maintainability of the software. The first factor is required for the validity of the scientific results, while the latter factors enable the software to have a broad, sustained impact.

The LINCC-Frameworks Python Project Template (LF-PPT) was originally created with the needs of astronomers in mind, however, it became apparent that it is broadly applicable for many scientific use cases. The LF-PPT codifies our best engineering practices because we were unable to find existing tooling that met our needs. Many other templates exist for specific applications that include non-trivial amounts of code, but we wanted a template that 1) is agnostic to specific applications 2) includes tooling needed for healthy software 3) doesn’t preclude use of other application-specific templates and 4) is updatable as best practices and tooling evolve. 


# Code health processes

There exists a wide variety of literature on best practices for developing healthy code (see for example [@martin2008] or [@perkel2022]). In this section we discuss several such practices that benefit from the existence of automated tooling. This list is not meant to be exhaustive, but each item should be considered important for developing a trustworthy and impactful software package.

## Automated testing

Automated testing is critical to ensuring the correctness of code during initial implementation and through ongoing changes. Code should be validated by a comprehensive suite of tests including unit tests, which confirm the accuracy of individual functions, and integration tests that ensure end-to-end functionality for supported use cases. A comprehensive and automated test suite is an indicator of a trustworthy software package.

The LF-PPT supports automated testing by configuring several different continuous integration GitHub workflows, that run test suites automatically:
 - at each push or pull request to ensure that changes to the current branch do not break the program’s behavior and
 - in regularly scheduled smoke tests (usually daily) to ensure that the code has not broken due to a change of the project’s code or the behavior of its dependencies.

## Documentation

Thorough documentation of code allows others to use the package more readily and encourages maintainability. The LF-PPT supports the use of sphinx[^1] for integration with ReadTheDocs[^2] to automatically render Python docstrings into well formatted documentation alongside manually written documentation. Additionally, to demonstrate the use of the package in context, the LF-PPT provides automatic rendering of example Jupyter notebooks within the documentation.

## Distribution

Software is only useful to the broader community if other users can find, install, and update it. Package management systems such as pip[^3] or conda[^4] provide simple tools for a user to download a new software package and its dependencies from public repositories such as PyPI[^7] or conda-forge[^8]. To enable easy code installation with pip or conda the LF-PPT provides support for automatic distribution through both PyPI and conda-forge when the user applies a new git tag via the GitHub UI.

## Additional code health tools

The LF-PPT supports many more features than those listed here including static code analysis, performance benchmarking, code testing coverage and more. For a complete list, please see the documentation at http://lincc-ppt.readthedocs.io/. 

The most notable exclusion from the LF-PPT is code. Aside from a few optional stub source and test files, the LF-PPT allows the user focus on scientific code, while supporting them with the industry best practices in maintainable software engineering.  

# Usage

## General usage

The LINCC-Frameworks Python Project Template automates the setup of the above processes for Python projects hosted on GitHub. The only direct dependency is copier[^5] [@copier], which is used as the engine to generate new projects from the LF-PPT with a specific directory structure, the requested configuration and stub files. To hydrate a new or existing project with the LF-PPT via copier the user calls:

> copier copy gh:lincc-frameworks/python-project-template <new/project/directory>

A questionnaire is presented to configure the project and establish the various features of the template to include. After the directory structure and files have been generated, the user should run the included initialization script to configure the local git repository and install the new package in the virtual environment:

> cd <new/project/directory>
> bash .initialize-new-project.sh

The process is designed so as not to require significant time, and, thus, if the user is unhappy with the generated project, they can simply delete and recreate it. Depending on the options selected, some additional configuration may be required, such as registering with ReadTheDocs or PyPI. To assist the user, a customized, post-creation checklist is generated.

## Existing projects

In addition to creating new projects from scratch, the LF-PPT can be applied to existing projects to incorporate the features it provides. Often a more established project will require more effort to apply the LF-PPT. However, LINCC-Frameworks has had success applying the template to multiple legacy projects. A collection of tips for applying the template to existing projects is included in the documentation http://lincc-ppt.readthedocs.io/.

## Updating projects

As best practices evolve and new tools are introduced, the LF-PPT will incorporate those into the template. Updates to the template can be applied to existing projects with minimal effort, allowing the users to focus on science and not software maintenance.

> copier update

## Hibernating projects

Scientific projects often go into periods of hibernation when not under active development or use, and are often challenging to revive. With the LF-PPT, hibernating projects should be much easier to reactivate. Automatically scheduled smoke tests and dependabot[^6] integration ensure that the code and dependencies continue to function correctly without significant interaction from the maintainers.

## Recent applications

The LF-PPT has been applied to multiple LINCC Frameworks projects including LSDB[^11], Hipscat[^12], and TAPE[^13], short term collaborations such as Sorcha[^14], SuperPhot+[^10], DeepDISC[^15], and MacCauff[^9], and external project including kcorrect[^16] and FlexCode[^17] Additionally a project specific version was forked from the project and has been applied to all RAIL packages[^18].

# Acknowledgments

This project is supported by Schmidt Sciences.

[^1]: https://www.sphinx-doc.org/
[^2]: https://about.readthedocs.com/
[^3]: https://pip.pypa.io/en/latest/
[^4]: https://docs.conda.io/en/latest/
[^5]: https://copier.readthedocs.io/en/stable/ 
[^6]: https://docs.github.com/en/code-security/dependabot 
[^7]: https://pypi.org/
[^8]: https://conda-forge.org/docs/
[^9]: https://github.com/macauff/macauff
[^10]: https://github.com/VTDA-Group/superphot-plus
[^11]: https://github.com/astronomy-commons/lsdb
[^12]: https://github.com/astronomy-commons/hipscat
[^13]: https://github.com/lincc-frameworks/tape
[^14]: https://github.com/dirac-institute/sorcha
[^15]: https://github.com/lincc-frameworks/deepdisc
[^16]: https://github.com/blanton144/kcorrect
[^17]: https://github.com/lee-group-cmu/FlexCode
[^18]: https://github.com/LSSTDESC/RAIL-project-template
