import React, { useState, useEffect} from 'react';

//Página de carga mientras los pokemones se guardan en la base de datos
export default function Loading() {
    return(
        
        <div className="flex flex-col justify-center items-center h-screen bg-blue-300">
            <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-purple-500"></div>
            <h1 className="text-2xl text-center text-purple-500">Loading...</h1>
            
        </div>
        
       
    );
}