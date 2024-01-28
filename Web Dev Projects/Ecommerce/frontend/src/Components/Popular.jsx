import React from 'react'
import data_product from '../assets/resources/data';
import Item from './item';


const Popular = () => {
    return (
        <div className='popular'>
            <h1>Popular For Women</h1>
            <hr />
            <div className='popular-item'>
                {data_product.map((item, i) => {
                    return <Item key={i} id={item.id} name={item.name} img={item.image} new_price={item.new_price} old_price={item.old_price} />
                })}
            </div>
        </div>
    )
}

export default Popular