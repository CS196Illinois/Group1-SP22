import './App.css';

function App() {
  const title = 'Welcome to the new blog';
  const likes = 50;
// react converts strings, numbers, arrays to a form of output; it cannot convert boolean and objects

  return (
    <div className="App">
      <div className = "content">
        <h1>{ title }</h1>
        <p>Liked { likes } times</p>
     
      </div>
   </div>
  );
}

export default App;
