import tkinter as tk

root = tk.Tk()

root.title("My House")
root.geometry("600x500")

canvas = tk.Canvas(
    root,
    width=600,
    height=500,
    bg="white"
)

canvas.pack()


# =========================
# NEIGHBOUR HOUSE (BEHIND)
# =========================

# Neighbour house body
canvas.create_rectangle(
    50, 180,
    250, 350,
    fill="lightgreen",
    outline="black",
    width=3
)

# Neighbour roof
canvas.create_polygon(
    30, 180,
    150, 80,
    270, 180,
    fill="gray",
    outline="black",
    width=3
)

# Neighbour left window
canvas.create_rectangle(
    75, 215,
    120, 260,
    fill="lightblue",
    outline="black",
    width=2
)

# Neighbour right window
canvas.create_rectangle(
    180, 215,
    225, 260,
    fill="lightblue",
    outline="black",
    width=2
)

# Neighbour door
canvas.create_rectangle(
    135, 270,
    175, 350,
    fill="saddlebrown",
    outline="black",
    width=2
)


# =========================
# MY HOUSE (IN FRONT)
# =========================

# House body
canvas.create_rectangle(
    150, 200,
    450, 400,
    fill="lightyellow",
    outline="black",
    width=3
)

# Roof
canvas.create_polygon(
    120, 200,
    300, 70,
    480, 200,
    fill="brown",
    outline="black",
    width=3
)

# Left window
canvas.create_rectangle(
    180, 240,
    245, 305,
    fill="lightblue",
    outline="black",
    width=3
)

# Left window divisions
canvas.create_line(
    212, 240,
    212, 305,
    width=2
)

canvas.create_line(
    180, 272,
    245, 272,
    width=2
)

# Right window
canvas.create_rectangle(
    355, 240,
    420, 305,
    fill="lightblue",
    outline="black",
    width=3
)

# Right window divisions
canvas.create_line(
    387, 240,
    387, 305,
    width=2
)

canvas.create_line(
    355, 272,
    420, 272,
    width=2
)

# Door
canvas.create_rectangle(
    270, 290,
    330, 400,
    fill="saddlebrown",
    outline="black",
    width=3
)

# Ground line
canvas.create_line(
    50, 400,
    550, 400,
    fill="black",
    width=3
)


root.mainloop()