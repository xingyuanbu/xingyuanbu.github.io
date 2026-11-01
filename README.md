# Xingyuan Bu · Academic Homepage

Personal academic website for **Xingyuan Bu (卜兴源)**, built on the supplied [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) Jekyll template. Production URL: https://xingyuanbu.github.io/.

The page retains the template’s sidebar and single-page structure, with a restrained blue-and-white style and **text-only publications**. It supports desktop, tablet, mobile, keyboard navigation, and reduced-motion preferences.

## Edit content

| File | Purpose |
| --- | --- |
| `_config.yml` | Identity, contact details, production URL, SEO, optional integrations |
| `_pages/about.md` | Biography, research interests, experience, education, service, talks, awards, patents |
| `_data/publications.yml` | Publication titles, authors, venues, years, and verified source links |
| `_data/navigation.yml` | Top navigation links |
| `_includes/publications.html` | Text-only publication rendering, grouped by year |
| `_includes/author-profile.html` | Sidebar profile |
| `_sass/_custom.scss` | Responsive layout and personal styling |
| `images/xingyuan-bu.jpg` | Photo retained from the previous homepage |

Publication data uses JSON syntax inside a YAML file; JSON is valid YAML. Add a publication with `title`, `year`, and `venue`, plus optional `authors`, `paper`, `code`, and `scholar`. Keep entries ordered by descending publication year; the template groups entries in that order. Write `Xingyuan Bu` in the author field to highlight the name automatically. `*` denotes equal contribution; `#` denotes corresponding author. Do not guess missing authors or URLs.

## Preview locally

Use Ruby with Bundler, following the upstream [local setup instructions](docs/README-zh.md). Install the locked dependencies, then run:

```sh
bundle install
bash run_server.sh
```

Open http://127.0.0.1:4000. The server rebuilds changes automatically. A production build can be checked with:

```sh
bundle exec jekyll build --strict_front_matter
```

The supplied lockfile is from an older GitHub Pages template. Ruby 2.6 can reproduce it; a newer Ruby may require a deliberate dependency update. Avoid replacing the template or committing machine-specific dependency paths.

## GitHub Pages

The existing `Gemfile` uses `github-pages`; no JavaScript build step or external font service is needed. Publish this directory’s contents in the `xingyuanbu/xingyuanbu.github.io` repository and configure GitHub Pages to build the intended branch from the repository root. If Pages uses a custom Actions workflow, keep that workflow’s source and Jekyll build settings consistent with this directory. Local previews and files in `docs/` are excluded from the published site.

## Citation data and optional integrations

Displayed metrics are a **dated snapshot** from the supplied Scholar export: 2,275 citations and h-index 21, October 24, 2026. They are not presented as live statistics. Update both the numbers and date together in `_pages/about.md`.

The original citation crawler and GitHub workflow remain available. Automatic display is disabled with `google_scholar_stats_enabled: false`; the current page does not depend on a successful crawl. To customize live counters later, follow [the original documentation](docs/README-upstream.md), configure `GOOGLE_SCHOLAR_ID` in GitHub, add counter markup, and enable that option. The fetch script preserves fallback values when offline or when a publication is missing. The template’s scheduled workflow still requires its original GitHub configuration.

Google Analytics loads only when `google_analytics_id` is configured. No new analytics ID has been added.

## Sources and verification

See [content provenance and editorial decisions](docs/content-sources.md). The previous homepage and the reference website were used as read-only sources.

## Credits

Based on AcadHomepage, itself influenced by Minimal Mistakes and AcademicPages. Original licensing is preserved in `LICENSE`. Upstream documentation is retained in [English](docs/README-upstream.md) and [Chinese](docs/README-zh.md).
