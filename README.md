# oi-browser

Browser automation backend for [Oi](https://github.com/akankofik-dev/Oi): CDP-driven
Chrome control, record/replay, an MCP server, and skill generation from recorded
sessions.

## Install

```bash
pip install oi-browser
```

From the Oi checkout it is pinned as a git dependency, so there is nothing extra
to do — `uv sync` resolves it.

## What's inside

| Module | Purpose |
|---|---|
| `oi_browser.cdp` | Launch and drive Chrome over the DevTools Protocol |
| `oi_browser.actions` | Screenshot / capture actions |
| `oi_browser.record` | Record a session, replay it later, store the artifacts |
| `oi_browser.cli` | `oi-browser` command-line entry point |
| `oi_browser.mcp_server` | Expose the browser over MCP for agent tool use |
| `oi_browser.install` | Chromium download and system dependency setup |
| `oi_browser.profile` | Persistent browser profile management |
| `oi_browser.settings` | Paths and runtime settings |

State lives under `~/.oi-browser/` by default (profiles, screenshots,
recordings). Override with `OI_HOME` if Oi is configured elsewhere.

## CLI

```bash
oi-browser --help
```

## Provenance

This package is the `oi_browser` module of the `octop-browser` distribution
(`orcakit`, MIT), renamed so it matches the Oi rebrand. The upstream wheel did
not ship its own licence file or copyright header; the MIT notice it is
distributed under is reproduced in [LICENSE](LICENSE) here.

## License

MIT — see [LICENSE](LICENSE).