# disable_license_notice
When account disable check who have license not remove yet  
And will use Teams webhook to push  


## Screenshots
Single view
![image](https://github.com/user-attachments/assets/dcf103d9-9c81-43ba-ad10-9c89d6d3b49b)

Multi view
![image](https://github.com/user-attachments/assets/ece3dcec-9fff-4c6e-a286-e1e352545827)

## Azure Application permission
Need to create Azure Application first, please following Microsoft document to create.  
https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app

following permission:
| Type | API / Permissions name |
| :-----| :----: | 
| Application  | Directory.Read.All |
| Application  | User.Read.All |

# How to try
The script requires **Python version 3.13 or higher**.
Of course, you need to install it yourself first [Python](https://www.python.org/). On Linux, it is usually already installed. If not, install it, for example:

```console
$ sudo yum install python3
$ sudo dnf install python3
$ sudo apt install python3
$ sudo pacman -S python
```

### Installing and update dependencies
```console
$ pip install -r requirements.txt
```
## Usage
```console
$ py main.py
```
