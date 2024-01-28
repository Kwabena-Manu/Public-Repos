import React from 'react'
import hand_icon from '../assets/images/work.jpg'
import hero_img from '../assets/images/companies/company-4.png'

const Hero = () => {
    return (
        <div className='hero'>
            <div className="hero-left">
                <h2>NEW ARRIVALS ONLY</h2>
                <div>

                    <div className='hero-hand-icon'>
                        <p>new</p>
                        <span>
                            <i className='fas fa-hand'></i>
                        </span>
                    </div>
                    <p>Collections</p>
                    <p>For everyone</p>
                </div>
                <div className='hero-latest-btn'>
                    <div>Latest Collection</div>
                    <span>
                        <i className='fas fa-arrow-right'></i>
                    </span>
                </div>
            </div>
            <div className="hero-right">
                <img src={hero_img} alt="" />
            </div>
        </div>
    )
}

export default Hero