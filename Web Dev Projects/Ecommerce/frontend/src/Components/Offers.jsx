import React from 'react'
import exclusive_image from '../assets/resources/exclusive_image.png'

const Offers = () => {
    return (
        <div className='offers'>

            <div className="offers-left">
                <h1>Exclusive</h1>
                <h1>Offers For You</h1>
                <p>Only ON Best Selling Products</p>
                <button>Check Now</button>
            </div>
            <div className="offers-right">
                <img src={exclusive_image} alt="" />
            </div>
        </div>
    )
}

export default Offers