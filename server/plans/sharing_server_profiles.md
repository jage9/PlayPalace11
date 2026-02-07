# Sharing server profiles from client to client
The server manager stores a lot of information for each server. This includes:
*server info like name, address, and port.
*User accounts to log into the server.
*Options profile (migrated from v10).

## Goal of system
The goal is to build a flexible system that will allow for easily sharing only specific details from one client to another. This is necessary because the identities.json file has sensitive information that should not be shared around, and doing so would also completely overwrite a client's previous data.
Therefore, both the user exporting the data and the user importing data, should have full control over what gets shared, overwritten, and/or added.

## Method
To accomplish this flexible system, we only need one screen, an import / export config screen. As well as tracking the mode "import" or "export".
Both modes will have almost identical controls, however there will be slight differences. Importing data will have more options since it is more complex and has the potential to merge with existing data.
To import or export data, the main server manager screen will have a button for each operation.
All checkboxes in the dialog start unchecked by default in both modes, including servers in the available servers list. The "included types" visibility filter is the exception — all its items are checked by default (showing all control types).

## Important Temporary Note
Option profiles at the current moment are empty. This is expected at the time of adding these features. It should still behave as normal, since exporting / importing things like option profiles and user accounts just coppies the object.

## Updated server manager main layout
After the default options profile button, add the "import server profiles" and "export server profiles" buttons.

## Config Sharing Dialog layout
These controls are present regardless of the mode.

*Filters (grouping)
*included types (checklistbox): controls which types of data are visible in the server panel. The label adapts to the mode ("export types" or "import types"). Items are: user accounts, option profiles. In import mode, "server info updates" is also included when applicable. The list is dynamic: if no servers have data for a given type, that type is removed from the list. All items are checked by default. Checking an item shows the corresponding control in the server panel; unchecking hides it. This does not change the value of any server's settings, it only affects visibility. Hiding and unhiding a type preserves whatever state the user set per server.

In import mode only:
*server filter (radio button): placed at the top of the dialog before the server list. Filters and refreshes the available servers list. Values are: all, existing only, new only.
In the "all" view, each server in the list should be labeled as either "existing" or "new" so the user can distinguish them without needing to switch filters.
If a filter results in an empty list, display an accessible message such as "No existing servers with changes" or "No new servers found."

*Details (grouping)
*available servers (checklistbox): the list of available servers to manage data from. When enabled, includes the general information for the focused server along with the data type controls in the server panel.
*ServerPanel (panel)

### Server Panel
Each server has these controls:
*add user accounts (checkbox): determines if the list of user accounts for the focused server should be included in the operation. The number of accounts is appended to the label as part of the accessible name (e.g., "add user accounts, 3 accounts"). If the server has 0 user accounts, this checkbox is grayed out.
*add options profile (checkbox): determines if the options profile for the focused server should be included in the operation. If no options profile data is available for this server, this checkbox is grayed out with "(will use defaults)" appended to the accessible label.

In import mode only, for existing servers where the imported name or port differs from the current data:
*server info (read-only multiline): displays the imported server info for comparison.
*update server info (checkbox): determines if the server name and port should be updated to match the imported data.
If the imported server info is identical to the existing server (comparing name and port only, not notes), the server info display and update checkbox are hidden entirely.

If the selected server is unchecked, hide the entire panel. A brief message such as "Server not included" can be displayed in its place.

*operation (grouping)
*start import/export (button): confirms and starts the operation. If no servers are checked, display a message such as "No servers selected" and keep the user on the dialog.
*cancel (button): aborts the operation. Pressing Escape or closing the dialog window is treated the same as pressing Cancel. The cancel confirmation only appears if the user has interacted with the controls (checked or unchecked something); otherwise the dialog closes immediately.

## Exported Json File
The scheme of the file must match this format exactly:
*description: string (can not be empty)
*timestamp: unix timestamp (not optional)
*servers: array (can not be empty, elements must be json objects)

### Example File
{
 "description": "Zarvox's export",
 "timestamp": 11112121111,
 "servers": [] # Copied data
}

## Exporting data
This is the simpler operation. It uses the current data from "identities.json" to populate the list of available servers. The data is already loaded into the config manager, so no reading from disc required.

### Saving Confirmation
After the user presses the "start operation" button, ask a confirmation for each export warning.
When saving, ask for a description for this export using a simple text entry dialog. The description is required and cannot be empty. Add the unix timestamp when the export occurred.
Prompt the user with a save file dialog. The default filename should be "identities-export.json" and the default directory should be the current working directory.

### Export Warnings
user accounts (for any server):

"User accounts are included in this export. Are you sure you want to proceed?
Some servers will ban the account owner and anyone else who attempts to access the same account."

### Saving to disc
Do not include servers that are unchecked in the available servers list.
Clear unused fields instead of deleting them from the data to make importing easier. This includes both fields the user did not select (e.g., unchecked user accounts results in an empty accounts array) and specific sensitive fields. The server's trust certificate and last connected user account should always be cleared. Server IDs and account IDs are kept as-is in the exported data.
After exporting, display a success summary and return to the server manager main screen.

## Importing data
Importing data is more complex. It uses a json file to populate the available servers list. The data is also compared against the client's current configuration in the config manager.

### Loading Exported Json File
After pressing the import button, a json file should be loaded. The system can automatically check for a file in the current working directory called "identities-export.json". If found, it will ask the user if they want to load this configuration, specifying the export description and formatted timestamp assuming the file is valid.
If the file is invalid, or the user selects no, or no file was found, they can browse for a json file to import. After selecting a file, the export description and formatted timestamp will also be revealed to ensure this is the correct file.
If the chosen file is invalid, return to the browser.

### Filtering the available servers list
The user may have some servers in common with the imported data. An existing server is determined by matching server address. Include existing servers in the available servers list.
If an existing server has no new or changed user accounts and no imported options profile, remove it from the available servers list since there is nothing meaningful to import for that server.
If all servers are removed after this filtering (no new servers and no existing servers with changes), display a message dialog informing the user that there is no data to import, and return to the main server manager screen.

### Saving Confirmation
After the user presses the "start operation" button, ask a confirmation for each import warning.
The user may have some servers in common with the imported data. An existing server is determined by matching server address.
For each server, the user may have some user accounts in common with the imported data. An existing user account is determined by matching username.
If any fields are different than the existing account info such as password or email, ask if the user wants to update the account, listing the field names that have been changed. Notes are excluded from this comparison. Ask for each existing account. The prompt options are:
- Update
- Skip
- Update all for server "{server name}"
- Skip all for server "{server name}"
New accounts (no matching username) are silently added without prompting when "add user accounts" is checked for that server.
For new servers, if options profile is unchecked, it uses the user's default options profile.

### Notes handling
Notes fields (on both servers and user accounts) are excluded from change comparisons. When the user updates a server or account, imported notes are appended to the existing notes with a header:
"\n\n" if existing notes +
"Imported Notes From Export (export description, export date):\n#imported notes content"

Multiple imports will stack these headers, which is acceptable.

### Import Warnings
user accounts (for any server):

"User accounts are included in this import. Are you sure you want to proceed?
Some servers will ban the account owner and anyone else who attempts to access the same account."

option profiles (for any server):
"Option profiles will overwrite your existing settings. Do you want to proceed?"
Note: Options profile import is a full replacement, not a merge.

### Error handling
If an error occurs during import or export, attempt to rollback any partial changes. Display an error message to the user.

### Saving to config
After the data is imported, save the "identities.json" file. Display a success summary (e.g., "Imported 2 new servers and updated 3 accounts") and return to the server manager main screen.
Repopulate the servers list, keeping the initial index if possible, 0 if not.

## Implementation Guidelines
The dialog, export/import logic, and merge logic all belong in `client/ui/config_sharing.py`. The server manager main screen buttons (import/export) will open this dialog.
If any of these helpers are later found to be broadly useful, they can be moved to `config_manager.py`.
