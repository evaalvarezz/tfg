import re
from flask import Flask
from flask import render_template,request,redirect,url_for,flash,session
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os
 

app=Flask(__name__)
app.secret_key="develoteca"


mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='comidas'
mysql.init_app(app)


CARPETA=os.path.join('imagenes')
app.config['CARPETA']=CARPETA

@app.route('/imagenes/<nombreDeFoto>')
def imagenes(nombreDeFoto):
    return send_from_directory(app.config['CARPETA'], nombreDeFoto)
#cerrar
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('correo', None)

    flash('Se ha cerrado sesión correctamente')
    return redirect(url_for('index'))

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password1']

        conn = mysql.connect()
        cursor = conn.cursor()

        # comprobar en la base de datos
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s", (correo, password))
        user = cursor.fetchone()

        if user:
            # Establecer sesion
            session['user_id'] = user[0]
            session['correo'] = user[2]
            flash('Se ha iniciado sesion correctamente')
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas')
            return redirect(url_for('login'))
    else:
        return render_template('recetas/login.html')
    

    
    

@app.route('/')
def index():
    sql="SELECT *FROM `recetas`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    recetas=cursor.fetchall()
    print(recetas)
    
    conn.commit()

    return render_template('recetas/index.html', recetas=recetas)

@app.route('/abajo')
def abajo():
  return render_template('abajo.html')

# enseñar todos los usuarios de la tabla
@app.route('/userAdmin1')
def index1():
    sql="SELECT *FROM `usuarios`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    usuarios=cursor.fetchall()
    print(usuarios)
    
    conn.commit()

    return render_template('recetas/userAdmin1.html', usuarios=usuarios)

# enseñar todos los comentario de la tabla
@app.route('/userAdmin2')
def index2():
    sql="SELECT *FROM `comentario`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    comentario=cursor.fetchall()
    print(comentario)
    
    conn.commit()

    return render_template('recetas/userAdmin2.html', comentario=comentario)

# eliminar una receta
@app.route('/destroy/<int:id>')
def destroy(id):
    conn=mysql.connect()
   
    cursor=conn.cursor()
    cursor.execute("SELECT foto FROM recetas WHERE id=%s", id)
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
    cursor.execute("DELETE FROM recetas WHERE id=%s",(id))
    conn.commit()
    return redirect('/userAdmin')

# eliminar un usuario
@app.route('/destroy1/<int:id>')
def destroy1(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
    conn.commit()
    return redirect('/userAdmin1')

# eliminar un comentario
@app.route('/destroy2/<int:id>')
def destroy2(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM comentario WHERE id=%s", (id,))
    conn.commit()
    return redirect('/userAdmin2')


# editar receta
@app.route('/edit/<int:id>')
def edit(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM recetas WHERE id=%s",(id))
    recetas=cursor.fetchall()
    conn.commit()
    
    return render_template('recetas/edit.html', recetas=recetas)



# Modificar los datos de la receta de el editar
@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _ingredientes=request.form['txtIngredientes']
    _pasos=request.form['txtPasos']
    _foto=request.files['txtFoto']
    _favorito=request.form['txtFavorito']
    id=request.form['txtId']

    
    sql="UPDATE `recetas` SET `nombre`=%s, `ingredientes`=%s, `pasos`=%s, `favorito`=%s  WHERE id=%s;"

    datos=(_nombre,_ingredientes,_pasos,_favorito,id)
    
    conn=mysql.connect()
    cursor=conn.cursor()
    
    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")

    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("imagenes/"+nuevoNombreFoto)
        
        cursor.execute("SELECT foto FROM recetas WHERE id=%s", id)
        fila=cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE recetas SET foto=%s WHERE id=%s",(nuevoNombreFoto,id))
        conn.commit()

    cursor.execute(sql,datos)
    conn.commit()  
    return redirect('/userAdmin') 


# crear una receta
@app.route('/create')
def create():
    return render_template('recetas/create.html')

# crear un ususario

@app.route('/create1')
def create1():
    return render_template('recetas/create1.html')

# mostrar las recetas a el usuario administardor

@app.route('/userAdmin')
def userAdmin():
    sql="SELECT *FROM `recetas`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    recetas=cursor.fetchall()
    print(recetas)
    
    conn.commit()
    return render_template('recetas/userAdmin.html', recetas=recetas)

# coger los datos para crear la receta
@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form['txtNombre']
    _ingredientes=request.form['txtIngredientes']
    _pasos=request.form['txtPasos']
    _foto=request.files['txtFoto']
    _favorito=request.form['txtFavorito']

    if _nombre=='' or _ingredientes=='' or _foto=='' or _pasos=='' or _favorito=='':
        flash('Rellene todos los campos')
        return redirect(url_for('create'))
    
    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")

    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("imagenes/"+nuevoNombreFoto)
    sql="INSERT INTO recetas VALUES (NULL, %s, %s, %s,%s,%s);"

    datos=(_nombre,_ingredientes,_pasos,nuevoNombreFoto,_favorito)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

# coger los datos para crear un usuario
@app.route('/store1', methods=['POST'])
def storage1():
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _correo=request.form['txtCorreo']
    _contrasena=request.form['txtContrasena']

    if _nombre=='' or _apellido=='' or _correo=='' or _contrasena=='':
        flash('Rellene todos los campos')
        return redirect(url_for('create1'))
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", _correo):
        flash('El formato del correo electrónico es incorrecto')
        return redirect(url_for('create1'))
    
    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")

    sql="INSERT INTO usuarios VALUES (NULL, %s, %s, %s,%s);"

    datos=(_nombre,_apellido,_correo,_contrasena)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')



# Vista de una receta con comentario
@app.route('/receta/<int:id>', methods=['GET', 'POST'])
def receta(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    # Obtener la receta
    cursor.execute("SELECT * FROM recetas WHERE id=%s", (id,))
    receta = cursor.fetchone()

    if receta:
        # Obtener los comentarios de la receta
        cursor.execute("SELECT * FROM comentario WHERE id_receta=%s", (id,))
        comentario = cursor.fetchall()

        if request.method == 'POST':
            # Añadir comentario
            nombre = request.form['nombre']
            contenido = request.form['contenido']
            if not re.match(r"[^@]+@[^@]+\.[^@]+", nombre):
                flash('El formato del correo electrónico es incorrecto')
               
           

            if nombre and contenido:
                cursor.execute("INSERT INTO comentario (id_receta, correo, comentario) VALUES (%s, %s, %s)",
                               (id, nombre, contenido))
                conn.commit()
                flash('Comentario agregado correctamente')
                return redirect(url_for('receta', id=id))

        conn.commit()
        return render_template('recetas/receta.html', receta=receta, comentario=comentario)
    else:
        flash('La receta no existe')
        return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)
