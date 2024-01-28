import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import * as bootstrap from '../node_modules/bootstrap/dist/js/bootstrap.bundle.js'
import '../src/assets/css/styles.css'
import ShopContextProvider from './Context/ShopContext.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <ShopContextProvider>
    <App />
  </ShopContextProvider>,
)
