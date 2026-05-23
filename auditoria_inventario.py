# =============================================================
#  AUDITORÍA DE INVENTARIO - PROBLEMA 3
#  Fundamentos de Programación
#  Herramienta de control de stock con matrices y funciones
# =============================================================

# ------------------------------------------------------------------
# FUNCIÓN: calcular_cantidad_pedido
# Determina cuántas unidades se deben pedir para cubrir el stock mínimo.
# Parámetros:
#   stock_actual   -- cantidad disponible actualmente en bodega
#   stock_minimo   -- cantidad mínima requerida para operación normal
# Retorno:
#   Diferencia entre stock_minimo y stock_actual si hay déficit, o 0.
# ------------------------------------------------------------------
def calcular_cantidad_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# ------------------------------------------------------------------
# MATRIZ DE INVENTARIO
# Estructura: [Código, Nombre del artículo, Stock actual, Stock mínimo]
# ------------------------------------------------------------------
inventario = [
    ["ART-001", "Papel Bond A4",              15,  50],
    ["ART-002", "Tóner HP LaserJet",           3,  10],
    ["ART-003", "Bolígrafos Azules (caja)",  120, 100],
    ["ART-004", "Carpetas Archivadoras",        8,  30],
    ["ART-005", "Memoria USB 32GB",             2,  15],
    ["ART-006", "Marcadores Permanentes",      45,  40],
    ["ART-007", "Resmas de Papel Carta",        6,  20],
]


# ------------------------------------------------------------------
# AUDITORÍA: recorre la matriz y reporta los artículos con déficit
# ------------------------------------------------------------------
print("=" * 65)
print("         REPORTE DE AUDITORÍA DE INVENTARIO")
print("=" * 65)
print(f"{'Código':<10} {'Artículo':<30} {'Stock':>6} {'Mínimo':>7} {'Pedido':>7}")
print("-" * 65)

articulos_con_deficit = []

for fila in inventario:
    codigo      = fila[0]
    nombre      = fila[1]
    stock_act   = fila[2]
    stock_min   = fila[3]

    cantidad_pedido = calcular_cantidad_pedido(stock_act, stock_min)

    if cantidad_pedido > 0:
        articulos_con_deficit.append([codigo, nombre, stock_act, stock_min, cantidad_pedido])
        print(f"{codigo:<10} {nombre:<30} {stock_act:>6} {stock_min:>7} {cantidad_pedido:>7}  *** PEDIR")

print("-" * 65)

# ------------------------------------------------------------------
# RESUMEN FINAL
# ------------------------------------------------------------------
print(f"\nTotal de artículos auditados   : {len(inventario)}")
print(f"Artículos con stock suficiente : {len(inventario) - len(articulos_con_deficit)}")
print(f"Artículos que requieren pedido : {len(articulos_con_deficit)}")
print()
print("Detalle de pedidos a realizar:")
print("-" * 65)
for art in articulos_con_deficit:
    print(f"  → {art[0]} | {art[1]:<30} | Pedir: {art[4]} unidades")
print("=" * 65)
