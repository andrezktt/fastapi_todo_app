import { Route, BrowserRouter as Router, Routes} from 'react-router-dom'

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/login' element={<h1>Login</h1>}></Route>
        <Route path='/register' element={<h1>Cadastro</h1>}></Route>
      </Routes>
    </Router>
  );
}

export default App;
