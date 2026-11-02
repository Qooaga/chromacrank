# ChromaCrank for Kodak Charmera

**Color experiments and firmware research for the Kodak Charmera.**

ChromaCrank explores how to change the look of this tiny camera through color
rendering, tone curves and JPEG compression. A second focus is understanding
shutter delay and improving the reliability of photo storage.

The goal is to give Charmera owners more control over their images, with a clear,
AI-assisted path to installing validated changes.

<p align="center">
  <img src="kodak-charmera.jpg" width="640" alt="Blue Kodak Charmera keychain digital camera">
</p>

Camera photo: [Ryohei Noda](https://www.flickr.com/photos/g4gti/54970475299/),
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?title=File:Kodak_Charmera_(54970475299).jpg),
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original file, unchanged.

## What you can use today

- **If you own a Charmera:** explore image examples and learn which changes are
  being investigated, what has been tested, and what remains uncertain.
- **If someone sent you this link:** give it to your AI agent. The repository
  includes a ready-to-copy prompt and a guided workflow for explaining the project,
  checking release availability, and assessing compatibility in plain language.
- **If you want to investigate the firmware:** use [RESEARCH.md](RESEARCH.md) as
  a starting map of JPEG presets, capture events, filesystem issues and USB
  behavior, with reference image hashes, offsets and known limitations.

The material available today is documentation and research. There is no downloadable
firmware package or ready-to-use camera modification yet.

## Image examples

<p>
  <img src="example-city.png" width="39%" alt="City scene with cool foliage and muted building colors">
  <img src="example-interior.png" width="58%" alt="Interior with warm highlights and cool shadows">
</p>

Two image examples, not a controlled before-and-after comparison.

## Current work

| Area | Progress |
|---|---|
| **Color and tone** | Experimental color profiles and tone curves have been developed. They are not a validated release, and compatibility across camera variants is not established |
| **JPEG** | Stock quantization tables and quality presets have been investigated. Higher quality still requires validation of the complete photo capture path |
| **Capture speed** | Parts of the firmware event and delay paths have been mapped. A speed improvement on hardware has not been demonstrated |
| **Photo storage** | Filesystem defects have been identified; fixes are being tested under laboratory conditions |

See [RESEARCH.md](RESEARCH.md) for concise findings, reference ROM offsets and
open questions.

## Download and installation

**This project is in the research stage. There is no validated firmware release
available for end-user installation yet.**

This repository contains the project overview, research notes and guidance for
AI-assisted installation. Firmware binaries and research tools are not included.
See [INSTALL.md](INSTALL.md) for installation availability and
[releases.json](releases.json) for the release catalog.

## Use with an AI agent

Give your agent this repository's URL and the following request:

> Help me understand ChromaCrank for my Kodak Charmera. Read README.md, AGENTS.md
> and INSTALL.md, and check the available releases. Explain what the project can
> do today and whether an update supports my camera. If a validated release is
> available, guide me through its installation instructions. Ask for my agreement
> before writing anything to the card. If there is no validated release, stop
> and explain that installation is unavailable; do not substitute experimental firmware.

The agent starts with release availability and compatibility. Detailed operating
rules are in [AGENTS.md](AGENTS.md).

## Contributing

Start with the [research map](RESEARCH.md) for technical investigation.
When reporting a problem, include the camera model and variant, firmware version,
reproduction steps, and expected versus actual behavior. If the version is unknown,
say so. Do not attach private dumps, photo archives or credentials.

---

An independent experimental project. Not affiliated with Kodak and not an official
manufacturer firmware update.
