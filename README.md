# SWCodes
SW Codes is a discord bot to facilitate the use of codes on the mobile game Summoners War


## TODO:
### Commands
- [x] Add a command to show the list of all commands and descriptions (/help)
- [x] Add a command to use a code on an account (/usecode 『hiveid』 『code』)[^5]
- [x] Add a command to register an ID to the list of IDs (/registerid 『hiveid』)[^1] [^5]
- [x] Add a command to unregister an ID from the list of IDs (/unregisterid 『hiveid』)[^5]
- [x] Add a command to use a code on all registered IDs (/trigger 『code』)[^2]

### Features
- [x] A JSON file to store the list of registered IDs (a real db is overkill)[^3] [^4]

### Extra
- [x] Change `token` to a `.env` file with token & ownerid
- [ ] Make a proper README
- [ ] Add a log system

### Lastly
- [x] Test the bot
- [ ] Host the bost on OCI

[^1]: Add a disclaimer or something to tell the user agree to share their ID and have it stored in a file (private for everyone but the bot owner)
[^2]: See if it won't cause trouble with the API/avoid banning accounts, maybe limit the number of registered IDs or only allow the command for the owner 
[^3]: Add the list to the [`.gitignore`](./.gitignore) file for security reasons
[^4]: HiveID : DiscordID for key-value pairs
[^5]: Use ephemeral messages for privacy