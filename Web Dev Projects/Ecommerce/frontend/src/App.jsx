import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { Navbar } from './Components/Navbar'
// import '../src/scss/styles.scss'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ShopCategory from './Pages/ShopCategory'
import Product from './Pages/Product'
import Cart from './Pages/Cart'
import LoginSignup from './Pages/LoginSignup'
import Shop from './Pages/Shop'
import Footer from './Components/Footer'
import men_banner from './assets/resources/banner_mens.png'
import women_banner from './assets/resources/banner_women.png'
import kids_banner from './assets/resources/banner_kids.png'

function App() {

  return (
    <>
      <div>
        <BrowserRouter>
          <Navbar />
          <Routes>
            <Route path='/' element={<Shop />} />
            <Route path='/men' element={<ShopCategory banner={men_banner} category="men" />} />
            <Route path='/women' element={<ShopCategory banner={women_banner} category="women" />} />
            <Route path='/kids' element={<ShopCategory banner={kids_banner} category="kid" />} />
            <Route path='/product' element={<Product />}>
              <Route path=':productId' element={<Product />} />
            </Route>
            <Route path='/cart' element={<Cart />} />
            <Route path='/login' element={<LoginSignup />} />
          </Routes>
          <Footer />
        </BrowserRouter>
      </div >
    </>
  )
}

export default App
