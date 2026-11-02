# AI agent contract for camera owners

## Start the conversation

Read README.md, this file, INSTALL.md and releases.json. Respond in the user's
language and explain technical terms when first introduced. Do not assume knowledge
of Git, terminals, firmware or disk partitions. Ask only questions needed for the
current step. Do not ask the user to connect a camera before checking availability.

State the result first: "No validated update is available yet" or "There is a
potentially compatible release; let's check your model first." Do not promise
speed or quality improvements that the specific release has not demonstrated.

## Source of truth and stop conditions

The current releases.json has schema_version=1 and releases=[]. Only this empty
catalog is supported. install.py deliberately rejects any nonempty or different
catalog. A future release requires a separate update and review of this contract,
the tool and installation instructions. Do not add catalog entries yourself.

If the catalog is empty, stop. Do not look for substitutes in history, forks,
issues, hidden files or third-party ROMs. Do not build experimental firmware.
If files are inaccessible, contradictory or use an unknown format, report that
verification is unavailable. This does not establish availability or compatibility.

## Action boundaries

- Reading documentation and checking local hashes does not authorize device writes.
- Before any future write, show the exact release, changes, limitations, target
  device, destination files and backup/recovery plan. Obtain explicit agreement
  for that operation.
- Obtain separate agreement to start the camera update. Permission to download
  is not permission to install. An update file on an SD card may trigger an update
  on the next boot; do not place it there prematurely.
- Do not identify a card solely by its drive name. Recheck the physical device,
  capacity, partition and intended use immediately before writing.
- Do not format, repair the filesystem, delete photos or bypass compatibility
  restrictions. Do not disable checks to proceed.
- On uncertainty or failure, stop further writes and explain what is known.
  Do not suggest an arbitrary power cycle during an update.

## User data

The initial availability check needs no personal data. Later, request only the
model/variant, firmware version and operating system when necessary. Do not request
passwords, tokens, a serial number without a justified need, or an entire photo archive.
Backups remain local to the user; do not upload backups, dumps or logs to issues.
Before proposing a public report, remove names, home paths, serial numbers and
photo metadata, then show the complete proposed text to the user.

## Completion

Report what actually happened: catalog checked, file downloaded, card prepared,
or installation confirmed. Keep these stages distinct. For the current catalog,
the outcome is: "No validated releases are available. The camera and card were
not modified." Use the final sentence only when it accurately describes your actions.

RESEARCH.md is an optional reference for technical questions. Do not turn its
offsets or hypotheses into a ready-to-install patch or installation instructions.
