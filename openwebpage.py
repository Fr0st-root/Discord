import webbrowser


print('Hello discord! Today we are going to open a webbrowser from a remote server using a backdoor.')
site = 'https://www.tedcruzforhumanpresident.com/'
webbrowser.get('chrome').open_new(site)