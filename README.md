# PyWaw Community Resources (Independent Project)

[![Documentation checks](https://github.com/BoluS095/Pywaw---Community/actions/workflows/docs-check.yml/badge.svg)](https://github.com/BoluS095/Pywaw---Community/actions/workflows/docs-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An independently maintained collection of reusable resources for Python meetups, speakers, organizers, and learners.

**Affiliation notice:** This repository is not an official PyWaw repository and is not affiliated with or endorsed by the PyWaw organization. The repository name describes its subject matter only. Please refer to the official community website for authoritative information about PyWaw and its activities: https://pywaw.org.

## Repository contents

- [Speaker guide](speaker-guide.md) — practical guidance for first-time and returning speakers
- [Meetup template](meetup-template.md) — a reusable structure for planning community events
- [Learning path](learning-path.md) — a starting route for people learning Python
- [Code of conduct](code-of-conduct.md) — suggested expectations for a welcoming learning environment
- [Contributing guide](CONTRIBUTING.md) — how to propose and review improvements

These materials are independent resources. They should not be treated as official PyWaw policies, event records, membership data, or statements on behalf of any organization.

## Quality checks

The repository runs a lightweight GitHub Actions check on pull requests and pushes to `main`. It validates relative links in Markdown documentation using Python's standard library.

Run the same check locally:

```bash
python scripts/check_markdown_links.py
```

## How to contribute

Contributions that make these independent learning and meetup resources more useful are welcome. Please read the [contributing guide](CONTRIBUTING.md) before opening an issue or pull request.

## License

This repository is distributed under the MIT License. See [LICENSE](LICENSE).
