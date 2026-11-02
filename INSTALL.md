# Installation guide

**V3.1 is available as an experimental download. There is no supported installation
release yet.** The supported release catalog is empty.

[Get the experimental binary and checksums](https://github.com/Qooaga/chromacrank/releases/tag/v3.1-experimental).
It was installed in a camera trial, but SD-card access failures were observed.
Read the release notes for the known issue and recovery requirements. Downloading
the file to your computer does not require connecting the camera or preparing a card.
Do not treat availability of the binary as approval to install it.

The steps below describe how an agent will help you check and install a future
release. They are not instructions for installing experimental firmware.

| Stage | Agent action | What you do or learn | Condition to proceed |
|---|---|---|---|
| 1. Open the repository | Read required documents and catalog | Learn whether an update is available | Known, supported catalog format |
| 2. Check availability | Look for a validated release | Currently: "No supported update is available; no camera connection is needed" | Stop when the catalog is empty |
| 3. Check compatibility | Follow future release instructions to verify model, variant and source firmware | Answer a few specific questions | Every release criterion is met; a similar name is insufficient |
| 4. Make an informed choice | Explain changes, limitations, risks and recovery | Decide whether to update | All safety requirements are met |
| 5. Download | Use the specific validated release link and check SHA-256 | See which file was obtained and verified | Matching hash and version; a hash alone does not establish provenance |
| 6. Prepare | Check backup, recovery, power and target card | Approve the specific write | Explicit agreement and all release checks passed |
| 7. Update | Follow the release instructions without guessing buttons or filenames | Separately approve the update and perform physical steps | Completion confirmed as described by the release |
| 8. Verify | Check version, capture, storage, playback and normal modes | Receive a clear result and limitations | Check the results rather than assuming success |

Stages 3–8 cannot be followed yet. A future release must provide an exact
compatibility matrix, artifact provenance, input/output hashes, hardware results,
power requirements, backup and recovery requirements, precise update steps and a
failure procedure. This general table does not replace those details.

## Common situations

**"I have the same camera. Can I try it?"**
Without a validated release there is no supported installation procedure.
Cameras that look identical can have different hardware or firmware. Compatibility
needs to be checked, not guessed.

**"My agent cannot open the link."**
You can give the agent README.md, AGENTS.md, INSTALL.md and releases.json directly.
Until their contents have
been checked, the agent must not select firmware or request a device connection.

**"The checksum does not match."**
Do not use the file. Renaming it or disabling verification does not resolve a mismatch.

**"There are important photos on my card."**
A local backup and a readability check are required before any future update.
No card is needed now; formatting is not part of checking availability.

**"An update is running or has failed."**
Do not improvise from this general guide. Use the failure procedure for the exact
installed release. Reflashing or disconnecting power is not a universal recovery method.
