import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from 'react-router-dom'
import './App.css'
import HomePage from './Pages/HomePage/HomePage'
import MainLayout from './MainLayout/MainLayout'

function App() {

  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route path = '/' element= {<MainLayout/>}>
          <Route index element = {<HomePage/>}/>
        </Route>
        
      </>
    )
  )

  return (
    <>
      <RouterProvider router={router}/>
    </>
  )
}

export default App
