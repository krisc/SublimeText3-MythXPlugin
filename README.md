# SublimeText3-MythPlugin
This is a plugin for Sublime Text 3 which uses [Sabre](https://github.com/b-mueller/sabre) under the hood.

## Prerequisites
- Sabre -- https://github.com/b-mueller/sabre

## Installation
1. Unpack this repository into `/YOUR_HOME_DIRECTORY/.config/sublime-text-3/Packages/MythX`
2. Open the preferences for this plugin (`Preferences.sublime-settings`) and enter the path to your sabre binary. You can run the command `which sabre` to get this path.

## Run
1. Open the `.sol` file which you want to test.
2. `Tools -> MythX -> Test Current File`

## Notes
This plugin was created as part of the Ethereal Hackathon. It was only tested on Linux. I plan to maintain this repo if there is interest. Future development entails not depending on Sabre and testing for Windows and OSx. Feedback is appreciated!
