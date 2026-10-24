import tkinter as tk
from tkinter import ttk
from pathlib import Path
from PIL import Image, ImageTk

class Personaje:
    def __init__(self, nombre, atributo, valor):
        self.nombre = nombre
        self.atributo = atributo
        self.valor = valor

    def entrenar(self):
        self.valor += 15
        self.actualizar_estado()

    def descansar(self):
        self.valor = max(0, self.valor - 10)
        self.actualizar_estado()

    def actualizar_estado(self):
        self.estado.config(
            text=f"{self.atributo}: {self.valor}"
        )


class TeresaMendoza(Personaje):
    def __init__(self, ventana):
        super().__init__("Teresa Mendoza", "Energía", 100)
        self.crear_panel(ventana, "👩🏻‍🦱", "#f8dce5")

    def crear_panel(self, ventana, dibujo, color):
        self.panel = tk.Frame(ventana, bg=color, padx=20, pady=15)
        self.panel.pack(side="left", padx=10, pady=10)

        ruta = Path(__file__).parent / "imagenes" / "teresa.jpg"

        imagen = Image.open(ruta)
        imagen.thumbnail((180, 200))

        self.foto = ImageTk.PhotoImage(imagen)

        tk.Label(
            self.panel,
            image=self.foto,
            bg=color
        ).pack()

        self.estado = tk.Label(
            self.panel, text="Energía: 100",
            font=("Arial", 12), bg=color
        )
        self.estado.pack(pady=10)

        ttk.Button(
            self.panel, text="Entrenar",
            command=self.entrenar
        ).pack(fill="x", pady=3)

        ttk.Button(
            self.panel, text="Descansar",
            command=self.descansar
        ).pack(fill="x", pady=3)


class EpifanioVargas(Personaje):
    def __init__(self, ventana):
        super().__init__("Epifanio Vargas", "Fuerza", 100)
        self.crear_panel(ventana, "🤠", "#d9eaff")

    def crear_panel(self, ventana, dibujo, color):
        self.panel = tk.Frame(ventana, bg=color, padx=20, pady=15)
        self.panel.pack(side="left", padx=10, pady=10)

        ruta = Path(__file__).parent / "imagenes" / "epifanio.jpg"

        imagen = Image.open(ruta)
        imagen.thumbnail((180, 200))

        self.foto = ImageTk.PhotoImage(imagen)

        tk.Label(
            self.panel,
            image=self.foto,
            bg=color
        ).pack()

        self.estado = tk.Label(
            self.panel, text="Fuerza: 100",
            font=("Arial", 12), bg=color
        )
        self.estado.pack(pady=10)

        ttk.Button(
            self.panel, text="Entrenar",
            command=self.entrenar
        ).pack(fill="x", pady=3)

        ttk.Button(
            self.panel, text="Descansar",
            command=self.descansar
        ).pack(fill="x", pady=3)


def main():
    ventana = tk.Tk()
    ventana.title("La Reina del Sur")
    ventana.geometry("600x360")
    ventana.configure(bg="#18263d")

    tk.Label(
        ventana, text="LA REINA DEL SUR",
        font=("Arial", 22, "bold"),
        bg="#18263d", fg="white"
    ).pack(pady=15)

    personajes = tk.Frame(ventana, bg="#18263d")
    personajes.pack()

    TeresaMendoza(personajes)
    EpifanioVargas(personajes)

    tk.Label(
        ventana, text="Programación Orientada a Objetos",
        bg="#18263d", fg="white"
    ).pack(pady=8)

    ventana.mainloop()


if __name__ == "__main__":
    main()
