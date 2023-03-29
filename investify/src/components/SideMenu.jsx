import '../styles/SideMenu.css';
import React from 'react';



function SideMenu() {


  return (
    <div className='side-menu'>
      <div className="top-heading">
        <h1>Investify</h1>
        <hr/>
      </div>
      <div className="menu-items">
        <br/>
        <h2>Stock & Data</h2>
        <ul>
          <li><a href="/Overview" >Overview</a></li>
          <li><a href="/ChatBot">ChatBot</a></li>
          <li><a href="/PricePredict">Stock Price Predictor</a></li>
        </ul>
        <h2>Portfolio</h2>
        <ul>
          <li><a href="/MyAccount">My Account</a></li>
          <li><a href="/MyTransacHistory">My Transaction History</a></li>
        </ul>
      </div>
    </div>
   
  );
}

export default SideMenu;
