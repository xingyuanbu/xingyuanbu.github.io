# Content sources · November 2026 update

## Supplied sources

- `../xingyuanbu.github.io.backup/index.md`: earlier biography, advisors, contact links, photo, full author names, paper and code links.
- `../zh/10.2en_niv.tex`: current appointment, career and education dates, 37 selected publications and venues, patents, talks, awards, memberships, and reviewer service.
- `../EOI_20261024/_Xingyuan Bu (卜兴源)_ - _Google Scholar_.html`: saved publication metadata, Scholar item URLs, abbreviated authors and contribution markers, citation count and h-index.
- `../lxtGH.github.io/`: layout reference, particularly compact publications without thumbnails.

Paths above are relative to the website checkout, not to this document. The local source files are authoritative for this update; no claim is made that the saved Scholar data is live.

## Editorial choices

- The CV supersedes the former homepage’s Alibaba appointment. The current role is Staff Research Engineer and Tech Leader at ByteDance / TikTok, Shanghai, since October 2024.
- The CV contains repeated qualification bullets. These were deduplicated rather than reproduced. Detailed business revenue and infrastructure figures were omitted from the public biography.
- Publication years use the CV’s venue years, not the first preprint year reported by Scholar (for example ACL 2025 and ECCV 2026 entries).
- ConceptMath is labeled ACL 2024 Findings, as stated in the supplied Scholar venue.
- The CV lists VideoLVR, but no matching Scholar row or paper URL is present in the supplied sources. Its title and CV venue are included without inventing authors or a link.
- Several saved Scholar author lists are truncated. They remain abbreviated. Full names from the old homepage are retained where available. RoleAgent explicitly abbreviates the list while identifying Xingyuan Bu as a coauthor, as supplied by the old homepage.
- The Scholar export lists the Seed model-card author as “B Seed”; that collective attribution is retained.
- The CV and export agree on 2,275 citations and h-index 21. The public page explicitly dates this snapshot to October 24, 2026.
- Talks are listed using the CV’s venues, dates and topics, without adding unsupplied talk links or media.
- Current hiring availability is not asserted. Visitors are invited to email about collaborations and internships, following the previous homepage’s contact intent.
- Awards have no exact dates in the CV, so none were invented.

## Design and behavior

The supplied AcadHomepage Jekyll structure is retained. Custom styles live in `_sass/_custom.scss`. Publications are rendered from `_data/publications.yml` without images. The original global new-tab target, nested head tag, unused remote MathJax, and unconditional analytics/statistics calls were removed or gated. Internal navigation stays in the same tab. All primary content remains usable without JavaScript.
