import React from 'react'
import new_collections from '../assets/resources/new_collections'
import Item from './item'

const NewCollections = () => {
    return (
        <div className='new-collections'>
            <h1>New Collections</h1>
            <hr />
            <div className='new-collections-item'>
                {new_collections.map((item, i) => {
                    return <Item key={i} id={item.id} name={item.name} img={item.image} new_price={item.new_price} old_price={item.old_price} />
                })}
            </div>
        </div>
    )
}

export default NewCollections