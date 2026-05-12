//aqui definimos los endpoints
//importamos el modulo de Router Express
import { Router } from "express";
//importamos las funciones de info.controler para usarlos como rutas 
import { getInfo } from "../controllers/info.controller";

const router = Router();//instaciamos un objeto de clase Router
//definimos una ruta con el metodo Get
router.get('/',getInfo)
//definimos una ruta con el metodo GETT para probar una conexion a postgresSQL
router.get('/pruebasConexion',getInfo);
//con esta linea permitimos que se pueda importar este codigo desde estos archivos
export default router;