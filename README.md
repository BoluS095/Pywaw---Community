# PyWaw — Warsaw Python User Group

[![Documentation checks](https://github.com/BoluS095/Pywaw---Community/actions/workflows/docs-check.yml/badge.svg)](https://github.com/BoluS095/Pywaw---Community/actions/workflows/docs-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Community resources and reusable materials for the Warsaw Python community.

This repository is a public resource collection for people who organize, speak at, or participate in Python meetups. It is intended to make community knowledge easier to reuse and improve.

## Repository contents

- [Speaker guide](speaker-guide.md) — practical guidance for current and first-time speakers
- [Meetup template](meetup-template.md) — a reusable structure for planning community events
- [Learning path](learning-path.md) — a starting route for people learning Python
- [Code of conduct](code-of-conduct.md) — shared expectations for a welcoming community
- [Contributing guide](CONTRIBUTING.md) — how to propose and review improvements

## Quality checks

The repository runs a lightweight GitHub Actions check on pull requests and pushes to `main`. It validates relative links in Markdown documentation using Python's standard library.

Run the same check locally:

```bash
python scripts/check_markdown_links.py
```

## About PyWaw

PyWaw is a Warsaw-based Python user group. Public information about the community and its activities is available at [pywaw.org](https://pywaw.org).

The repository is a community resource, not an official event archive or a complete record of PyWaw activity. Membership and event totals are intentionally omitted unless they can be linked to a current, authoritative source.

## Community involvement

Rafał Korzeniowski is listed publicly as a PyWaw co-organizer. See the [PyWaw speaker and community contributors page](https://pywaw.org/prelegenci/).

For broader Python community context, see [Python Summit](https://pythonsummit.org/).

## How to contribute

Contributions that make these resources more useful are welcome. Please read the [contributing guide](CONTRIBUTING.md) before opening an issue or pull request.

## License

This repository is distributed under the MIT License. See [LICENSE](LICENSE).
