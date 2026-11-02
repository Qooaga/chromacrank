# Technical findings

Research status: 2026-11-02. This note records findings from public ROM images
and the questions still open. It is a starting point for further investigation,
**not a set of ready-to-install patches or update instructions**. There are no
supported releases, and compatibility with an individual camera is unverified.

## Reference images

Complete 2 MiB SPII images, identified by SHA-256:

- Project-Sirius: `720ed0b65c91b149b0916498732b0ecf40227736ef5e3c126c487a7b5253436c`.
- Keychain: `cc3b4b2fd7eb71ba5a441decdc86984261fac8418ee3e105d7e2b3c38b7ea42f`.

Binaries are not distributed here. A hash identifies a research input, not the
firmware installed on a particular camera. For the coordinates below,
**file offset = runtime address + 0x200**.

## Findings from static analysis or bounded emulation

| Area | Finding | Limitation |
|---|---|---|
| JPEG | Stock selector 80 chooses quantization tables matching IJG80. Separate presets 90/95 are available and have been checked | The complete still-photo-only configuration path is unproven; hardware setters were stubbed in probes |
| JPEG buffers | The studied initializer allocates two buffers of 716800 bytes each | This does not prove the hardware output limit; overflow/error handling remains unresolved |
| Capture events | A static chain was recovered: 0x500B → 0x500D → request → 0x00500000 → capture-front | The physical shutter button and exposure time have not been mapped to this chain |
| Queue | An isolated request function overwrites the enqueue result: the caller receives 0 even with a synthetic error | This does not prove the cause of lag, a dropped frame or the absence of higher-level retries |
| Timers | A tick-based OS delay exists. The 0x7032 branch contains a 20-tick wait, nominally 200 ms at the configured 100 Hz | The branch is linked to post-capture events; the delay is not established as redundant or as first-shot lag |
| FAT | EOF/chain-boundary and writeback-error handling defects were reproduced in reference code; local fixes were tested with synthetic block I/O | Cache caller contracts, multi-block I/O, SD/RTOS and hardware validation remain incomplete; no installable patch |
| USB | The MSC vendor callback checks the GP signature; FD28/FD2A/FF28/FF2A require state==2. The handshake path writes 1 after a synthetic helper | The normal transition to 2 is unknown; bypassing the shared gate also exposes write operations |
| USB data | FD28 reads a word at an address; FF28/FF2A use mapped-memory copy callbacks | This is not a proven complete physical SPI dump; unknown addresses may be MMIO |
| LED | Candidate runtime address 0x1E844 selects a resource and sends a UI message | It is not a proven white capture-light driver; Flash Off is not implemented |

## Reference offsets

Valid only for the two hashes above. All addresses in this table are **file offsets**.

| Area | Offsets |
|---|---|
| JPEG selector | 0x82A94 |
| DQT80 luma/chroma | 0x108CB8 / 0x108D38 |
| DQT90 luma/chroma | 0x108EB8 / 0x108F38 |
| DQT95 luma/chroma | 0x1090B8 / 0x109138 |
| OS delay | 0x906E4 |
| 20-tick argument / call | 0x1E1D4 / 0x1E1D8 |
| Capture message producer | 0xC7E0 |
| MSC vendor callback | 0x2AAD4 |
| FD28 memory dereference | 0x2A92C |
| SPI read wrapper / driver | 0x139C / 0x308B4 |

Before changing an instruction at any of these offsets, check its callers,
branch conditions, ABI, buffer ownership and effects on hardware.
Research tools and the complete evidence set are not included in this minimal
repository; this table does not replace independent reproduction.

## Useful next investigations

1. Measure button-to-exposure, button-to-durable-storage and the interval between
   two successful shots separately. Screen animation and file timestamps are not exposure time.
2. Recover CPU clock settings at boot and during capture before considering
   overclocking. GPCV2247F specifications list up to 144 MHz, hardware JPEG, DMA
   and a scaler; the clock of an individual camera is unverified. The CPU may be
   waiting for peripherals rather than computing.
3. Look for redundant preparation/copying and blocking UI operations while
   preserving required waits, flushes, closes and frame synchronization.
4. Evaluate JPEG90 separately from speed: reduced compression losses can increase
   file size and write time. Do not change AE, NR and PLL simultaneously.

SoC specification: [Generalplus GPCV2247F](https://www.generalplus.com/GPCV2247F-gCwgf-phLV2kcoLN5006SVpnSNproduct_detail).
These specifications do not establish that every camera variant uses this chip.

## Before hardware experiments

The stock SD updater in the studied images touches boot regions. A small patch
does not make installation transactional. Before an experiment, obtain a complete backup of the specific device, verify
a recovery method and compatibility, and have the exact changes independently reviewed. A public stock ROM or photo backup is not a flash backup.

Color behavior, file preservation, boot and other camera modes need separate
validation. Emulation with stubbed peripherals is not a hardware test. These findings do not yet demonstrate a speed improvement or establish a safe
installation procedure.
