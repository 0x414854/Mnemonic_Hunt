![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white) ![Static Badge](https://img.shields.io/badge/MIT%20License-grey) ![Static Badge](https://img.shields.io/badge/bitcoin-%23ff9900?logo=bitcoin&logoColor=white)

# Mnemonic Hunt©

## Project Description

Welcome to the **Mnemonic Hunt**!
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
- [Security and Ethics](#🔐-security-and-ethics)
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
- Required Python libraries (_see [Installation](#installation)_)
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

## **Usage**

1. **Run the script**

   ```bash
   python3 mnemonicHunt.py
   ```

2. **Connect to the Bot**
   <br><br>**If the `license key` or `username` is not valid, **return to the home screen.**
   <br>If the authentication is incorrect **more than three times**, **the program will close\*\*.

3. **Display each attempt**
   <br>Choose whether to display each attempt or not when prompted then the search process begins automatically.

4. **Search begin !**

### Output

- Matching mnemonics, private keys, and wallet addresses are saved in `utils/Enjoy.txt`.

## 🔒 **Security and Ethics**

### **Your Data is Safe**

- All operations performed by **Mnemonic Hunt** are entirely local to your system.
- The tool does not send or receive any data over the internet.
- Sensitive files like `mnemonicHunt.log` and `users.csv` remain on your local machine.

By keeping all processes offline, we ensure that **your data stays private and secure**.

### ⚠️ **Disclaimer**

**Mnemonic Hunt** is intended for :

- Research purposes.
- Educational use.
- Solving Bitcoin puzzles and cryptographic challenges legally and ethically.

**Misuse of this tool for unauthorized access or illegal purposes is strictly prohibited and may violate laws in your jurisdiction.**

<!--
## Benchmarks

Performance metrics:

- Average mnemonics tested per second: 1000+ with multithreading.
- Successful discovery time depends on the complexity of the phrase.

--- -->

## **Roadmap**

<!-- - Add GPU support for faster processing.
- Expand wordlist compatibility.
- Introduce a graphical user interface. -->

## **Tree Directory**

.
<br>├── .gitignore
<br>├── LICENSE
<br>├── mnemonicHunt.py
<br>├── README.md
<br>├── requirements.txt
<br>├── logs/
<br>&nbsp;&nbsp;&nbsp;&nbsp;└── mnemonicHunt.log
<br>└── utils/
<br>&nbsp;&nbsp;&nbsp;&nbsp; ├── mnemonic.txt
<br>&nbsp;&nbsp;&nbsp;&nbsp; ├── users.csv
<br>&nbsp;&nbsp;&nbsp;&nbsp; └── words.txt

## **Contributions**

Contributions are welcome ! Feel free to open issues or submit pull requests.

## **Support the Project**

**Your support makes a huge difference !** This project is maintained with the energy, time, and passion of its contributors.
<br>If you enjoy this project or want to help sustain its development, **consider making a donation**.

### 🫶 Why Donate?

- Help cover development and hardware costs.
- Contribute to new features and improvements.
- Support an open-source project to keep it free and accessible to everyone.
- Enable the purchase of better hardware to create a computational pool for solving bitcoin puzzles.

### 🪙 Cryptocurrency Wallets

You can donate using the following cryptocurrency addresses:

- **Bitcoin (BTC)** : `bc1q6n3ufauzjqgxztkklj3734cp0f7evqq3djh4ne`
- **Ethereum (ETH)** : `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Bittensor (TAO)** : `5CrG7bKratZVocnxj66FF23AMVvqKHf7RSHfz49csEtJ2CuG`
- **Dogecoin (DOGE)** : `DJQnasX39Unat3vkmyBMgp4H6Kfd4wFumF`
- **Solana (SOL)** : `Gj9JkpFqdSabag8RiiNTmLaCiZrcxYa6pc4y599vft15`

#### **USDT (Tether)**

- **Binance Smart Chain (BEP-20)** : `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Ethereum (ERC-20)** : `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Tron (TRC-20)** : `THHcEQ8zG3ZnUXoHdBmCdpZ3AAqhoDbMpW`
- **Solana (SPL)** : `Gj9JkpFqdSabag8RiiNTmLaCiZrcxYa6pc4y599vft15`

#### **USDC (USD Coin)**

- **Binance Smart Chain (BEP-20)**: `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Ethereum (ERC-20)**: `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Solana (SPL)**: `Gj9JkpFqdSabag8RiiNTmLaCiZrcxYa6pc4y599vft15`

### 💬 A Big Thank You

Thank you so much for your generosity. Your support truly means the world to us and motivates us to keep improving this project. 🙏

**➡️ Take action now ! Every contribution, big or small, makes a huge impact.**

## Useful Links

- [CoinMonks Article](https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254)
- [Bitcoin Wallet Explorer](https://btcscan.org/address/1K4ezpLybootYF23TM4a8Y4NyP7auysnRo)

## **License**

This project is licensed under the **[MIT License](https://github.com/0x414854/Satoshi_Hunter/blob/main/LICENSE)**.

## **Author**

[**0x414854**](https://github.com/0x414854)
