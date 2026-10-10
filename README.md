# oi-browser

Backend otomasi browser untuk [Oi](https://github.com/akankofik-dev/Oi): kontrol Chrome via CDP,
record/replay, server MCP, dan pembuatan skill dari sesi yang direkam.

## Install

Paket ini **tidak tersedia di PyPI**. Install dari GitHub:

```bash
pip install "oi-browser @ git+https://github.com/akankofik-dev/oi-browser.git@v1.0.1"
```

Dari checkout Oi, paket ini di-pin sebagai dependency git, jadi tidak ada yang perlu dilakukan
manual — `uv sync` akan menyelesaikannya.

## Isi

| Modul | Fungsi |
|---|---|
| `oi_browser.cdp` | Menjalankan dan mengendalikan Chrome via DevTools Protocol |
| `oi_browser.actions` | Aksi screenshot / capture |
| `oi_browser.record` | Merekam sesi, memutar ulang, menyimpan artefak |
| `oi_browser.cli` | Entry point command-line `oi-browser` |
| `oi_browser.mcp_server` | Mengekspos browser via MCP untuk dipakai agent |
| `oi_browser.install` | Unduhan Chromium dan setup dependency sistem |
| `oi_browser.profile` | Manajemen profil browser persisten |
| `oi_browser.settings` | Path dan pengaturan runtime |

State tersimpan di `~/.oi-browser/` secara default (profil, screenshot, rekaman).
Override dengan `OI_HOME` jika Oi dikonfigurasi di tempat lain.

## CLI

```bash
oi-browser --help
```

## Lisensi

MIT — lihat [LICENSE](LICENSE).
