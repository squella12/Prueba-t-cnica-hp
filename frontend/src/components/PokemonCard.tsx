
// Componente que muestra la información de cada pokemon
export default function PokemonCard({pokemon}:any) {
    return(
        <div key={pokemon.id} className="flex-row text-center bg-blue-500 rounded-3xl p-3 m-5">                  
            <img src={pokemon.img_1} alt={pokemon.name} className=" mx-auto " ></img>
            <h1>Nombre: {pokemon.name}</h1>
            <h1>Peso: {pokemon.weight}</h1>
            <h1>Altura: {pokemon.height}</h1>
            <h1>Tipo 1: {pokemon.type1}</h1>
            {pokemon.type2 && <h1>Tipo 2: {pokemon.type2}</h1>}
            </div>
    );
}
