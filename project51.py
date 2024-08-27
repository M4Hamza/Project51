#+-------------------------------------------------------------------------------------------------+
#| PROJECT51                            | Author: Muhamamd Amir Hamza (linkedin.com/in/mamirhamza) |
#+-------------------------------------------------------------------------------------------------+

# pip3 install requests
import requests

def main():
    ascii_logo()
    main_menu()

def ascii_logo():
    response = requests.get(f'https://drive.google.com/uc?export=download&id=1De1cjIY5HisSvRQQ_kII0-imwwTbbiW9')
    print("\n" + response.text + "\n")

def credits():
    print("\n+---------------------------------------------------------------------------+\n| AUTHOR:        Muhammad Amir Hamza (0xH4M2A)                              |\n| TITLE:         Cybersecurity Engineer                                     |\n| LINKEDIN:      https://linkedin.com/in/mamirhamza                         |\n+---------------------------------------------------------------------------+\n")
    wait()

def about():
    print("\n+---------------------------------------------------------------------------+\n| PROJECT:       Project51                                                  |\n| UPDATE:        26-08-2024                                                 |\n| LEVEL:         Novice                                                     |\n| LANGUAGE:      Python3                                                    |\n| COMPATIBLE:    Windows, Linux, Mac, UNIX                                  |\n| DESCRIPTION:   Quick tools guide for pentester with usage and detail.     |\n+---------------------------------------------------------------------------+\n")
    wait()

def main_menu():
    while True:
        print("==============[ MAIN MENU ]==============\n\n---| [1] Scanning & Enumeration\n---| [2] Brute Forcing & Cryptography\n---| [3] Stegnography\n---| [4] Vulnerability Analysis\n---| [5] Packet Analysis\n---| [6] Injection\n---| [7] Malware Analysis\n---| [8] Wireless Hacking\n---| [9] Mobile Hacking\n---| [10] IoT Hacking\n---| [CHKLS] OWASP Pentesting Check List\n---| [BONUS] Privilege Escalation\n---| [CREDS] Credits\n---| [ABOUT] About\n---| [EXIT] Exit")
        choice = input(">>>| ")
        if choice == '1':
            fileRead('1GsA1LvQCg-QUd-zdtl6PiQORZXX238MV')
        elif choice == '2':
            fileRead('1_HVUI9avGf3rlaUCVbryrtXj9Mc4KCo7')
        elif choice == '3':
            fileRead('1HppTYUsZnN12cqGD1KuXuECRdain1Vlu') 
        elif choice == '4':
            fileRead('1iqkpy3VG5Kn6X3S9VeEfTGPymYzPZj0R') 
        elif choice == '5':
            fileRead('1MAXYL2_EpVmFva7VyzKBqiwLH4yfVYQH') 
        elif choice == '6':
            fileRead('1PR2GGaAJEX3p2K_DZaJpNJdQhjKCNXMm') 
        elif choice == '7':
            fileRead('1fFc2eN3fWOeLgvzqIiD_JryqpZpTnEKb') 
        elif choice == '8':
            fileRead('1tjE31cXwT3ZJkmVmyrr-DHc3K1-UGE6c') 
        elif choice == '9':
            fileRead('15JwkUfKesQpeT6rB86UlwT9gy1UvjgfI') 
        elif choice == '10':
            fileRead('1P8RFL90bh34X_wf6MVv0xW3xmghtdNiV') 
        elif choice == 'CHKLS':
            fileRead('1jUsCG5B_kvArefCKQYx1TjkD3yLD0bBi')
        elif choice == 'BONUS':
            print("\n+------------------------------------------------------------+\n|          Premium Guide Unavailable, pay to get :)          |\n+------------------------------------------------------------+\n")
            wait()
        elif choice == 'CREDS':
            credits()
        elif choice == 'ABOUT':
            about()
        elif choice == 'EXIT':
            print("\nBYE: Exiting the program.")
            break        
        else:
            print("\n+------------------------------------------------+\n|          Correct yourself, or quit ;(          |\n+------------------------------------------------+\n")
            wait()

def fileRead(file_id):
    response = requests.get(f'https://drive.google.com/uc?export=download&id={file_id}')
    if response.status_code == 200:
        print("\n" + response.text)
        wait()
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")

def wait():
    input("Press any key to continue...")
    print("\n")

if __name__ == "__main__":
    main()