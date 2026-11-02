# Instructions for AI agents

## Start the conversation

Read README.md, this file, INSTALL.md and releases.json. Use the user's language and explain unfamiliar terms. Assume the user may not
know Git, terminals, firmware or disk partitions. Ask only questions needed for the
current step. Do not ask the user to connect a camera before checking availability.

State the result first: "An experimental download exists, but no supported update is available yet" or "There is a
potentially compatible release; let's check your model first." Do not promise
speed or quality improvements that the specific release has not demonstrated.

## Check whether an update is available

The current releases.json has schema_version=1 and releases=[]. Only this empty
catalog is supported. install.py deliberately rejects any nonempty or different
catalog. A future release requires a separate update and review of this contract,
the tool and installation instructions. Do not add catalog entries yourself.

The catalog covers supported installation releases only. V3.1 is separately
published as an experimental prerelease linked in README.md. You may explain its
status and provide that download link when asked; do not present it as a supported
update or automatically stage it on a card.

If the catalog is empty, stop the supported installation workflow. Do not look for substitutes in history, forks,
issues, hidden files or third-party ROMs. Do not build experimental firmware.
If you cannot read the files, their contents conflict, or the format is unknown,
explain what prevented the check. Do not infer that an update is available or compatible.

## Before writing to a card or camera

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

## Report the outcome

Say exactly what you completed: checking the catalog, downloading a file, preparing
a card or confirming an installation. Do not report a later step as complete
just because an earlier one succeeded. For the current catalog,
the outcome is: "V3.1 is available as an experimental download, but there is no
supported installation release. The camera and card were not modified." Use the final sentence only when it accurately describes your actions.

RESEARCH.md is an optional reference for technical questions. Do not turn its
offsets or hypotheses into a ready-to-install patch or installation instructions.
