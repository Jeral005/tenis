import type {Request, Response}from "express";
import type {QueryResult} from "pg"
import {pool} from "../db";

export const getInfo=async(req: Request,res:Response):Promise<Response>=>{
    return res.status(200).json({
        "mensaje": "Bienvenidos a GeoQuery API",
        "status":200
    });
}


export const pruebaConexion = async (req: Request, res: Response): Promise<Response> => {
    try {
        const response: QueryResult = await pool.query('SELECT NOW()');
        console.log("conexión exitosa");
        return res.status(200).json(response.rows);
    } 
    catch (e) {
        console.log(e);
        return res.status(500).json({ "error": [`NodeJS dice ${e}`] })
    }
}