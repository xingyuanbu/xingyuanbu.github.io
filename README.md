# Xingyuan Bu’s academic homepage

A responsive, static academic homepage for <https://xingyuanbu.github.io/>. It runs on GitHub Pages without a theme, Ruby, JavaScript packages, or a build step. All typography, icons, styles, and scripts are served locally; no tracking scripts or external font requests are included.

## Preview

From this directory, run:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open <http://127.0.0.1:8765/>. The `index.html` file also opens directly in a browser, including publication filtering.

## Update content

- Biography, experience, education, service, talks, and awards: edit `index.html`.
- Publications: edit `data/publications.json`, then run `python3 scripts/update_publications.py`.
- Each publication stores its title, venue, year, research area (`language` or `vision`), and `selected` flag. Optional fields are `authors`, `paper`, `code`, `scholar`, and `note`.
- Styling: `assets/style.css`. Interactive filtering and navigation: `assets/main.js`.
- Citation statistics and their snapshot date appear in the profile sidebar in `index.html`; these are intentionally dated, rather than presented as live statistics.
- The complete publication list is embedded in the page, so it remains readable and indexable without JavaScript. Search and topic filters query all papers.

## Sources and editorial choices

Updated in November 2026 from the owner’s supplied `zh/10.2en_niv.tex`, the saved Google Scholar profile in `EOI_20261024`, and the previous homepage. The original homepage text is preserved verbatim in `docs/previous-homepage.md`; original image resources are retained.

- The CV takes precedence for current affiliation, roles, publication venues, and conference years. Scholar sometimes uses the preprint year; the page uses the conference year from the CV.
- The saved Scholar profile supplies author lists, citation-record links, and the October 2026 statistics: 2,275 citations, h-index 21, i10-index 26. Abbreviated author lists and ellipses are preserved; `X Bu` is expanded to Xingyuan Bu. Contribution markers are retained where the supplied author lists specify them.
- The ConceptMath venue is shown as Findings of ACL 2024, as specified in the saved Scholar profile.
- VideoLVR appears in the CV but has no record in the supplied Scholar snapshot. Its title and preprint status are included, with no invented author list or paper URL.
- Repeated qualification bullets in the CV were consolidated. The CV’s older “6 years of experience” wording was omitted in favor of dated roles. Commercial revenue figures are not reproduced on the homepage.
- Verified paper/code URLs from the previous homepage are retained; arXiv IDs explicitly included in the Scholar snapshot are linked directly. Other entries link to their supplied Scholar record. No additional network research is required to maintain this version.

The sidebar/content layout is inspired by the owner-supplied [Xiangtai Li homepage](https://lxtgh.github.io/) / Academic Pages reference. This implementation uses independent HTML, CSS, and JavaScript instead of importing its Jekyll theme, crawler, personal content, or tracking configuration.

## Publish

Commit the site changes and push the repository’s `master` branch. Keep GitHub Pages configured to deploy from that branch’s root. `.nojekyll` tells GitHub Pages to serve these static files directly. If Pages is configured with a custom workflow, that workflow must upload the repository root as its Pages artifact.
