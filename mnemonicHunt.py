import base58
import binascii
import bip32utils
import codecs
import csv
import logging
import os
import random
import time
from bit import Key
from bit.format import bytes_to_wif
from concurrent.futures import ThreadPoolExecutor, as_completed
from mnemonic import Mnemonic
from shadePy import Colors


GREEN, RED, BLUE, CYAN, BRIGHT_GREY, YELLOW, RESET = (
    Colors.GREEN, Colors.RED, Colors.BLUE, Colors.CYAN,
    Colors.BRIGHTGREY, Colors.YELLOW, Colors.RESET
)

title = f"""{YELLOW}
 __  __                                        _       
|  \/  | _ __    ___  _ __ ___    ___   _ __  (_)  ___ 
| |\/| || '_ \  / _ \| '_  _  \  / _ \ | '_ \ | | / __|
| |  | || | | ||  __/| | | | | || (_) || | | || || (__ 
|_|  |_||_| |_| \___||_| |_| |_| \___/ |_| |_||_| \___|
| | | | _   _  _ __  | |_                              
| |_| || | | || '_ \ | __|                             
|  _  || |_| || | | || |_           {RESET} by {CYAN}CoinMonks{RESET}                             
{YELLOW}|_| |_| \__,_||_| |_| \__|          {RESET} Powered by {BLUE}0x414854{RESET}                                  
                                            
"""

WORDS_FILE = './utils/words.txt'
USER_FILE = './utils/users.csv'
RESULT_DIR = './Results/'
LOGS_DIR = './logs'
LOG_FILE = os.path.join(LOGS_DIR, 'mnemonicHunt.log')
MNEMONIC_FILE = './utils/mnemonic.txt'
RESULT_FILE = './utils/Enjoy.txt'

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def getClear():
    os.system("cls" if os.name == 'nt' else "clear")

def load_license_keys():
    with open(USER_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return {row[1] for row in reader}

def authenticate(license_key, valid_keys):
    return license_key in valid_keys

def authentication(valid_keys):
    login_attempts = 0  
    choice = input(f"{YELLOW}[1]{RESET} : Login\n\n{YELLOW}[2]{RESET} : Exit\n\n")
    if choice == '1':
        getClear()
        license_key = input(f"{BRIGHT_GREY}Enter license key : {RESET}")
        print(f"{YELLOW}Verifying informations...Please wait{RESET}")
        time.sleep(1)
        if authenticate(license_key, valid_keys):
            print(f"{GREEN}Authentication successful!{RESET}")
            logging.info("Authentication successful")
            time.sleep(2)
            getClear()
            return True
        else:
            print(f"{RED}Error: Authentication failed. Invalid license key.{RESET}")
            logging.warning("Authentication failed for license key")
            login_attempts += 1
            time.sleep(2)
            getClear()
            print(title)

            if login_attempts == 3:
                time.sleep(1)
                print(f"{RED}Error: Maximum login attempts reached.\nExiting program.{RESET}\n{YELLOW}Please contact support on Discord if needed.{RESET}")
                logging.error("Maximum login attempts reached")
                exit()
            else:
                return False
    elif choice == '2': 
        print("See you soon !")
        logging.info("Program exited by user")
        exit()
    else: 
        print(f"{RED}Error: Incorrect choice. Please enter '1' to Log in or '2' to Exit.{RESET}")

with open(WORDS_FILE, 'r') as file:
    WORDS = file.read().splitlines()

def load_generated_mnemonics():
    generated_mnemonics = set()
    if os.path.exists(MNEMONIC_FILE):
        with open(MNEMONIC_FILE, "r", buffering=100000) as file:
            for count, line in enumerate(file):
                generated_mnemonics.add(line.strip())
                if count % 100 == 0:
                    print(f"{YELLOW}Loading mnemonics{RESET} : {count} iterations", end='\r')
            logging.info(f"Total mnemonics loaded : {count}")
            print(f"\nTotal mnemonics loaded : {GREEN}{count}{RESET}")
    return generated_mnemonics

def GetUniqueMnemonic(len_seed, generated_mnemonics):
    while True:
        mnemonic = ' '.join(random.sample(WORDS, len_seed))
        if mnemonic not in generated_mnemonics:
            generated_mnemonics.add(mnemonic)
            return mnemonic

def save_mnemonic_to_file(mnemonic):
    with open(MNEMONIC_FILE, "a") as file:
        file.write(f"{mnemonic}\n")


def PrivateKeyFromMnemonic(mnemonic):
    mne = Mnemonic("english")
    seed = mne.to_seed(mnemonic, passphrase="")
    Bip32_Root_Key_Object = bip32utils.BIP32Key.fromEntropy(seed)
    Bip32_Child_Key_Object = Bip32_Root_Key_Object.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(
        0 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(0)
    first_encode = base58.b58decode(Bip32_Child_Key_Object.WalletImportFormat())
    private_key_byte = binascii.hexlify(first_encode)
    private_key_hex = private_key_byte[2:-10]
    private_hex = private_key_hex.decode()
    byte_private = codecs.decode(private_hex, 'hex_codec')
    wif_compressed = bytes_to_wif(byte_private, compressed=True)
    wif_uncompressed = bytes_to_wif(byte_private, compressed=False)
    bit_com = Key(wif_compressed)
    bit_uncom = Key(wif_uncompressed)
    compressed_address = bit_com.address
    uncompressed_address = bit_uncom.address

    return compressed_address, uncompressed_address, private_hex

def save_results_to_file(mnemonic, private_key, address):
    with open(RESULT_FILE, "a") as file:
        file.write(f"Mnemonic : {mnemonic}\n")
        file.write(f"Private Key : {private_key}\n")
        file.write(f"Address : {address}\n\n")
    print(f"\n{GREEN}Wallet saved{RESET} in the file '{GREEN}Enjoy.txt{RESET}'")
    logging.info("Wallet saved to Enjoy.txt")

def search_for_target_address(len_seed, generated_mnemonics, display_attempts):
    target_address = '1K4ezpLybootYF23TM4a8Y4NyP7auysnRo'
    count = 0
    while True:
        mnemonic = GetUniqueMnemonic(len_seed, generated_mnemonics)
        compressedAddress, uncompressedAddress, private_key = PrivateKeyFromMnemonic(mnemonic)
        
        if target_address in (compressedAddress, uncompressedAddress):
            print(f"{GREEN}Target Address found !{RESET}")
            save_results_to_file(mnemonic, private_key, compressedAddress)
            logging.info("Target address found")
            return True

        if display_attempts:
            print(f"{RED}{mnemonic}{RESET}")
        else:
            if count % 1000 == 0:
                print(f"\n{BRIGHT_GREY}Generated Mnemonic {YELLOW}{count}{RESET}...", end='\r')
            if count % 1000000 == 0:
                logging.info(f"{count} generated mnemonic")

        save_mnemonic_to_file(mnemonic)
        count += 1

def parallel_search(generated_mnemonics, len_seeds, display_attempts):
    with ThreadPoolExecutor(max_workers=len(len_seeds) * 4) as executor:
        futures = [executor.submit(search_for_target_address, len_seed, generated_mnemonics, display_attempts) for len_seed in len_seeds]
        for future in as_completed(futures):
            if future.result():
                executor.shutdown(wait=False)
                break

def main():
    print(title)
    valid_keys = load_license_keys()
    authenticated = False
    while not authenticated:
        authenticated = authentication(valid_keys)
        
    generated_mnemonics = load_generated_mnemonics()
    display_attempts = input(f"{BRIGHT_GREY}Display each attempt? (y/n) : {RESET}").lower() == 'y'
    print(f"{YELLOW}The search will begin...{RESET}")
    len_seeds = [12, 24]
    parallel_search(generated_mnemonics, len_seeds, display_attempts)

if __name__ == "__main__":
    main()
 