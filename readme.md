# View Networks

- Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
- Creation date: 07/08/2022
- **License**: [GPL v2](https://www.gnu.org/licenses/gpl-2.0.html)

---

**View Networks** is an NVDA add-on that allows users to **list Wi-Fi networks saved on Windows** and **display all details of a specific network**, including the password **when it is stored by the system**.

⚠️ **Important**
This add-on **does not break, force, or attempt to discover Wi-Fi passwords**.
It only displays information **already saved by Windows**, in the same way as the `netsh wlan show profile` command.

---

## What’s new in the current version

- **Unified interface** in a single window
- Two main buttons:
  - **List saved networks**
  - **Show network details**
- Single output field showing the **complete content**, exactly as in the Command Prompt
- Manual **encoding selection**:
  - `cp850` (default)
  - `cp1252`
  - `latin1`
  - `utf-8`
- Automatic detection of:
  - No Wi-Fi adapter present
  - Computers connected only via Ethernet
  - WLAN service disabled
- Compatible with systems **without Wi-Fi**, without causing errors or NVDA restarts

---

## How to use

The add-on can be accessed:

- From the **NVDA Tools menu**
- Or via a **keyboard shortcut**, Windows + Alt + N — Opens the main View Networks dialog

### Main dialog

When opening View Networks, the user will find:

1. **Encoding selection field**
   Allows choosing the encoding used by Windows for correct text display.

2. **“List saved networks” button** Alt + L
   Displays all Wi-Fi networks stored on the system.

3. **“Show network details” button** Alt + M
   Prompts for the network name and displays **all available information**, including the password, if present.

4. **Main text field**
   Shows the complete output of the `netsh` command, without filtering or modification.

5. **Close button** Alt + F
   Closes the dialog.

---

## Behaviour on PCs without Wi-Fi

If the computer:

- does not have a Wi-Fi adapter, or
- is connected only via Ethernet,

the add-on will display a clear message informing that **no Wi-Fi interface was detected**, along with the diagnostic information returned by the system.
