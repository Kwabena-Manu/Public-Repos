import React from 'react'
import arrow_icon from '../assets/resources/breadcrum_arrow.png'

const BreadCrumbs = (props) => {
    const { product } = props;
    return (
        <div className='breadcrumbs'>
            Home <img src={arrow_icon} alt="" /> Shop <img src={arrow_icon} alt="" />  {product.category} <img src={arrow_icon} alt="" /> {product.name}
        </div>

    )
}

export default BreadCrumbs