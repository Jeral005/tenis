import  express  from "express";
import infoRoute from "./routes/info.Route"

const app =express();
app.use(express.json());
app.use(infoRoute);

const PORT =300;
app.listen(PORT,()=>{
    console.log(`servidor corriendo en http://localhost:${PORT}`);
});

//`` estos se llaman backticks, es el equivalente a usar comillas simples y dobles
// usa alt gr + corchete de bigote que cierra