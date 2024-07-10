import {useEffect, useState } from 'react'
import './App.css'

function App() {
    const [movies, setMovies] = useState([])

    useEffect(() => {
      fetch("/movies")
        .then((r) => r.json())
        .then((movies) => setMovies(movies));
    }, []);

  

    

  return (
    <>
    <h1>
      Testing
    </h1>
        {
          movies.map((movie)=>{
            return(
              <div key={movie.id}>
                {movie.title}
              </div>
            )
          })
        }
    </>
  )
}

export default App;
