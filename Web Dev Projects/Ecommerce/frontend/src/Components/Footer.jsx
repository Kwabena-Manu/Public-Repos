import React from 'react'
import footer_logo from '../assets/resources/logo_big.png'
import instagram_icon from '../assets/resources/instagram_icon.png'
import pinterest_icon from '../assets/resources/pinterest_icon.png'
import whatsapp_icon from '../assets/resources/whatsapp_icon.png'


const Footer = () => {
    return (
        <div className='footer'>
            <div className='footer-logo'>
                <img src={footer_logo} alt="" />
                <p>SHOPPER</p>
            </div>
            <ul className='footer-links'>
                <li>Company</li>
                <li>Product</li>
                <li>Offices</li>
                <li>About</li>
                <li>Contact</li>
            </ul>

            <div className='footer-social-icons'>
                <div className="footer-icons container">
                    <img src={instagram_icon} alt="" />
                </div>
                <div className="footer-icons container">
                    <img src={pinterest_icon} alt="" />
                </div>
                <div className="footer-icons container">
                    <img src={whatsapp_icon} alt="" />
                </div>
            </div>

            <div className="footer-copyright">
                <hr />
                <p>Copyright @ 2023 - All rights researved.</p>
            </div>
        </div>
    )
}

export default Footer