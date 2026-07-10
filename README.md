# WordFetch

Look up word definitions instantly — just select a word and hit a hotkey. No copying, no browser, no fuss.

## How it works

1. **Select a word** with your mouse (anywhere — browser, terminal, document)
2. **Press your hotkey** (e.g. `Ctrl+M`)
3. **Get a notification** with the word's definition, right on your desktop

That's it. WordFetch reads from your primary selection (the middle-click clipboard), looks up the word via the [Free Dictionary API](https://dictionaryapi.dev/), and pops a desktop notification with the result.

![WordFetch notification](screenshot.png)

## Installation

```bash
git clone https://github.com/yugal-07/WordFetch.git
cd WordFetch
python3 -m venv venv
source venv/bin/activate
pip install requests desktop_notifier
```

### Dependencies — what you need

**Python packages** (via pip):
- `requests` — makes the API call to dictionaryapi.dev
- `desktop_notifier` — shows native desktop notifications via D-Bus

**System packages** — depends on your display server:

| Your setup | Install this | What it does |
|------------|-------------|--------------|
| **Wayland** (Sway, Niri, Hyprland, etc.) | `wl-clipboard` | Provides `wl-paste` to read primary selection |
| **X11/Xorg** (i3, bspwm, Openbox, etc.) | `xclip` | Reads from the primary selection buffer |

WordFetch auto-detects your display server, so just install the one that matches your setup.

**Debian/Ubuntu:**
```bash
# For Wayland
sudo apt install wl-clipboard

# For X11
sudo apt install xclip
```

**Arch:**
```bash
# For Wayland
sudo pacman -S wl-clipboard

# For X11
sudo pacman -S xclip
```

## Usage

1. Select any word with your mouse
2. Run the script or press your hotkey
3. Read the definition in the notification

### Set up a hotkey

**Example for Niri (Wayland):**

Create a wrapper script:
```bash
#!/bin/bash
/home/you/WordFetch/venv/bin/python3 /home/you/WordFetch/dictionary.py
```

Add a keybinding in your Niri config:
```kdl
Ctrl+M { spawn "sh" "-c" "/path/to/WordFetch.sh"; }
```

**Example for i3 (X11):**

Add to your `i3/config`:
```
bindsym Ctrl+m exec /home/you/WordFetch/venv/bin/python3 /home/you/WordFetch/dictionary.py
```

Adjust the paths to match your setup.

### Run directly

```bash
source venv/bin/activate
python3 dictionary.py
```

Or without activating the venv:
```bash
./venv/bin/python3 dictionary.py
```

## Notes

- WordFetch uses the **primary selection** (middle-click paste), not Ctrl+C. Just highlight text — no need to copy it.
- Words longer than 50 characters or empty selections are silently ignored.
- Definitions come from the [Free Dictionary API](https://dictionaryapi.dev/) — no API key needed.
