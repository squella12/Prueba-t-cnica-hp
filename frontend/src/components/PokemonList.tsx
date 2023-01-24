import React from 'react';
import { useState, useEffect } from 'react';
import Button from './Button';
import Loading from './Loading';
import PokemonCard from './PokemonCard';


export default function PokemonList() {
    const [pokemon, setPokemon] = useState([]);
    const [url, setUrl] = useState('getpokemon/'); //url que se va a cambiar dependiendo del boton que se presione, el resto de la url está en package.json en "proxy"


    useEffect(() => {
        renderPokemons();
    }, [url]);

    //funcion que hace la peticion a la api a través de la url
    const renderPokemons = async () => {
        const response = await fetch(url);
        const data = await response.json();
        setPokemon(data);
        console.log(pokemon)
        
    };

    return(
        //si pokemon.length es 0, es decir, si no hay pokemons, se muestra el componente Loading, si no, se muestra el resto de la pagina
        pokemon.length === 0 ?
        <div>
            {/* Componente Loading, muestra un circulo girando mientras se carga la página */}
            <Loading />
        </div> 
        :
        <div className='bg-blue-300'>
        {/*Barra de navegacion */}
        <nav className="bg-blue-500">
            <div className="container mx-auto px-6 py-2 flex items-center justify-between">
                <div className="text-white font-medium text-lg">
                    <img className='w-40' src={require('../assets/Pokémon_logo.png')} alt={"Logo"}></img>
                </div>
                    <div>
                        {/* Botones que cambian la url para desplegar la información que tiene esa viewset de django */}
                        <Button handleClick={() => setUrl('pokemon/')} text='All Pokemons' />
                        <Button handleClick={() => setUrl('pokemonweight/')} text='Weight Filter'/>
                        <Button handleClick={() => setUrl('pokemontype/')} text='Type Grass Filter' />
                        <Button handleClick={() => setUrl('pokemontypeheight/')} text='Flying and Height Filter' />
                        <Button handleClick={() => setUrl('pokemonname/')} text='Reversed Name' />
                    </div>
                </div>
        </nav>
        <div className='bg-blue-700 w-60 mx-auto p-3 m-10 rounded-full shadow-2xl'>
            <h1 className='text-center text-3xl font-extrabold  text-yellow-500 '>Pokemon List</h1>
        </div>
            {/* Grid de pokemons utilizando pokemon Card */}
            <div className=' grid grid-cols-6 mx-auto w-10/12'>
                {pokemon.map((pokemon:any, index) => (
                    <PokemonCard pokemon={pokemon}/>
                ))}
            </div>
           
        </div>
    );
}
