import React from 'react';
import '../styles/Navbar.css';

function Navbar() {
  return (
    <div className="navbar">
      <div className="navbar-logo">
      </div>
      <div className="navbar-search">
        <input type="text" placeholder="Search..." />
        <i className="fas fa-search"></i>
      </div>
    </div>
  );
}

export default Navbar;
