import tkinter as tk
import requests
import os

def download_music():
    song_id = entry.get()
    url = "http://v.api.aa1.cn/api/wymusic/index.php?id=" + song_id
    response = requests.get(url)
    
    if response.status_code == 200:
        save_path = os.path.expanduser("~/Desktop/music.mp3")
        with open(save_path, "wb") as file:
            file.write(response.content)
        print("音频文件下载成功！保存路径：", save_path)
    else:
        print("音频文件下载失败！")

window = tk.Tk()
window.title("NCM Music Download")
window.geometry("380x240")

label = tk.Label(window, text="请输入歌曲ID", justify="center")
label.pack(pady=10)

entry = tk.Entry(window, justify="center")
entry.pack(pady=10)

button = tk.Button(window, text="开始下载", command=download_music)
button.pack(pady=10)

label2 = tk.Label(window, text="By 桀皮 | All In One", justify="center")
label2.pack(pady=10)

window.mainloop()