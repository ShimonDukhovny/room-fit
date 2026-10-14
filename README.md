# Room Fit

A furniture-layout planner for real rooms: enter a room's walls, doors and windows, then drag
furniture around to see what fits, how much space is left, and where things conflict.

## Use it

- **On a Mac or PC:** open `index.html` in Chrome or Edge (double-click it). It works offline
  and needs no account. Without internet the type falls back from Archivo to Arial.
- **On the web:** the same `index.html`, served by GitHub Pages.
- **In Claude:** `src/room-fit.html` is published as a Claude artifact.

## Where rooms are kept

The sidebar holds **projects** (a client or a house), each with **rooms**.

- **A folder on this computer** (Chrome and Edge): choose "Use a folder on this computer".
  Each project is a sub-folder and each room is a `.roomfit.json` file, saved automatically.
  A folder inside iCloud Drive is backed up and syncs to other Macs. After the browser
  restarts it may ask for permission again: "Reconnect the folder". Changes made before
  reconnecting are kept in the browser and written to the file on reconnect.
- **In the browser** (Safari, Firefox, and inside the Claude artifact): projects live in that
  browser's storage. Use "Save room to a file" to keep copies.

The file on a Mac, the website and the Claude artifact each have their own browser storage.
To move a room between them, save it to a file and open it with "Open a saved room", or keep
it in the shared folder.

## Room files

A room file is JSON: `{ "app": "Room Fit", "version": 1, "savedAt": "…", "room": { … } }`.
All lengths are stored in inches, whatever units are showing, so switching units never changes
a file. Older files (from before doors could be several) still open.

## Build

`src/room-fit.html` is the single source, written as a Claude artifact fragment.
`python3 build.py` wraps it into the standalone `index.html`. Edit the source, never
`index.html` directly.

## Publishing to GitHub Pages (not done yet)

GitHub Pages is free for **public** repositories; a private repository needs a paid plan.
Anyone with the address could open the app itself, but rooms stay on each person's computer.

1. Create a public repository and push this folder to it.
2. In the repository: Settings → Pages → Deploy from a branch → `main`, folder `/ (root)`.
