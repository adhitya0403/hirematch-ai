import React from 'react'

const Viewer = ({content}) => {
  return (
    <div className='border-2 border-dotted border-gray-700 rounded-md p-10'>
      <p className='text-white'>{content}</p>
    </div>
  )
}

export default Viewer
