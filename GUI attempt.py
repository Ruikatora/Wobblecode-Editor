import tkinter as tk
import tkinter.ttk as ttk

def createFrame(labelText, tabParent):
    frame = tk.Frame(tabParent)

    label = tk.Label(master=frame)
    label.pack()
    tabParent.add(frame, text=labelText)
    #frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)

window = tk.Tk()
window.title("Wobblecode Editor")

tabSystem = ttk.Notebook(window)

mainFrame = tk.Frame()

bodyFrame = createFrame("Body", tabSystem)
legFrame = createFrame("Legs", tabSystem)
headFrame = createFrame("Head", tabSystem)
snoutFrame = createFrame("Snout", tabSystem)
noseFrame = createFrame("Nose", tabSystem)
earFrame = createFrame("Ears", tabSystem)
wingFrame = createFrame("Wings", tabSystem)
patternFrame = createFrame("Pattern", tabSystem)
voiceFrame = createFrame("Voice", tabSystem)
iFrame = createFrame("Eyes", tabSystem)
tailFrame = createFrame("Tail", tabSystem)
hornyFrame = createFrame("Horns", tabSystem)
mouthFrame = createFrame("Mouth", tabSystem)


tabSystem.pack()
window.mainloop()