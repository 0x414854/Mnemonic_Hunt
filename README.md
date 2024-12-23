![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white) ![Static Badge](https://img.shields.io/badge/MIT%20License-grey) ![Static Badge](https://img.shields.io/badge/bitcoin-%23ff9900?logo=bitcoin&logoColor=white)

# Mnemonic Hunt©

## Project Description

Welcome to the Mnemonic Hunt!
<br>This project is inspired by the Mnemonic Bitcoin Puzzle created by **CoinMonks** in 2019. **It offers a fascinating way to explore cryptographic concepts while aiming to claim a Bitcoin reward.**

## Table of Contents

- [Project Description](#project-description)
- [Table of Contents](#table-of-contents)
- [What is Mnemonic Bicoin Puzzle ?](#what-is-mnemonic-bitcoin-puzzle)
  - [Description](#description)
  - [History](#history)
  - [Rewards](#rewards)
  - [Hints](#hints)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Install Required Packages](#install-required-packages)
  - [Generate License Key](#generate-license-key)
- [Usage](#usage)
- [Security and Ethics](#security-and-ethics)
- [Benchmarks](#benchmarks)
- [Roadmap](#roadmap)
- [Tree Directory](#tree-directory)
- [Contributions](#contributions)
- [Support the Project](#support-the-project)
- [Useful Links](#useful-links)
- [License](#license)
- [Author](#author)

## What is Mnemonic Bitcoin Puzzle ?

### Description

**The challenge involves deciphering a hidden mnemonic phrase embedded in the article** :
[Securing Bitcoin Seed Phrases in Stories](https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254).

### History

Created by CoinMonks in 2019, this puzzle introduces an innovative method of embedding recovery phrases into stories to enhance their security.

### Rewards

- **Wallet Address** : [1K4ezpLybootYF23TM4a8Y4NyP7auysnRo](https://btcscan.org/address/1K4ezpLybootYF23TM4a8Y4NyP7auysnRo)
- **Prize**: `0.0312463 BTC` _(~$2,903 at the time of writing)_

### Hints

To participate, **extract the words from the article** and **reconstruct the mnemonic phrase that unlocks the Bitcoin wallet.**

---

## Features

- 🔍 **Specific Wallet Search**
  <br>_Find the mnemonic of a specific Bitcoin wallet._

- 🎲 **Custom Mnemonic Length Generation**
  <br>_Generate mnemonics of various lengths (**12** and **24 words**)._

- 🆕 **Unique Mnemonic Generation**
  <br>_Generates unique mnemonics and records each attempt to avoid duplication, ensuring no repetition even after restarting the program._

- 🧠 **Previously Generated Mnemonics**
  <br>_Handling Loads and skips mnemonics that have already been generated to ensure a unique search._

- 🚀 **Optimized Multi-Threading for Efficient Search**
  <br>_Searches for private keys faster using a multi-threaded approach with dynamic thread allocation based on mnemonic lengths._

- 🔐 **License Key Login System**
  <br>_Secure authentication via an unique license key._

- 📊 **Real-Time Display**
  <br>_Option to display each search attempt in real time._

- 💾 **Result Recording**
  <br>_Automatic saving of found mnemonic, private key and wallet addresses._

- 💻 **Cross-Platform Compatibility**
  <br>_Works on Mac, Windows, and Linux._

## Prerequisites

- Python 3.11
- Required Python libraries : _see [Installation](#installation)_
  - `mnemonic`
  - `bit`
  - `base58`
  - `bip32utils`

## Installation

1. **Clone this repository to your machine**

   ```bash
   git clone https://github.com/0x414854/Mnemonic_Hunt.git
   ```

   ```bash
   cd Mnemonic_Hunt

   ```

2. **Run the following command to install libraries**

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the necessary files**

- `users.csv` : **Contains usernames and license keys**
  <br>_You can generate a license key using the_ [Generate_License_Key](https://github.com/0x414854/Generate_License_Key) _repository._
- `words.txt`: **Contains the wordlist**

4. **You're ready to run the program** !

   ```bash
   python3 mnemonicHunt.py
   ```

## Usage

1. **Run the script**

   ```bash
   python3 mnemonicHunt.py
   ```

2. **Connect to the Bot**
   <br><br>If the `license key` or `username` is not valid, **return to the home screen.** <br>If the authentication is incorrect **more than three times**, **the program will close**.

3. **Display each attempt**
   <br>choose whether to display each attempt or not when prompted then the search process begins automatically.

4. **Search begin !**

### Output

- Matching mnemonics, private keys, and wallet addresses are saved in `utils/Enjoy.txt`.

## Security and Ethics

This tool is designed for educational and ethical purposes only. Misuse of cryptographic tools may violate laws and ethical standards.

---

## Benchmarks

Performance metrics:

- Average mnemonics tested per second: 1000+ with multithreading.
- Successful discovery time depends on the complexity of the phrase.

---

## Roadmap

- Add GPU support for faster processing.
- Expand wordlist compatibility.
- Introduce a graphical user interface.

---

## Tree Directory

```
├── utils/
│   ├── words.txt
│   ├── users.csv
│   └── Enjoy.txt
├── logs/
│   └── mnemonicHunt.log
├── Results/
└── main.py
```

---

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## Support the Project

If you find this project helpful, consider supporting it by sharing or contributing.

---

## Useful Links

- [CoinMonks Blog](https://medium.com/coinmonks)
- [Bitcoin Wallet Explorer](https://btcscan.org)

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

Developed by the CoinMonks team and powered by 0x414854.
