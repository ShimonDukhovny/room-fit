# Room Fit

A furniture-layout planner for real rooms: enter a room's walls, doors and windows, then drag
furniture around to see what fits, how much space is left, and where things conflict.

## Use it

- **On a Mac or PC:** open `index.html` in Chrome or Edge (double-click it). It works offline
  and needs no account. Without internet the type falls back from Archivo to Arial.
- **On the web:** the same `index.html`, served by GitHub Pages.
- **In Claude:** `src/room-fit.html` is published as a Claude artifact.

## Where rooms are kept

The sidebar holds **projects** (for example a house or an apartment), each with **rooms**.

- **A folder on this computer** (Chrome and Edge): choose **Use a folder…** in the Projects pane.
  Each project is a sub-folder and each room is a `.roomfit.json` file, saved automatically.
  If Chrome refuses a folder (it blocks some system folders), make a new folder in Documents
  instead. After the browser restarts it may ask for permission again: **Reconnect**.
  Changes made before reconnecting are kept in the browser and written to the file on reconnect.
- **In the browser** (Safari, Firefox, and inside the Claude artifact): projects live in that
  browser's storage. Use "Save room to a file" to keep copies.

### Open a folder of projects

**Open folder…** in the Projects pane works in every browser. Choose a folder laid out like this:

```
Projects/
  Smith house/
    Living room.roomfit.json
    Main bedroom.roomfit.json
  Jones condo/
    Kitchen.roomfit.json
```

Each sub-folder becomes a project and the `.json` room files inside it (at any depth) become its
rooms. Room files at the top level go into a project named after the folder. Rooms are copied
into the workspace; any room already there is skipped, so opening the same folder again adds
only what's new. In the browser workspace the original folder is never changed.

The file on a Mac, the website and the Claude artifact each have their own browser storage.
To move a room between them, save it to a file and open it with **Open a saved room**, or keep
it in the shared folder.

The **?** next to where projects are saved explains these options in the app itself.

## Room files

A room file is JSON: `{ "app": "Room Fit", "version": 1, "savedAt": "…", "room": { … } }`.
All lengths are stored in inches, whatever units are showing, so switching units never changes
a file. Older files (from before doors could be several) still open.

## Build

`src/room-fit.html` is the single source, written as a Claude artifact fragment.
`python3 build.py` wraps it into the standalone `index.html`. Edit the source, never
`index.html` directly.

## GitHub Pages

The site is served from `main`, folder `/ (root)`. GitHub Pages is free for **public**
repositories; a private repository needs a paid plan.
Anyone with the address can open the app itself, but rooms stay on the computer they were made on.

