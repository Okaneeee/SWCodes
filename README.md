<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/fr/c/c2/Summoners_War_Logo.png" width="300" alt="sw logo"></img>

  <h1 align="center">
    🔖 SW Codes 🔖
  </h1>
</p>

## Table of Content
<details>
  <summary> Click me! </summary>

  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Quick Start](#quick-start)
    - [Updating](#updating)
  - [Commands](#commands)
  - [Long-Term Support (LTS)](#long-term-support-lts)
    - [As the developer](#as-the-developer)
    - [Dependencies](#dependencies)
    - [Code Quality & Security](#code-quality--security)
  - [References](#references)
  - [Copyrights](#copyrights)

</details>

## Getting Started
### Installation

<details>
  <summary> Instructions for cloning with git (recommended) </summary>

  - Open a terminal and navigate to the directory where you want to clone the repo.
  - Run the following commands:
    ```bash
    git clone https://github.com/Okaneeee/SWCodes.git
    cd SWCodes
    ```

</details>

<br>


<details>
  <summary> Instructions for zip downloading </summary>

  - Click on the green `Code` button and select `Download ZIP` or click [here](https://github.com/Okaneeee/SWCodes/archive/refs/heads/main.zip).
  - Extract the zip file to the directory where you want to clone the repo. Or in Linux:
    ```bash
    sudo apt-get install unzip
    sudo unzip SWCodes-main.zip -d SWCodes
    ```
  - Open a terminal in the folder where you extracted the zip file and run the following command:
    ```bash
    cd discord-chatbot
    ```

</details>

<br>

This repo was made with Python ``3.11.9``. So you'll need to install python. You can check the working versions of Python for this repo [here](#dependencies). <br>

The repo uses some dependencies. You can install them by running the following command:

Windows:
```bash
pip install -r requirements.txt
```

Linux:
```bash
pip3 install -r requirements.txt
```

<br>

### Quick Start
You'll need to setup a `.env` file first. The `.env` need to be on the same folder as the repo. You can use the following template, or you can rename the [`.env.example`](./.env.example) file to `.env`.

```env
TOKEN =
OWNERID = 
```

**TOKEN** is the bot token you get from the [Discord Developer Portal](https://discord.com/developers/applications). <br>
*More information [here](https://discord.com/developers/docs/getting-started#configuring-your-bot).* <br>

**OWNERID** is the ID of the owner (you). You can get your ID by right-clicking your name in Discord and selecting `Copy ID`. <br>
*More information on how to get your ID [here](https://support.discord.com/hc/en-us/articles/206346498).*
<br>

After, you'll need to [add your bot to your server](https://discord.com/developers/docs/getting-started#installing-your-app). <br>
Finally, you can run the bot by running the following command:

```bash
python src/main.py
```

### Updating
You'll need first to stop the bot by pressing `CTRL + C` in the terminal where the bot is running. <br>

If you cloned the repo when you did the installation, you can update the repo by running the following command:

```bash
git pull
```

If you downloaded the repo as a zip file, you can download the new version by following the same installation steps you did before. <br>
After, unzip the file using the following command in the same directory as the zip file:

```bash
sudo unzip SWCodes-main.zip -d SWCodes
```
and type `A` to replace all the files. <br>
Finally, you can run the bot again by doing:

```bash
cd SWCodes
python src/main.py
```

## Commands
- `/help` 
> Shows the help message with all the commands listed.
- `/usecode [hiveid] [code]`
> Use a code on an account.
- `/registerid [hiveid]`
> Register your Hive ID (linked in the database with the Discord ID of the command invoker).
- `/unregisterid [hiveid]`
> Unregister your Hive ID (only the one who registered it can unregister it).
- `/trigger [code]`
> Trigger a code on all registered Hive IDs. <br>
> **ONLY THE OWNER CAN USE THIS COMMAND**.

## Long-Term Support (LTS)

<img src="https://img.shields.io/github/last-commit/Okaneeee/SWCodes">

### As the developer 
I will be maintaining this repo for a long time. I will be fixing eventual bugs and do the necessary changes in case of a new Discord API update, a new Python version or if the Summoners War API changes. <br>
I will also be updating the dependencies with [Dependabot](https://github.com/dependabot). <br>

### Dependencies
| Version             | Done | Status |
|-------------------------|------|--------|
| Python 3.10 | ✔ | [![Python 3.10](https://github.com/Okaneeee/SWCodes/actions/workflows/python310.yml/badge.svg)](https://github.com/Okaneeee/SWCodes/actions/workflows/python310.yml) |
| Python 3.11 | ✔ | [![Python 3.11](https://github.com/Okaneeee/SWCodes/actions/workflows/python311.yml/badge.svg)](https://github.com/Okaneeee/SWCodes/actions/workflows/python311.yml) |
| Python 3.12 | ✔ | [![Python 3.12](https://github.com/Okaneeee/SWCodes/actions/workflows/python312.yml/badge.svg)](https://github.com/Okaneeee/SWCodes/actions/workflows/python312.yml) |
| Python 3.13 | ✔ | [![Python 3.13](https://github.com/Okaneeee/SWCodes/actions/workflows/python313.yml/badge.svg)](https://github.com/Okaneeee/SWCodes/actions/workflows/python313.yml) |
| Python 3.14 | ✔ | [![Python 3.14](https://github.com/Okaneeee/SWCodes/actions/workflows/python314.yml/badge.svg)](https://github.com/Okaneeee/SWCodes/actions/workflows/python314.yml) |

### Code Quality & Security
| Actions             | Done | Status |
|-------------------------|------|--------|
| CodeQL | ✔ | [![CodeQL](https://github.com/Okaneeee/SWCodes/actions/workflows/codeql.yml/badge.svg)](https://github.com/Okaneeee/SWCodes/actions/workflows/codeql.yml) |
| Dependabot | ✔ | [![Dependabot](https://github.com/Okaneeee/SWCodes/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/Okaneeee/SWCodes/actions/workflows/dependabot/dependabot-updates) |

## References
- [Pycord](https://pycord.dev)
- [Pycord docs](https://docs.pycord.dev/en/stable/)
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Discord API](https://discord.com/developers/docs/reference)
- [Hive Code "API"](https://event.withhive.com/ci/smon/evt_coupon)

## Copyright
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details. <br>
This include all contributions to the project, even from the community.

Copyright © 2024 Okaneeee | Anatole