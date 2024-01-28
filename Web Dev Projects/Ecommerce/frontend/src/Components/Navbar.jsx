import React, { useContext, useState } from 'react'
import logo from '../assets/images/logo.png'
import { Link } from 'react-router-dom'
import { ShopContext } from '../Context/ShopContext'

export const Navbar = () => {

    const [menu, setmenu] = useState("shop")
    const { getTotalCartItems } = useContext(ShopContext);
    return (
        <nav className="navbar navbar-expand-lg bg-body-tertiary p-2">
            <div className="container-fluid">
                <Link to="/" className="navbar-brand" href="#">
                    <img src={logo} className='img-thumbnail mx-2' alt="" />
                    SHOPPER
                </Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse " id="navbarText">
                    <ul className="navbar-nav w-100 d-flex justify-content-center mb-2 mb-lg-0">
                        <li onClick={() => { setmenu("shop") }} className="nav-item">
                            <Link to="/" className="nav-link" aria-current="page" href="#">Shop</Link>
                        </li>
                        <li onClick={() => { setmenu("men") }} className="nav-item">
                            <Link to='/men' className="nav-link" aria-current="page" href="#">Men</Link>
                        </li>
                        <li onClick={() => { setmenu("women") }} className="nav-item">
                            <Link to="/women" className="nav-link" aria-current="page" href="#">Women</Link>
                        </li>
                        <li onClick={() => { setmenu("kids") }} className="nav-item">
                            <Link to="/kids" className="nav-link" aria-current="page" href="#">Kids</Link>
                        </li>

                    </ul>
                    <div className='d-flex nav-login-cart'>
                        <Link to="/login" className='nav-login-cart--loginLink mx-3'>
                            <button className="rounded-pill d-inline px-5 ">
                                Login
                            </button>
                        </Link>
                        <Link to="/cart" className='nav-login-cart--loginLink pt-1'>
                            <span className='d-inline align-bottom  '>
                                <i className='fa fa-cart-shopping'></i>
                            </span>
                        </Link>
                        <div className="nav-cart-count ">
                            {getTotalCartItems()}
                        </div>

                    </div>
                </div>
            </div>
        </nav >
    )
}
