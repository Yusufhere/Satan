import os
import shutil
import requests
import time
import random
from colorama import Fore, Style
import pyfiglet
import sys

os.system("clear")

# List of different styles for the text
styles = ['script' , 'roman', 'bubble', 'digital' , 'standard']

# Generate a random style
style = random.choice(styles)

# Create the logo with the chosen style
logo = pyfiglet.figlet_format("TG RuLex", font=style)

# Print the logo with neon colors
for char in logo:
    print(Fore.MAGENTA + char, end='', flush=True)
time.sleep(0.5)
print(Style.RESET_ALL)

hater_name = input(Fore.YELLOW + "꧁.💕▄︻デɦǟȶɛʀֆ ռǟʍɛ══━一💖.꧂: ").strip()
print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)

hero_name = input(Fore.YELLOW + "꧁.💕❀💋 ᕼEᖇO ᑎᗩᗰE 💋❀💖.꧂: ").strip()
print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)

def custom_font(text):
    font_map = {
        'A': '𝘼', 'B': '𝘽', 'C': '𝘾', 'D': '𝘿', 'E': '𝙀',
        'F': '𝙁', 'G': '𝙂', 'H': '𝙃', 'I': '𝙄', 'J': '𝙅',
        'K': '𝙆', 'L': '𝙇', 'M': '𝙈', 'N': '𝙉', 'O': '𝙊',
        'P': '𝙋', 'Q': '𝙌', 'R': '𝙍', 'S': '𝙎', 'T': '𝙏',
        'U': '𝙐', 'V': '𝙑', 'W': '𝙒', 'X': '𝙓', 'Y': '𝙔',
        'Z': '𝙕',
        'a': '𝙖', 'b': '𝙗', 'c': '𝙘', 'd': '𝙙', 'e': '𝙚',
        'f': '𝙛', 'g': '𝙜', 'h': '𝙝', 'i': '𝙞', 'j': '𝙟',
        'k': '𝙠', 'l': '𝙡', 'm': '𝙢', 'n': '𝙣', 'o': '𝙤',
        'p': '𝙥', 'q': '𝙦', 'r': '𝙧', 's': '𝙨', 't': '𝙩',
        'u': '𝙪', 'v': '𝙫', 'w': '𝙬', 'x': '𝙭', 'y': '𝙮',
        'z': '𝙯'
    }
    return ''.join(font_map.get(char, char) for char in text)

hater_name_stylish = custom_font(hater_name)
hero_name_stylish = custom_font(hero_name)

def edit_hn_file(hero_name, hater_name):
    myhn_file_path = None
    possible_paths = [
        os.path.join(os.path.expanduser("~"), "TGTOOL", "HN", "MYHN.txt"),
        os.path.join("/storage/emulated/0/TGTOOL/HN", "MYHN.txt"),
        os.path.join("/storage/sdcard0/TGTOOL/HN", "MYHN.txt")
    ]

    for path in possible_paths:
        if os.path.exists(path):
            myhn_file_path = path
            break

    if myhn_file_path:
        duplicate_file_path = myhn_file_path.replace("MYHN.txt", "MYHN_duplicate.txt")
        try:
            shutil.copy(myhn_file_path, duplicate_file_path)
        except Exception as e:
            print(f"[x]  𝐄𝐫𝐫𝐨𝐫 𝐜𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐝𝐮𝐩𝐥𝐢𝐜𝐚𝐭𝐞 𝐟𝐢𝐥𝐞 ʕʘ̅͜ʘ̅ʔ: {e}")
            return

        try:
            with open(duplicate_file_path, 'r') as file:
                content = file.read()
        except Exception as e:
            print(f"[x] 𝕰𝖗𝖗𝖔𝖗 𝖗𝖊𝖆𝖉𝖎𝖓𝖌 𝖉𝖚𝖕𝖑𝖎𝖈𝖆𝖙𝖊 𝖋𝖎𝖑𝖊✍: {e}")
            return

        content = content.replace("{server_runner}", hero_name_stylish)
        content = content.replace("{hater_name}", hater_name_stylish)

        legend_file_path = os.path.join(os.path.dirname(myhn_file_path), "LEGENDHN.txt")
        
        if os.path.exists(legend_file_path):
            try:
                os.remove(legend_file_path)
                print(f"[+]  𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐞𝐱𝐢𝐬𝐭𝐢𝐧𝐠 LEGENDHN.txt ʕʘ̅͜ʘ̅ʔ: {legend_file_path}")
            except Exception as e:
                print(f"[x]  𝐄𝐫𝐫𝐨𝐫 𝐝𝐞𝐥𝐞𝐭𝐢𝐧𝐠 𝐞𝐱𝐢𝐬𝐭𝐢𝐧𝐠 LEGENDHN.txt ʕʘ̅͜ʘ̅ʔ: {e}")

        try:
            with open(legend_file_path, 'w') as new_file:
                new_file.write(content)
            print(f"[+] ಠ_ಠ ηєω ƒιℓє ¢яєαтє∂: {legend_file_path} ")
        except Exception as e:
            print(f"[x]  𝐄𝐫𝐫𝐨𝐫 𝐰𝐫𝐢𝐭𝐢𝐧𝐠 𝐧𝐞𝐰 LEGENDHN.txt: ʕʘ̅͜ʘ̅ʔ: {e}")

        try:
            os.remove(duplicate_file_path)
            print(f"[+]  𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐝𝐮𝐩𝐥𝐢𝐜𝐚𝐭𝐞 𝐟𝐢𝐥𝐞: {duplicate_file_path} ʕʘ̅͜ʘ̅ʔ")
        except Exception as e:
            print(f"[x]  𝙴𝚛𝚛𝚘𝚛 𝚍𝚎𝚕𝚎𝚝𝚒𝚗𝚐 𝚍𝚞𝚙𝚕𝚒𝚌𝚊𝚝𝚎 𝚏𝚒𝚕𝚎 ◔_◔: {e}")
    else:
        print("[x]  𝐌𝐘𝐇𝐍.𝐭𝐱𝐭 𝐟𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝 ʕʘ̅͜ʘ̅ʔ.")

edit_hn_file(hero_name_stylish, hater_name_stylish)

input(Fore.YELLOW + "❂𐂷 ꝒⱤƸⳜⳜ ƸƝƬƸⱤ ƬⰙ ƓⰙ ƬⰙ ƬǶƸ 𐒄𐤠ƖƝ ⳜƇⱤƖꝒƬ... (⁠ʃ⁠ƪ⁠＾⁠3⁠＾⁠）")

os.system('clear')

def send_message(token, message, target_id, message_index, token_index):
    url = f"https://graph.facebook.com/v17.0/t_{target_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "www.google.com",
    }
    parameters = {
        "to": {"id": target_id},
        "message": message
    }
    
    try:
        response = requests.post(url, json=parameters, headers=headers)
        response.raise_for_status()
        current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
        logos = [
            " ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა♡꧁ད รєгשєг เร ๏ภ ཌ꧂",
            "彡(✿╹◡╹) 𝘉𝘢𝘯𝘨𝘪𝘯𝘨 𝘏𝘢𝘵𝘦𝘳𝘴 (｀∀´)Ψ",
            "(❁˃́ᴗ˂̀)(≧ᴗ≦✿)♡ ⎝⎝✧𝐓𝐆 𝐓𝐎𝐎𝐋✧⎠⎠ ♡ღ´͈ ᵕ `͈ )",
            "(˶ᵔ ᵕ ᵔ˶) F⋆u⋆c⋆k⋆i⋆n⋆g⋆ ⋆b⋆i⋆t⋆c⋆h⋆e⋆s◝(ᵔᗜᵔ)◜⋆˚✿˖°"
        ]
        current_logo = random.choice(logos)
        print(Fore.BLUE + "<---------------------------------------------------->" + Style.RESET_ALL)
        print(Fore.MAGENTA + current_logo)
        print(Fore.BLUE + "<---------------------------------------------------->" + Style.RESET_ALL)
        print_with_animation(Fore.YELLOW + f"┋↝───────────────·········⋆༺𓆩❀𓆪༻⋆·········───────────────↜┋\n"
          "┋┋┈➤✦《 ┈➤✦《 「꧁༒☠💥✨𝐀𝐓𝐓𝐀𝐂𝐊𝐈𝐍𝐆 𝟎𝐍 𝐓𝐀𝐑𝐆𝐄𝐓✨💥☠༒꧂」 \n"
          "┋↝───────────────·········⋆༺𓆩❀𓆪༻⋆·········───────────────↜┋\n"
          f"┋┋┈➤✦《 ┈➤✦《 MΣƧƧΛGΣ ᔕEᑎT ૮₍ ˶•⤙•˶ ₎ა {message_index + 1}✦》✓」\n"
          "┋↝───────────────·········⋆༺𓆩❀𓆪༻⋆·········───────────────↜┋\n"
          f"┋┋┈➤✦《 ᗯITᕼ TOKEᑎ {token_index + 1}✦》✓」\n"
          "┋↝───────────────·········⋆༺𓆩❀𓆪༻⋆·········───────────────↜┋\n"
          f"┋┋┈➤✦《 at {current_time} ✦》✓✓」\n"
          "┋↝───────────────·········⋆༺𓆩❀𓆪༻⋆·········───────────────↜┋\n")
    except requests.exceptions.RequestException as e:
        print_with_animation(Fore.RED + f"[x] ( ,,⩌'︿'⩌,,)ᖴᗩIᒪEᗖ TO ᔕEᑎᗪ ᗰEᔕᔕᗩGE TO ᑕOᑎᐯEᖇᔕᗩTIOᑎ {target_id} ᗯITᕼ TOKEᑎ {token}:- Error: {e}")

def print_with_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def approval():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)

banner = """
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
               💣𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 𝙈𝙀𝙎𝙎𝘼𝙂𝙀 𝘽𝙊𝙈𝘽𝙀𝙍💣
                    💻𝙑𝙀𝙍𝙎𝙄𝙊𝙉 3.0💻
                   👑𝘼𝙐𝙏𝙃𝙊𝙍 {𝙔𝙐𝙎𝙐𝙁}👑
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN]
print(Fore.MAGENTA + "\U0001F600" + " Thank you!")
for line in banner.split('\n'):
    for i, char in enumerate(line):
        print(colors[i % len(colors)] + char, end='', flush=True)
    print()
print(Fore.RESET)

def get_file_selection(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    for index, file in enumerate(files):
        print(f"{index + 1}. {file}")
    while True:
        try:
            selection = int(input(Fore.YELLOW + "Please select a file by number: ")) - 1
            if 0 <= selection < len(files):
                return os.path.join(folder_path, files[selection])
            else:
                print(Fore.RED + "Invalid selection, please enter to try again.")
        except ValueError:
            print(Fore.RED + "Invalid input, please enter a number.")

def main():
    print_with_animation("\033[38;5;201mWELCOME \033[38;5;196mTO \033[38;5;202mYUSUF \033[38;5;226mMESSAGE \033[0m \033[38;5;201mBOMBER \033[38;5;196mTOOL \033[38;5;202mENJOY \033[0m")
    print(Fore.CYAN + "-------------------------------------------------->")
    print_with_animation(Fore.YELLOW + f" ╰┈➤✦ᑭᒪEᗩᔕE ᔕEᒪEᑕT ᗩ TOKEᑎ ᖴIᒪE (ಠ‿ಠ)" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    tokens_file = get_file_selection('/storage/emulated/0/TGTOOL/TK')
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    
    target_id = input(Fore.YELLOW + "🔥(✖EᑎTEᖇ TᗩᖇGET Iᗭ✖)🔥: ").strip()
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    print_with_animation(Fore.YELLOW + f" ╰┈➤✦ ᑭᒪEᗩᔕE ᔕEᒪEᑕT ᗩ ᗰEᔕᔕᗩGE ᖴIᒪE (ಠ‿ಠ)" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    messages_file = get_file_selection('/storage/emulated/0/TGTOOL/NP')
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    print_with_animation(Fore.YELLOW + f" ╰┈➤✦ ᑭᒪEᗩᔕE ᔕEᒪEᑕT ᗩ ᕼᗩTEᖇᔕ ᑎᗩᗰE ᖴIᒪE (ಠ‿ಠ)" + Style.RESET_ALL)
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    haters_file = get_file_selection('/storage/emulated/0/TGTOOL/HN')
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)
    speed = float(input(Fore.YELLOW + "꧁༒☠💥✨EᑎTEᖇ ᔕᑭEEᗪ✨💥☠༒꧂: ").strip())
    print(Fore.YELLOW + "<---------------------------------------------------->" + Style.RESET_ALL)

    try:
        with open(tokens_file, 'r') as f:
            tokens = f.readlines()
        with open(messages_file, 'r') as f:
            messages = f.readlines()
        with open(haters_file, 'r') as f:
            haters_names = f.readlines()
    except FileNotFoundError as e:
        print(Fore.RED + f"[x] Error: {e}")
        return

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            token = tokens[token_index].strip()
            haters_name = haters_names[message_index % len(haters_names)].strip()
            full_message = f"{haters_name} {message.strip()}"
            send_message(token, full_message, target_id, message_index, token_index)
            time.sleep(speed)
        print(Fore.CYAN + "\n[+] ✎ (❁ᴗ͈ˬᴗ͈) ༉‧ 『R』『E』『S』『T』『A』『R』『T』『I』『N』『G』 ♡*.✧...\n")

if __name__ == "__main__":
    main()
