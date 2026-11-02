# User journey: from a repository link to a result

**Current outcome: installation is unavailable.** The validated release catalog
is empty. This is a support workflow, not an experimental firmware installation guide.

| Stage | Agent action | User experience | Condition to proceed |
|---|---|---|---|
| 1. Open the repository | Read required documents and catalog | A short availability explanation | Known, supported catalog format |
| 2. Check availability | Look for a validated release | Currently: "No update is available; no camera connection is needed" | Stop when the catalog is empty |
| 3. Check compatibility | Follow future release instructions to verify model, variant and source firmware | Answer a few specific questions | Every release criterion is met; a similar name is insufficient |
| 4. Make an informed choice | Explain changes, limitations, risks and recovery | Decide whether to update | No outstanding safety requirements |
| 5. Download | Use the specific validated release link and check SHA-256 | See which file was obtained and verified | Matching hash and version; a hash alone does not establish provenance |
| 6. Prepare | Check backup, recovery, power and target card | Approve the specific write | Explicit agreement and all release checks passed |
| 7. Update | Follow the release instructions without guessing buttons or filenames | Separately approve the update and perform physical steps | Completion confirmed as described by the release |
| 8. Verify | Check version, capture, storage, playback and normal modes | Receive a clear result and limitations | Success observed, not assumed |

Stages 3–8 are currently unavailable. A future release must supply an exact
compatibility matrix, artifact provenance, input/output hashes, hardware results,
power requirements, backup and recovery requirements, precise update steps and a
failure procedure. This general table does not replace those details.

## Common situations

**"I have the same camera. Can I try it?"**
Without a validated release there is no supported installation procedure.
Visually identical cameras can differ; do not guess compatibility.

**"My agent cannot open the link."**
You can provide the four required text files directly. Until their contents have
been checked, the agent must not select firmware or request a device connection.

**"The checksum does not match."**
Do not use the file. Renaming it or disabling verification does not resolve a mismatch.

**"There are important photos on my card."**
A local backup and a readability check are required before any future update.
No card is needed now; formatting is not part of checking availability.

**"An update is running or has failed."**
Do not improvise from this general guide. Use the failure procedure for the exact
installed release. Reflashing or disconnecting power is not a universal recovery method.
