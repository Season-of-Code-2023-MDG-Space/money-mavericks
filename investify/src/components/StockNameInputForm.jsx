import React, { useState } from 'react';
import "../styles/StockNameInputForm.css"
import axios from 'axios';

const StockNameInputForm = () => {
  const [name, setStockName] = useState('');

  const handleInputChange = (event) => {
    setStockName(event.target.value);
  };

  function handleSubmit(event) {
    event.preventDefault();
    // like fetch stock data from an API
    let formfield = new FormData()
    formfield.append('name',name)
    axios.post('http://127.0.0.1:8000/Stock_Name/',formfield)
    console.log(`Submitting stock name: ${name}`);
    // setStockName(''); // clear the input field after submission
    window.location.href = '/Pricechart';
  };

  return (
    <div className="form-container ">
    <div className="form-wrapper">
    <form onSubmit={handleSubmit}>
      <label className='form-label'>
        Stock Name:
        <div className="form-input-wrapper">
        <input className="form-input" type="text" value={name} onChange={handleInputChange} />
        </div> 
      </label>
      <button className="form-button"type="submit">Submit</button>
    </form>
    </div>
    </div>
  );
};

export default StockNameInputForm;
