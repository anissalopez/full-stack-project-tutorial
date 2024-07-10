import {useEffect, useState } from 'react'
import './App.css'

function App() {
    const [movies, setMovies] = useState([])

    useEffect(() => {
      fetch("http://127.0.0.1:5555")
        .then((r) => r.json())
        .then((movies) => setMovies(movies));
    }, []);


  return (
    <>
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
