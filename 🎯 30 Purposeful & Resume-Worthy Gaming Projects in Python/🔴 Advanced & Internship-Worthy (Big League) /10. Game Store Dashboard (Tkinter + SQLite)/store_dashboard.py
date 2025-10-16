# store_dashboard.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import os, subprocess, sys

DB = 'store.db'
conn = sqlite3.connect(DB)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, name TEXT, path TEXT)''')
conn.commit()

def add_game():
    p = filedialog.askopenfilename(title="Select Executable or Script")
    if p:
        name = os.path.basename(p)
        c.execute("INSERT INTO games (name,path) VALUES (?,?)", (name,p))
        conn.commit()
        load_games()

def launch_game():
    sel = tree.selection()
    if not sel: return
    gid = tree.item(sel[0])['values'][0]
    c.execute("SELECT path FROM games WHERE id=?", (gid,))
    path = c.fetchone()[0]
    try:
        if path.endswith('.py'):
            subprocess.Popen([sys.executable, path])
        else:
            os.startfile(path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_games():
    for i in tree.get_children(): tree.delete(i)
    for row in c.execute("SELECT id,name FROM games"):
        tree.insert('', 'end', values=row)

root = tk.Tk()
root.title("Game Store Dashboard")
frame = tk.Frame(root); frame.pack()
btn = tk.Button(frame, text="Add Game", command=add_game); btn.pack(side='left')
btn2 = tk.Button(frame, text="Launch", command=launch_game); btn2.pack(side='left')
tree = ttk.Treeview(root, columns=('ID','Name'), show='headings')
tree.heading('ID', text='ID'); tree.heading('Name', text='Name')
tree.pack(fill='both', expand=True)
load_games()
root.mainloop()
conn.close()
