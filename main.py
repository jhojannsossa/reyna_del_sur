import tkinter as tk
from tkinter import ttk


class Personaje:
    def __init__(self, nombre, atributo, valor):
        self.nombre = nombre
        self.atributo = atributo
        self.valor = valor

    def entrenar(self):
        self.valor += 15
        self.mostrar_estado()

    def descansar(self):
        self.valor = max(0, self.valor - 10)
        self.mostrar_estado()

    def mostrar_estado(self):
        self.estado.config(
            text=f"{self.atributo}: {self.valor}"
        )


class TeresaMendoza(Personaje):
    def __init__(self, padre):
        super().__init__("Teresa Mendoza", "Energía", 100)
        self.crear_panel(padre, "👩🏻‍🦱", "#f8dce5")

    def crear_panel(self, padre, dibujo, color):
        self.panel = tk.Frame(padre, bg=color, padx=20, pady=15)
        self.panel.pack(side="left", padx=10, pady=10)

        tk.Label(
            self.panel, text=dibujo,
            font=("Segoe UI Emoji", 65), bg=color
        ).pack()

        tk.Label(
            self.panel, text=self.nombre,
            font=("Arial", 15, "bold"), bg=color
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
    def __init__(self, padre):
        super().__init__("Epifanio Vargas", "Fuerza", 100)
        self.crear_panel(padre, "🤠", "#d9eaff")

    def crear_panel(self, padre, dibujo, color):
        self.panel = tk.Frame(padre, bg=color, padx=20, pady=15)
        self.panel.pack(side="left", padx=10, pady=10)

        tk.Label(
            self.panel, text=dibujo,
            font=("Segoe UI Emoji", 65), bg=color
        ).pack()

        tk.Label(
            self.panel, text=self.nombre,
            font=("Arial", 15, "bold"), bg=color
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
    ventana.title("La Reina del Sur - Proyecto Python")
    ventana.geometry("600x390")
    ventana.configure(bg="#18263d")

    tk.Label(
        ventana,
        text="LA REINA DEL SUR",
        font=("Arial", 22, "bold"),
        bg="#18263d", fg="white"
    ).pack(pady=15)

    zona = tk.Frame(ventana, bg="#18263d")
    zona.pack()

    TeresaMendoza(zona)
    EpifanioVargas(zona)

    tk.Label(
        ventana,
        text="Programación Orientada a Objetos",
        bg="#18263d", fg="white",
        font=("Arial", 10)
    ).pack(pady=10)

    ventana.mainloop()