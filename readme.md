# View Networks

- **Author:** Edilberto Fonseca <edilberto.fonseca@outlook.com>
- **Created on:** 2022-07-08
- **Last updated:** 2026

---

The **View Networks** add-on allows you to list Wi-Fi networks saved on the system and view the complete details of a specific network, using information provided directly by Windows through the `netsh` command.

> ⚠️ **Important note:**  
> This add-on **does not crack, decode, or attempt to discover Wi-Fi passwords**.  
> It only displays information **already stored on the system**, including the password **only when Windows itself allows it** (networks the user has previously connected to).

---

## How to use

Using the add-on is simple and fully accessible with NVDA.

View Networks can be opened:

- from the **NVDA Tools menu**, or
- via a **configurable keyboard shortcut**.

When opened, the add-on displays **a single unified window**, where all functionality is centralised.

---

## Main window (unified interface)

The main View Networks window brings all features together in one dialog, making the add-on more organised and intuitive.

### Window components

1. **“Network name” field**
   - Optional field
   - Should only be filled in when the user wants to view details of a specific network.

2. **“Encoding” field (text encoding)**
   - Allows selecting the encoding used to interpret the output of the `netsh` command.
   - The selected encoding is applied **both to the network list and to the network details**.
   - Available options:
     - `cp850` (default)
     - `cp1252`
     - `latin-1`
     - `utf-8`
     - `cp437`

   This option is especially useful on systems with different Windows language or regional settings.

3. **“List saved networks” button**
   - Executes the command:

     ```dos
     netsh wlan show profile
     ```

   - Lists all Wi-Fi networks saved on the system.
   - The complete output is shown in the output field.

4. **“Show network details” button**
   - Uses the name entered in the “Network name” field.
   - Executes the command:

     ```dos
     netsh wlan show profile name="NETWORK_NAME" key=clear
     ```

   - Displays **the full output returned by Windows**, exactly as it appears in the Command Prompt.
   - If the field is empty, NVDA informs the user that a network name is required.

5. **Output field (multiline text)**
   - A single area where:
     - the list of saved networks is displayed, or
     - the full details of a specific network are shown.
   - Focus is automatically moved to this field after each operation, making reading with NVDA easier.

6. **“Copy” button**
   - Copies the entire content of the output field to the clipboard.
   - Useful for pasting into emails, documents, or technical support requests.

7. **“Close” button**
   - Closes the add-on window.
   - Can also be activated using the **Escape** key.

---

## Accessibility

The add-on was developed with a strong focus on accessibility:

- All actions provide **spoken feedback via NVDA**.
- Focus is automatically managed after each operation.
- No multiple or confusing dialogs.
- The entire interface can be operated using only the keyboard.

---

## Keyboard shortcuts

Keyboard shortcuts may vary depending on the user’s configuration, but typically include:

1. **Windows + Alt + N** – Opens the main View Networks window
2. **Windows + Alt + O** – Displays add-on information
3. **Windows + Alt + J** – Opens the add-on help page

> Note: Shortcuts can be customised in NVDA’s Input Gestures settings.

---

## About

The **About** option displays detailed information about the add-on, including:

- Add-on version
- Author
- Description
- Minimum required NVDA version
- Latest tested NVDA version

---

## Final notes

The current version of View Networks provides:

- A unified and better-organised interface
- Improved stability
- Better compatibility with different Windows languages
- A significantly improved experience for screen reader users

The add-on has evolved to deliver **clarity, control, and accessibility**, while always respecting the limitations and security enforced by the operating system.
