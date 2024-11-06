import tkinter as tk 

# ------------------------------------------------------
# Funciones:
# ------------------------------------------------------

def cerrarVentana():
    """Cierra la ventana principal."""
    vn.destroy()

# ------------------------------------------------------
# Inicio:
# ------------------------------------------------------

def Inicio():
    nav.pack(fill="x")
    bordeInf.pack(fill="x", pady=(0, 5))
    instr.pack(fill="x")
    menu.pack(side="top")
    footer.pack(fill="x", pady=(15, 0))

def ocultarInicio():
    nav.pack_forget()
    bordeInf.pack_forget()
    instr.pack_forget()
    menu.pack_forget()
    footer.pack_forget()
# ------------------------------------------------------
# Navegador Secciones:
# ------------------------------------------------------

def navegadorEntreSecciones():
    nav2.pack(fill="x")
    bordeInf.pack(fill="x", pady=(0, 5))

def ocultarNavegadorEntreSecciones():
    nav2.pack_forget()
    bordeInf.pack_forget()
# ------------------------------------------------------
# Agregar Termino:
# ------------------------------------------------------

def seccionAgregarTermino():
    ocultarInicio()
    navegadorEntreSecciones()
    agregarTermino.pack(fill="both")

def ocultarSeccionAgregarTermino():
    ocultarNavegadorEntreSecciones()
    agregarTermino.pack_forget()

# ------------------------------------------------------
# Eliminar Termino:
# ------------------------------------------------------

def seccionEliminarTermino():
    ocultarInicio()
    navegadorEntreSecciones()
    eliminarTermino.pack(fill="both")

def ocultarSeccionEliminarTermino():
    ocultarNavegadorEntreSecciones()
    eliminarTermino.pack_forget()

# ------------------------------------------------------
# Buscar Termino:
# ------------------------------------------------------

def seccionBuscarTermino():
    ocultarInicio()
    navegadorEntreSecciones()
    buscarTermino.pack(fill="both")

def ocultarSeccionBuscarTermino():
    ocultarNavegadorEntreSecciones()
    buscarTermino.pack_forget()

# ------------------------------------------------------
# listar Termino:
# ------------------------------------------------------

def seccionListarTermino():
    ocultarInicio()
    navegadorEntreSecciones()
    listarTermino.pack(fill="both")

def ocultarSeccionListarTermino():
    ocultarNavegadorEntreSecciones()
    listarTermino.pack_forget()

# ------------------------------------------------------
# listar Termino:
# ------------------------------------------------------

def seccionAcercaDe():
    ocultarInicio()
    navegadorEntreSecciones()
    acercaDe.pack(fill="both")

def ocultarSeccionAcercaDe():
    ocultarNavegadorEntreSecciones()
    acercaDe.pack_forget()


# ------------------------------------------------------
# Volver:
# ------------------------------------------------------

def volver():
    """Vuelve al menú principal ocultando otras secciones."""
    ocultarSeccionAgregarTermino()
    ocultarSeccionEliminarTermino()
    ocultarSeccionBuscarTermino()
    Inicio()

    


# ------------------------------------------------------
# Configuración de la ventana principal
# ------------------------------------------------------

vn = tk.Tk()
vn.configure(bg="#F2F2F2")
vn.geometry("600x420")
vn.resizable(False, False)
vn.title("Diccionario del Programador")
vn.iconbitmap("ui\img\diccionarioimg.ico")


# ------------------------------------------------------
# Barra de navegación Inicio
# ------------------------------------------------------

nav = tk.Frame(vn, bg="#1B1259", width=600, height=42)

lbnav = tk.Label(
    nav, text="Diccionario Del Programador",
    font=("Roboto", 22, "bold"), fg="#F2F2F2", bg="#1B1259"
)
lbnav.pack(side="top")

# Borde inferior de la barra de navegación
bordeInf = tk.Frame(vn, height=2, bg="#d91f2b")

# ------------------------------------------------------
# Sección de Instrucciones
# ------------------------------------------------------

instr = tk.Frame(vn, height=67)

lbInstr = tk.Label(
    instr, text="Ingresa una Opción:", 
    font=("Roboto", 16, "bold"), fg="#201161"
)
lbInstr.pack(side="top", anchor="s", pady=15)


# ------------------------------------------------------
# Menú principal
# ------------------------------------------------------

menu = tk.Frame(vn, width=270, height=220, bg="#1B1259")

btnAgregarT = tk.Button(
    menu, text="Agregar Término", bg="#F2B705", fg="#F2F2F2",
    font=("Roboto", 12, "bold"), command=seccionAgregarTermino
)
btnAgregarT.pack(fill="both", expand=True, padx=60, pady=10)

btnEliminarT = tk.Button(
    menu, text="Eliminar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"),command=seccionEliminarTermino
)
btnEliminarT.pack(fill="both", expand=True, padx=60, pady=11)

btnBuscarT = tk.Button(
    menu, text="Buscar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"),command=seccionBuscarTermino
)
btnBuscarT.pack(fill="both", expand=True, padx=60, pady=11)

btnListarT = tk.Button(
    menu, text="Listar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"),command=seccionListarTermino
)
btnListarT.pack(fill="both", expand=True, padx=60, pady=11)

# ------------------------------------------------------
# Footer
# ------------------------------------------------------

footer = tk.Frame(vn)

btnAcercaDe = tk.Button(
    footer, text="Acerca De", bg="#d91f2b", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"),command=seccionAcercaDe
)
btnAcercaDe.pack(pady=10, padx=15, side="right")

btnSalir = tk.Button(
    footer, text="Salir", bg="#d91f2b", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=cerrarVentana
)
btnSalir.pack(pady=10, padx=15, side="left")

# ------------------------------------------------------
# Barra de navegación secundaria  (para secciones internas)
# ------------------------------------------------------

nav2 = tk.Frame(vn, bg="#1B1259", width=600, height=42)

lbnav2 = tk.Label(
    nav2, text="Diccionario Del Programador", 
    font=("Roboto", 22, "bold"), fg="#F2F2F2", bg="#1B1259"
)
lbnav2.pack(side="left", padx=(40, 0))

btnVolver = tk.Button(
    nav2, text="Volver", bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=volver
)
btnVolver.pack(side="right", padx=(0, 10), pady=2)

# ------------------------------------------------------
# Sección "Agregar Término"
# ------------------------------------------------------

agregarTermino = tk.Frame(vn)

# ------------------------------------------------------
# Sección "Eliminar Término"
# ------------------------------------------------------

eliminarTermino = tk.Frame(vn)

# ------------------------------------------------------
# Sección "Bucar Término"
# ------------------------------------------------------

buscarTermino = tk.Frame(vn)

# ------------------------------------------------------
# Sección "Listar Término"
# ------------------------------------------------------

listarTermino = tk.Frame(vn)

# ------------------------------------------------------
# Sección "Acerca De"
# ------------------------------------------------------

acercaDe= tk.Frame(vn)


# ------------------------------------------------------
# Ejecutar la aplicación
# ------------------------------------------------------
Inicio()
vn.mainloop()
