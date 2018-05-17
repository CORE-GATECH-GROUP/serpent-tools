Please add the appropriate tag to the beginning of the title of your PR:

1. `[DOC]` if documentation related
1. `[DEP]` if something is deprecated or a deprecated feature is removed
1. `[ENH]` if a feature or enhancement
1. `[BUG]` if a bug fix
1. `[API]` if a (possibly incompatible) change to the API
1. `[TST]` if related to our test suite
1. `[STY]` if related to code cleanliness and pythonicness

For bug fixes and enhancements, link to the corresponding issue.

Make sure you have read over the developer guide to ease
the review process. These include:

- [ ] PR fits the [project scope](http://serpent-tools.readthedocs.io/en/latest/develop/contributing.html#project-scope)
- [ ] Code to be committed is [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) and matches the [code style](http://serpent-tools.readthedocs.io/en/latest/develop/codestyle.html#code-style) of the project
- [ ] New and/or changed features are [well documented](http://serpent-tools.readthedocs.io/en/latest/develop/documentation.html#documentation) and have adequate testing
- [ ] For first-time contributors, you have included your attribution in [`docs/contributors.rst`](https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/develop/docs/contributors.rst)

Include a thorough and concise overview of the changes, and why this PR is overall beneficial to the project.

Once the PR has been created and is nearing closure, make sure that serious changes, including deprecations and incompatible changes are documented in [the changelog](https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/develop/docs/changelog.rst)
