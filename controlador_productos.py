from bd import obtener_conexion

def insertar_producto(idproducto, descripcion, precio, stock, disponible, idproveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO productos(idproducto, descripcion, precio, stock, disponible, idproveedor) VALUES (%s, %s, %s,%s, %s, %s)",
        (idproducto, descripcion, precio, stock, disponible, idproveedor))
    conexion.commit()
    conexion.close()

def obtener_producto():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idproducto, descripcion, precio, stock, disponible, idproveedor FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def eliminar_productos(idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE idproducto = %s", (idproducto,))
    conexion.commit()
    conexion.close()

def obtener_producto_por_id(idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM productos WHERE idproducto = %s", (idproducto,))
        producto = cursor.fetchone()
    return producto

def actualizar_producto(idproducto, descripcion, precio, stock, disponible, idproveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE productos SET descripcion = %s, precio = %s, stock = %s, disponible = %s, idproveedor = %s WHERE idproducto = %s",
        (descripcion, precio, stock, disponible, idproveedor, idproducto))
    conexion.commit()
    conexion.close()
    
