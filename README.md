<h1 align="center">
  <br><img src="project-logo.svg">
  <br>
  Release
  <br>
</h1>

<h4 align="center">iCalendar for Release dates.</h4>

<p align="center">
  <a href="https://badge.fury.io/gh/damoun%2Frelease">
    <img src="https://badge.fury.io/gh/damoun%2Frelease.svg"
         alt="Version">
  </a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/damoun/release.svg"></a>
  <a href="https://github.com/damoun/release/actions">
      <img src="https://github.com/damoun/release/actions/workflows/build.yml/badge.svg">
  </a>
  <a href="https://app.codacy.com/app/damoun-github/release">
    <img src="https://api.codacy.com/project/badge/Grade/010cedd6f7184f5f931c4ca64b0ae5f4">
</a>
</p>

<p align="center">
  <a href="#installing">Installing</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#contributing">Contributing</a> •
  <a href="CHANGELOG.md">Changelog</a>
</p>

## Installing

This Python project use [Pipenv][pipenv] for it's dependencies.

```sh
pipenv install --dev
pipenv run python -m release.cli --help
```

## Getting Started

Since I couldn't find an updated icalendar with Nintendo Switch games release dates, I wrote this project. It scrape release dates from Wikipedia and create ics files.
It's deployed using Github Actions on Github Pages.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

> or if you like it simple:

1. `Fork` this repository
2. Create a `branch`
3. `Commit` your changes
4. `Push` your `commits` to the `branch`
5. Submit a `pull request`

> You can find more information about Pull Requests [here][pull-request-help]

Check also the [list of contributors](AUTHOR.md#contributors) who helped on this project.

[pipenv]: https://pipenv.readthedocs.io/en/latest/
[pull-request-help]: https://help.github.com/categories/collaborating-on-projects-using-pull-requests/
