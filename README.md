# Servicio de Autentificación

### Para iniciar la API seguir los siguientes pasos.

Crear un entorno virtual y activar-lo.

```sh
python3 -m venv venv && source venv/bin/activate
```

Instalar las dependencias

```sh
pip3 install -r service/requirements.txt
```

Para iniciar-la os situais en el directorio `/service` y usamos `uvicorn`.

```sh
uvicorn app.main:app
```

- `--reload`: Reinicia la API cada vez que encuentra un canvio en los ficheros.
