import os
import time
import sys

red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
white = "\033[1;37;40m"
cyan = "\033[1;36;40m"


def select_distro():
	os.system('clear')
	print(f"{red} [{white}-{red}] {cyan}Select Distro...\n")
	time.sleep(0.5)

	print(f" {green} 1. {yellow}Ubuntu 18.04")
	print(f" {green} 2. {yellow}Ubuntu 20.04")
	print(f" {green} 3. {yellow}Kali")
	print(f" {green} 4. {yellow}Debian")
	print(f" {green} 5. {yellow}Arch")
	print(f" {green} 6. {yellow}Manjaro")
	print(f" {green} 7. {yellow}Fedora")
	print(f" {green} 8. {yellow}Void")
	print(f" {green} 9. {yellow}Alpine")

def distro_process():
	## distro commands
	ubuntu18 = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu/ubuntu-xfce.sh | bash" 
	ubuntu20 = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-xfce.sh | bash"
	kali = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-xfce.sh | bash"
	debian = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh | bash"
	arch = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-xfce.sh | bash"
	manjaro = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-xfce.sh | bash"
	fedora = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-xfce.sh | bash"
	void = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-xfce.sh | bash"
	alpine = "apt update -y && apt install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpinexfce.sh | bash"

	try:
		user_input_expt = input(f"\n {red}[{white}-{red}] {white} Enter distro : ")
	except KeyboardInterrupt:
		print(f"\n\n {red}[{white}-{red}] {red} Process cancled by user...\n")
		sys.exit()
	user_input = str(user_input_expt)

	if user_input == '1':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Ubuntu 18.04 downloading has started... \n")
		os.system(ubuntu18)
	elif user_input == 'ubuntu 18.04':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Ubuntu 18.04 downloading has started... \n")
		os.system(ubuntu18)
	elif user_input == 'ubuntu18':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Ubuntu 18.04 downloading has started... \n")
		os.system(ubuntu18)

	elif user_input == '2':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Ubuntu 20.04 downloading has started... \n")
		os.system(ubuntu20)
	elif user_input == 'ubuntu 20.04':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Ubuntu 20.04 downloading has started... \n")
		os.system(ubuntu20)
	elif user_input == 'ubuntu20':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Ubuntu 20.04 downloading has started... \n")
		os.system(ubuntu20)

	elif user_input == '3':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Kali linux downloading has started... \n")
		os.system(kali)
	elif user_input == 'kali':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Kali linux downloading has started... \n")
		os.system(kali)

	elif user_input == '4':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Debian linux downloading has started... \n")
		os.system(debian)
	elif user_input == 'debian':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Debian linux downloading has started... \n")
		os.system(debian)

	elif user_input == '5':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Arch linux downloading has started... \n")
		os.system(arch)
	elif user_input == 'arch':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Arch linux downloading has started... \n")
		os.system(arch)

	elif user_input == '6':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Manjaro linux downloading has started... \n")
		os.system(manjaro)
	elif user_input == 'manjaro':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Manjaro linux downloading has started... \n")
		os.system(manjaro)

	elif user_input == '7':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Fedora linux downloading has started... \n")
		os.system(fedora)	
	elif user_input == 'fedora':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Fedora linux downloading has started... \n")
		os.system(fedora)

	elif user_input == '8':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Void linux downloading has started... \n")
		os.system(void)
	elif user_input == 'void':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Void linux downloading has started... \n")
		os.system(void)	

	elif user_input == '9':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Alpine linux downloading has started... \n")
		os.system(alpine)
	elif user_input == 'alpine':
		os.system('clear')
		print(f"{red}[{white}-{red}] {cyan} Alpine linux downloading has started... \n")
		os.system(alpine)

	else:
		print(f'{red}[{white}-{red}] {red}Wrong input... \n')
	
	file_setup(user_input)

def file_setup(user_input):
	
	if user_input == '1':
		os.system('mv inner_setup.sh ubuntu-fs/root')
	elif user_input == 'ubuntu 18.04':
		os.system('mv inner_setup.sh ubuntu-fs/root')
	elif user_input == 'ubuntu18':
		os.system('mv inner_setup.sh ubuntu-fs/root')

	elif user_input == '2':
		os.system('mv inner_setup.sh ubuntu20-fs/root')
	elif user_input == 'ubuntu 20.04':
		os.system('mv inner_setup.sh ubuntu20-fs/root')
	elif user_input == 'ubuntu20':
		os.system('mv inner_setup.sh ubuntu20-fs/root')

	elif user_input == '3':
		os.system('mv inner_setup.sh kali-fs/root')
	elif user_input == 'kali':
		os.system('mv inner_setup.sh -fs/root')

	elif user_input == '4':
		os.system('mv inner_setup.sh debian-fs/root')
	elif user_input == 'debian':
		os.system('mv inner_setup.sh debian-fs/root')

	elif user_input == '5':
		os.system('mv inner_setup.sh arch-fs/root')
	elif user_input == 'arch':
		os.system('mv inner_setup.sh arch-fs/root')

	elif user_input == '6':
		os.system('mv inner_setup.sh manjaro-fs/root')
	elif user_input == 'manjaro':
		os.system('mv inner_setup.sh manjaro-fs/root')

	elif user_input == '7':
		os.system('mv inner_setup.sh fedora-fs/root')	
	elif user_input == 'fedora':
		os.system('mv inner_setup.sh fedora-fs/root')

	elif user_input == '8':
		os.system('mv inner_setup.sh void-fs/root')
	elif user_input == 'void':
		os.system('mv inner_setup.sh void-fs/root')	

	elif user_input == '9':
		os.system('mv inner_setup.sh alpine-fs/root')
	elif user_input == 'alpine':
		os.system('mv inner_setup.sh alpine-fs/root')

	else:
		print(f'{red}[{white}-{red}] {red}File transfer faill...')	

def call_file():
	os.system('bash sound_setup.sh')

select_distro()
distro_process()
call_file()