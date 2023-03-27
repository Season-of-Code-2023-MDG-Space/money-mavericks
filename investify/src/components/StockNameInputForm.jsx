import React, { useState } from 'react';
import "../styles/StockNameInputForm.css"

const StockNameInputForm = () => {
  const [stockName, setStockName] = useState('');

  const handleInputChange = (event) => {
    setStockName(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // like fetch stock data from an API
    console.log(`Submitting stock name: ${stockName}`);
    setStockName(''); // clear the input field after submission
  };

  return (
    <div className="form-container ">
    <div className="form-wrapper">
    <form onSubmit={handleSubmit}>
      <label className='form-label'>
        Stock Name:
        <div className="form-input-wrapper">
        <input className="form-input" type="text" value={stockName} onChange={handleInputChange} />
        </div> 
      </label>
      <button className="form-button"type="submit">Submit</button>
    </form>
    </div>
    </div>
  );
};

export default StockNameInputForm;
